"""Auth API constants
"""

TAGS = ["auth"]

# Operation Ids
LOGIN_OPERATION_ID = "login"
REGISTER_USER_OPERATION_ID = "registerUser"
LOGOUT_OPERATION_ID = "logout"
FORGOT_PASSWORD_OPERATION_ID = "forgotPassword"

# Route Internal paths
LOGIN_ROUTE_PATH = "/login"
LOGOUT_ROUTE_PATH = "/logout"
REGISTER_USER_ROUTE_PATH = "/register-user"
FORGOT_PASSWORD_ROUTE_PATH = "/forgot-password"

# External paths
AUTH_LOGIN_USER_EXTERNAL_PATH = "/api/v1/auth/login"
AUTH_LOGOUT_USER_EXTERNAL_PATH = "/api/v1/auth/logout"
AUTH_REGISTER_USER_EXTERNAL_PATH = "/api/v1/auth/register"
AUTH_FORGOT_PASSWORD_EXTERNAL_PATH = "/api/v1/auth/reset-password-email"
AUTH_TOKENS_EXTERNAL_PATH = "/api/v1/auth/tokens"
AUTH_TOKEN_VALIDATE_EXTERNAL_PATH = "/api/v1/auth/token/validate"
AUTH_USER_BASIC_DATA_EXTERNAL_PATH = "/api/v1/auth/user-basic-data"
AUTH_EXTERNAL_BASE_PATH = "/api/v1/auth/"
AUTH_TOKENS_FOR_CREDENTIALS_EXTERNAL_PATH="/api/v1/auth/tokens/for-credentials"
CUSTOMERS_EXTERNAL_PATH = "/api/v1/customers/"
