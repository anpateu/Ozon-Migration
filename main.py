from config import Config
from api_ozon import OzonAPI
import pandas as pd


def load_products_from_CSV():
    goods_link = 'data\\products.csv'
    merge_link = 'data\\matching.xlsx'

    products = pd.read_csv(goods_link, sep=';', usecols=['Артикул', 'FBS OZON SKU ID',
                                                                         'Наименование товара',
                                                                         'Текущая цена с учетом скидки, руб.'])
    products = products.rename(columns={'Артикул': 'Код'})
    products = products.drop_duplicates()

    merge_dot = pd.read_excel(merge_link, usecols=['Код (поставщик)', 'QID'])
    merge_dot = merge_dot.rename(columns={'Код (поставщик)': 'Код'})
    merge_dot = merge_dot.drop_duplicates()

    merge_not_dot = pd.read_excel(merge_link, usecols=['Код', 'QID'])
    merge_not_dot = merge_not_dot.drop_duplicates()

    products_dot = products.query('Код.str.contains("\.")')
    products_not_dot = products.query('not Код.str.contains("\.")')

    result_AE = pd.merge(products_dot, merge_dot, on='Код')
    result_AE['QID'] = result_AE['QID'].astype(str)

    result_BS = pd.merge(products_not_dot, merge_not_dot, on='Код')
    result_BS['QID'] = result_BS['QID'].astype(str)

    return result_AE, result_BS

def add_item(product):
    x = {
        "sku": int(product[1]),
        "name": str(product[2]),
        "offer_id": str(product[4]),
        "currency_code": "RUB",
        "price": str(int(product[3])),
        "vat": "0"
    }
    return x

def do_migration(api):
    result_AE, result_BS = load_products_from_CSV()

    all_items = []
    for product in result_AE.values:
        if int(product[1]) != 0:
            all_items.append(add_item(product))
    for product in result_BS.values:
        if int(product[1]) != 0:
            all_items.append(add_item(product))

    items = []
    for i in range(0, len(all_items), 1000):
        items.append(all_items[i:i + 1000])

    for slice in items:
        api.create_products(slice)


if __name__ == '__main__':
    api = OzonAPI(client_id=Config.OZON_CLIENT_ID, api_key=Config.OZON_API_KEY)
    do_migration(api)