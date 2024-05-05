"""Service API models
"""

from pydantic import BaseModel


class CreateAppointmentPayload(BaseModel):
    """Create appointment payload
    """

    date: str
    locationId: int
    categoryId: int


class CommonHeaders(BaseModel):
    """Common headers data
    """

    authorization: str


class CreateAppointmentRequest(BaseModel):
    """Create appointment request
    """

    serviceId: int
    headers: CommonHeaders
    payload: CreateAppointmentPayload


class CreateAppointmentResponse(BaseModel):
    """Create appointment response
    """

    id: int
    customerName: str
    categoryName: str
    locationName: str
    serviceName: str
    date: str
