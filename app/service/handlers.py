"""Service API handlers
"""

from . import models
from . import api
from . import mappers


def create_appointment(
    request: models.CreateAppointmentRequest,
) -> models.CreateAppointmentResponse:
    """Creates a appointment for the given service

    Args:
        request (models.CreateAppointmentRequest): Request for creating the appointment

    Returns:
        models.CreateAppointmentResponse: Created appointment
    """
    response = api.create_appointment(request)
    item = response.json()
    return mappers.map_appointment(item)
