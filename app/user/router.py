"""User API router
"""

from fastapi import APIRouter, Depends, Header
from .. import helpers
from .. import constants
from .. import responses
from .constants import (
    TAGS,
    GET_APPOINTMENTS_OPERATION_ID,
    APPOINTMENTS_PATH,
    GET_HOME_DATA_OPERATION_ID,
    GET_PROFILE_DATA_OPERATION_ID,
    HOME_DATA_PATH,
    PROFILE_DATA_PATH,
)
from . import handlers
from . import models


router = APIRouter()


@router.get(
    APPOINTMENTS_PATH,
    dependencies=[Depends(helpers.validate_token(constants.READ_OWN_APPOINTMENTS_SCOPE))],
    tags=TAGS,
    operation_id=GET_APPOINTMENTS_OPERATION_ID,
    response_model=models.AppointmentsListResponse,
    responses=responses.responses_descriptions,
)
def get_appointments(
    active: bool = True,
    offset: int = 0,
    limit: int = 10,
    authorization: str = Header(..., convert_underscores=False),
) -> models.AppointmentsListResponse:
    """Gets the list of user appointments
    """
    request = models.GetAppointmentsRequest(
        headers=models.CommonHeaders(
            authorization=authorization
        ),
        params=models.AppointmentListParams(
            active=active,
            offset=offset,
            limit=limit,
        ),
    )
    return handlers.get_appointments(request)


@router.get(
    HOME_DATA_PATH,
    dependencies=[Depends(helpers.validate_token(constants.READ_HOME_DATA_SCOPE))],
    tags=TAGS,
    operation_id=GET_HOME_DATA_OPERATION_ID,
    response_model=models.HomeDataResponse,
    responses=responses.responses_descriptions,
)
def get_home_data(
    authorization: str = Header(..., convert_underscores=False),
) -> models.HomeDataResponse:
    """Get User Home Data
    """
    return handlers.get_home_data(authorization)


@router.get(
    PROFILE_DATA_PATH,
    dependencies=[Depends(helpers.validate_token(constants.READ_PROFILE_DATA_SCOPE))],
    tags=TAGS,
    operation_id=GET_PROFILE_DATA_OPERATION_ID,
    response_model=models.ProfileDataResponse,
    responses=responses.responses_descriptions,
)
def get_profile_data(
    authorization: str = Header(..., convert_underscores=False),
) -> models.ProfileDataResponse:
    """Get User Profile Data
    """
    return handlers.get_profile_data(authorization)
