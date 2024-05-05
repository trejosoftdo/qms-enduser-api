"""User API models
"""

from typing import List
from pydantic import BaseModel

class Appointment(BaseModel):
    """Appointment data
    """

    id: int
    category: str
    service: str
    location: str
    date: str

class User(BaseModel):
    """User data
    """

    id: int
    username: str
    email: str
    fullName: str
    imageUrl: str


class AppointmentListParams(BaseModel):
    """Appointment List params data
    """

    active: bool
    offset: int
    limit: int


class CommonHeaders(BaseModel):
    """Common headers data

    Args:
        BaseModel (class): Base model class
    """

    authorization: str


class GetAppointmentsRequest(BaseModel):
    """Get locations request
    """

    headers: CommonHeaders
    params: AppointmentListParams

class ProfileDataResponse(BaseModel):
    """Profile data response
    """
    user: User

class HomeDataResponse(BaseModel):
    """Home data response
    """
    user: User
    appointments: List[Appointment]

AppointmentsListResponse = List[Appointment]
