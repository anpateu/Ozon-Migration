import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    OZON_CLIENT_ID = os.getenv('OZON_CLIENT_ID')
    OZON_API_KEY = os.getenv('OZON_API_KEY')
    MS_EMPLOYEE_ID = os.getenv('MS_EMPLOYEE_ID')
    MS_ORGANIZATION_ID = os.getenv('MS_ORGANIZATION_ID')
    MS_OZ_COUNTERPARTY_ID = os.getenv('MS_OZ_COUNTERPARTY_ID')
    MS_OZ_CONTRACT_ID = os.getenv('MS_OZ_CONTRACT_ID')

    # Data from the old cabinet will be deleted
    OLD_OZON_CLIENT_ID = os.getenv('OLD_OZON_CLIENT_ID')
    OLD_OZON_API_KEY = os.getenv('OLD_OZON_API_KEY')