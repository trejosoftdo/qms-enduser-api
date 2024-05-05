"""Auth API helpers
"""

import requests
from .. import environment
from .. import constants
from .constants import (
    AUTH_LOGIN_USER_EXTERNAL_PATH,
    AUTH_EXTERNAL_BASE_PATH,
    LOGOUT_ROUTE_PATH,
    CUSTOMERS_EXTERNAL_PATH,
    AUTH_REGISTER_USER_EXTERNAL_PATH,
    AUTH_FORGOT_PASSWORD_EXTERNAL_PATH,
    AUTH_TOKEN_VALIDATE_EXTERNAL_PATH,
    AUTH_USER_BASIC_DATA_EXTERNAL_PATH,
    AUTH_TOKENS_FOR_CREDENTIALS_EXTERNAL_PATH,
)


def get_common_headers() -> dict:
    """Gets the request common headers

    Returns:
        dict: Common headers
    """
    return {
        "Content-Type": constants.CONTENT_TYPE_JSON,
        "api_key": environment.iam_api_key,
    }


def get_common_payload() -> dict:
    """Gets the request common payload

    Returns:
        dict: Common payload
    """
    return {
        "clientId": environment.app_client_id,
        "clientSecret": environment.app_client_secret,
    }


def get_admin_common_payload() -> dict:
    """Gets the admin request common payload

    Returns:
        dict: Admin Common payload
    """
    return {
        "clientId": environment.admin_client_id,
        "clientSecret": environment.admin_client_secret,
    }

def login(
    username: str,
    password: str,
    scopes=constants.USER_SCOPES
) -> requests.Response:
    """Logs in an user

    Args:
        username (str): The username
        password (str): The password
        scopes (List[str]): The user scopes
    Returns:
        requests.Response: The response from the auth API.
    """
    url = f"{environment.auth_api_base_url}{AUTH_LOGIN_USER_EXTERNAL_PATH}"
    payload = {
        **get_common_payload(),
        "scope": constants.SCOPES_SEPARATOR.join(scopes),
        "username": username,
        "password": password,
    }
    headers = {**get_common_headers(), "application": environment.auth_application}
    return requests.post(
        url, headers=headers, json=payload, timeout=constants.TIMEOUT
    )

def get_admin_authorization() -> str:
    """Gets admin access token

    Returns:
        str: The admin token
    """
    url = f"{environment.auth_api_base_url}{AUTH_TOKENS_FOR_CREDENTIALS_EXTERNAL_PATH}"
    payload = {
        **get_admin_common_payload(),
        "scope": "email profile write_customers",
    }
    headers = {
        **get_common_headers(),
        "application": environment.auth_application,
    }
    response = requests.post(
        url, headers=headers, json=payload, timeout=constants.TIMEOUT
    )
    data = response.json()
    token = data.get("data", {}).get("accessToken", "")
    return f"Bearer {token}"

def forgot_password(email: str) -> requests.Response:
    """Makes a request to a new password

    Args:
        email (str): User's email
    Returns:
        requests.Response: The response from the auth API.
    """
    url = f"{environment.auth_api_base_url}{AUTH_FORGOT_PASSWORD_EXTERNAL_PATH}?email={email}"
    payload = {
        **get_common_payload(),
    }
    headers = {
        **get_common_headers(),
        "application": environment.auth_application,
        "authorization": get_admin_authorization(),
    }
    return requests.post(
        url, headers=headers, json=payload, timeout=constants.TIMEOUT
    )

def logout(user_id: str) -> requests.Response:
    """Logs out an user

    Args:
        id (str): Id of the user
    Returns:
        requests.Response: The response from the auth API.
    """
    url = f"{environment.auth_api_base_url}{AUTH_EXTERNAL_BASE_PATH}{user_id}{LOGOUT_ROUTE_PATH}"
    authorization = get_admin_authorization()
    headers = {
        **get_common_headers(),
        "application": environment.auth_application,
        "authorization": authorization,
    }
    return requests.post(
        url, headers=headers, timeout=constants.TIMEOUT
    )


def validate_token(
    authorization: str,
    expected_scope: str
) -> requests.Response:
    """Gets information such as scope and active from the given token

    Args:
        authorization (str): The access token to validate
        expected_scope (str): The expected scope

    Returns:
        requests.Response: The response from the auth API.
    """
    validate_token_url = (
        f"{environment.auth_api_base_url}{AUTH_TOKEN_VALIDATE_EXTERNAL_PATH}"
    )
    payload = {
        **get_common_payload(),
        "expectedScope": expected_scope,
    }
    headers = {
        **get_common_headers(),
        "application": environment.auth_application,
        "authorization": authorization,
    }
    return requests.post(
        validate_token_url, headers=headers, json=payload, timeout=constants.TIMEOUT
    )


def get_user_basic_data(authorization: str) -> requests.Response:
    """Gets the user basic data

    Args:
        authorization (str): The access token

    Returns:
        requests.Response: The response from the auth API.
    """
    url = (
        f"{environment.auth_api_base_url}{AUTH_USER_BASIC_DATA_EXTERNAL_PATH}"
    )
    payload = {
        **get_common_payload(),
    }
    headers = {
        **get_common_headers(),
        "application": environment.auth_application,
        "authorization": authorization,
    }
    return requests.post(
        url, headers=headers, json=payload, timeout=constants.TIMEOUT
    )

def register_user(
    name: str,
    username: str,
    email: str,
    password: str,
) -> requests.Response:
    """Registers a new user

    Args:
        name (str): The name of the user
        username (str): The username
        email (str): The email of the user
        password (str): The password
    Returns:
        requests.Response: The response from the auth API.
    """
    url = f"{environment.auth_api_base_url}{AUTH_REGISTER_USER_EXTERNAL_PATH}"
    payload = {
        **get_common_payload(),
        "username": username,
        "firstName": name,
        "lastName": "",
        "email": email,
        "password": password
    }

    headers = {
        **get_common_headers(),
        "application": environment.auth_application,
        "authorization": get_admin_authorization(),
    }
    return requests.post(
        url, headers=headers, json=payload, timeout=constants.TIMEOUT
    )


def create_customer(
    name: str,
    username: str,
    email: str,
) -> requests.Response:
    """Registers a new user

    Args:
        name (str): The name of the user
        username (str): The username
        email (str): The email of the user
        authorization (str): The authorization token
    Returns:
        requests.Response: The response from the auth API.
    """
    url = f"{environment.core_api_base_url}{CUSTOMERS_EXTERNAL_PATH}"
    payload = {
        **get_common_payload(),
        "username": username,
        "firstName": name,
        "lastName": "",
        "email": email,
        # The value should make it optional with a default
        "gender": "N/S",
        # The value should make it optional with a default
        "yearOfBirth": 1970,
        # The value should make it optional with a default
        "statusId": 8,
    }

    headers = {
        **get_common_headers(),
        "application": environment.auth_application,
        "api_key": environment.core_api_key,
        "authorization": get_admin_authorization(),
    }
    return requests.post(
        url, headers=headers, json=payload, timeout=constants.TIMEOUT
    )
