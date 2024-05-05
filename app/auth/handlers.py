"""Auth API handlers
"""

from .. import helpers
from . import models
from . import api


def login(payload: models.LoginUserPayload) -> models.LoginUserResponse:
    """Logs in an user

    Args:
        payload (models.LoginUserPayload): The login payload

    Returns:
        models.LoginUserResponse: The login response
    """
    response = api.login(payload.username, payload.password)

    helpers.handle_error_response(response)

    data = response.json().get("data", {})
    return models.LoginUserResponse(
        data=models.LoginUserResponseData(
            accessToken=data.get("accessToken"),
            expiresIn=data.get("expiresIn"),
        )
    )


def register_user(payload: models.RegisterUserPayload) -> models.RegisterUserResponse:
    """Registers a new user

    Args:
        payload (models.RegisterUserPayload): The registration payload

    Returns:
        models.RegisterUserResponse: The registration response
    """
    response = api.register_user(
        payload.name,
        payload.username,
        payload.email,
        payload.password,
    )

    helpers.handle_error_response(response)

    create_customer_response = api.create_customer(
        payload.name,
        payload.username,
        payload.email,
    )

    helpers.handle_error_response(create_customer_response)

    data = response.json()
    return models.RegisterUserResponse(
        data=models.RegisterUserResponseData(
            registered=data.get('registered'),
        )
    )


def logout(authorization: str) -> models.LogoutUserResponse:
    """Logs out an user

    Args:
        authorization (str): the user authorization token

    Returns:
        models.LogoutUserResponse: The login response
    """
    user_data_response = api.get_user_basic_data(authorization)

    helpers.handle_error_response(user_data_response)

    user_data = user_data_response.json()

    user_id = user_data.get('data', {}).get('id', '')
    response = api.logout(user_id)

    helpers.handle_error_response(response)

    data = response.json().get("data", {})
    return models.LogoutUserResponse(
        data=models.LogoutUserResponseData(
            loggedOut = data.get("loggedOut", False),
        )
    )

def forgot_password(payload: models.ForgotPasswordPayload) -> models.ForgotPasswordResponse:
    """Makes a request to a new password

    Args:
        payload (models.ForgotPasswordPayload): The forgot password payload

    Returns:
        models.ForgotPasswordResponse: The forgot password response response
    """
    response = api.forgot_password(payload.email)

    helpers.handle_error_response(response)

    data = response.json().get("data", {})
    return models.ForgotPasswordResponse(
        data=models.ForgotPasswordResponseData(
            emailSent = data.get("emailSent"),
        )
    )