"""Auth API router
"""

from fastapi import APIRouter, Header
from .. import responses
from . import handlers
from . import models
from . import constants


router = APIRouter()


@router.post(
    constants.LOGIN_ROUTE_PATH,
    tags=constants.TAGS,
    operation_id=constants.LOGIN_OPERATION_ID,
    response_model=models.LoginUserResponse,
    responses=responses.responses_descriptions,
)
def login(payload: models.LoginUserPayload) -> models.LoginUserResponse:
    """Logs in an user
    """
    return handlers.login(payload)


@router.post(
    constants.REGISTER_USER_ROUTE_PATH,
    tags=constants.TAGS,
    operation_id=constants.REGISTER_USER_OPERATION_ID,
    response_model=models.RegisterUserResponse,
    responses=responses.responses_descriptions,
)
async def register_user(payload: models.RegisterUserPayload) -> models.RegisterUserResponse:
    """Registers a new user
    """
    return handlers.register_user(payload)

@router.get(
    constants.LOGOUT_ROUTE_PATH,
    tags=constants.TAGS,
    operation_id=constants.LOGOUT_OPERATION_ID,
    response_model=models.LogoutUserResponse,
    responses=responses.responses_descriptions,
)
def logout(authorization: str = Header(..., convert_underscores=False),) -> models.LogoutUserResponse:
    """Logs out an user
    """
    return handlers.logout(authorization)

@router.post(
    constants.FORGOT_PASSWORD_ROUTE_PATH,
    tags=constants.TAGS,
    operation_id=constants.FORGOT_PASSWORD_OPERATION_ID,
    response_model=models.ForgotPasswordResponse,
    responses=responses.responses_descriptions,
)
def forgot_password(payload: models.ForgotPasswordPayload) -> models.ForgotPasswordResponse:
    """Makes a request to a new password
    """
    return handlers.forgot_password(payload)