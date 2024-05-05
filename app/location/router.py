"""Location API router
"""

from fastapi import APIRouter, Depends, Header
from .. import helpers
from .. import constants
from .. import responses
from .constants import (
    TAGS,
    GET_LOCATIONS_OPERATION_ID,
    LOCATIONS_PATH,
)
from . import handlers
from . import models


router = APIRouter()


@router.get(
    LOCATIONS_PATH,
    dependencies=[Depends(helpers.validate_token(constants.READ_LOCATIONS_SCOPE))],
    tags=TAGS,
    operation_id=GET_LOCATIONS_OPERATION_ID,
    response_model=models.LocationsListResponse,
    responses=responses.responses_descriptions,
)
def get_locations(
    active: bool = True,
    offset: int = 0,
    limit: int = 10,
    authorization: str = Header(..., convert_underscores=False),
) -> models.LocationsListResponse:
    """Gets a list of locations
    """
    request = models.GetLocationsRequest(
        headers=models.CommonHeaders(
            authorization=authorization
        ),
        params=models.LocationListParams(
            active=active,
            offset=offset,
            limit=limit,
        ),
    )
    return handlers.get_locations(request)
