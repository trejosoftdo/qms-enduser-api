"""Service API router
"""

from fastapi import APIRouter, Depends, Header
from .. import constants
from .. import responses
from .constants import TAGS, CREATE_APPOINTMENT_OPERATION_ID, APPOINTMENTS_PATH
from .. import helpers
from . import handlers
from . import models

router = APIRouter()


@router.post(
    APPOINTMENTS_PATH,
    dependencies=[Depends(helpers.validate_token(constants.CREATE_OWN_APPOINTMENTS_SCOPE))],
    tags=TAGS,
    operation_id=CREATE_APPOINTMENT_OPERATION_ID,
    response_model=models.CreateAppointmentResponse,
    responses=responses.responses_descriptions,
)
def create_appointment(
    service_id: int,
    payload: models.CreateAppointmentPayload,
    authorization: str = Header(..., convert_underscores=False),
) -> models.CreateAppointmentResponse:
    """Creates an appointment for the given service
    """
    request = models.CreateAppointmentRequest(
        headers=models.CommonHeaders(
            authorization=authorization,
        ),
        payload=payload,
        serviceId=service_id,
    )
    return handlers.create_appointment(request)
