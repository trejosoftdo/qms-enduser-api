"""Auth API models
"""

from pydantic import BaseModel


class RegisterUserPayload(BaseModel):
    """Register User payload
    """

    name: str
    username: str
    email: str
    password: str


class RegisterUserResponseData(BaseModel):
    """Register User response data
    """

    registered: bool

class RegisterUserResponse(BaseModel):
    """Register User response
    """

    data: RegisterUserResponseData


class LoginUserPayload(BaseModel):
    """Login User payload
    """

    username: str
    password: str

class LoginUserResponseData(BaseModel):
    """Login User response data
    """

    accessToken: str
    expiresIn: int


class LoginUserResponse(BaseModel):
    """Login User response
    """

    data: LoginUserResponseData


class LogoutUserResponseData(BaseModel):
    """Logout User response data
    """

    loggedOut: bool


class LogoutUserResponse(BaseModel):
    """Logout User response
    """

    data: LogoutUserResponseData


class ForgotPasswordPayload(BaseModel):
    """Forgot Password payload
    """

    email: str


class ForgotPasswordResponseData(BaseModel):
    """Forgot Password response data
    """

    emailSent: bool


class ForgotPasswordResponse(BaseModel):
    """Forgot Password response
    """

    data: ForgotPasswordResponseData
