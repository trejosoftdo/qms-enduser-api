"""Project environment variables
"""

import os
from dotenv import load_dotenv
from . import constants

load_dotenv()

auth_api_base_url = os.getenv(constants.AUTH_API_BASE_URL_ENV_NAME)
auth_application = os.getenv(constants.AUTH_APPLICATION_ENV_NAME)
admin_client_id = os.getenv(constants.ADMIN_CLIENT_ID_ENV_NAME)
admin_client_secret = os.getenv(constants.ADMIN_CLIENT_SECRET_ENV_NAME)
app_client_id = os.getenv(constants.APP_CLIENT_ID_ENV_NAME)
app_client_secret = os.getenv(constants.APP_CLIENT_SECRET_ENV_NAME)
iam_api_key = os.getenv(constants.IAM_API_KEY_ENV_NAME)
core_api_key = os.getenv(constants.CORE_API_KEY_ENV_NAME)
core_api_base_url = os.getenv(constants.CORE_API_BASE_URL_ENV_NAME)

test_auth_application = os.getenv(constants.TEST_AUTH_APPLICATION_ENV_NAME)
test_auth_username = os.getenv(constants.TEST_AUTH_USERNAME_ENV_NAME)
test_auth_password = os.getenv(constants.TEST_AUTH_PASSWORD_ENV_NAME)
