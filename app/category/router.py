"""Category API router
"""

from fastapi import APIRouter, Depends, Header
from .. import helpers
from .. import constants
from .. import responses
from .constants import (
    TAGS,
    GET_CATEGORIES_OPERATION_ID,
    GET_CATEGORY_SERVICES_OPERATION_ID,
    CATEGORY_SERVICES_PATH,
    CATEGORIES_PATH,
)
from . import handlers
from . import models


router = APIRouter()


@router.get(
    CATEGORIES_PATH,
    dependencies=[Depends(helpers.validate_token(constants.READ_CATEGORIES_SCOPE))],
    tags=TAGS,
    operation_id=GET_CATEGORIES_OPERATION_ID,
    response_model=models.CategoriesListResponse,
    responses=responses.responses_descriptions,
)
def get_categories(
    active: bool = True,
    offset: int = 0,
    limit: int = 10,
    authorization: str = Header(..., convert_underscores=False),
) -> models.CategoriesListResponse:
    """Gets a list of categories for the application in context
    """
    request = models.GetCategoriesRequest(
        headers=models.CommonHeaders(
            authorization=authorization
        ),
        params=models.ListParams(
            active=active,
            offset=offset,
            limit=limit,
        ),
    )
    return handlers.get_categories(request)


@router.get(
    CATEGORY_SERVICES_PATH,
    dependencies=[Depends(helpers.validate_token(constants.READ_SERVICES_SCOPE))],
    tags=TAGS,
    operation_id=GET_CATEGORY_SERVICES_OPERATION_ID,
    response_model=models.CategoryServicesListResponse,
    responses=responses.responses_descriptions,
)
def get_category_services(  # pylint: disable=R0913
    category_id: int,
    active: bool = True,
    offset: int = 0,
    limit: int = 10,
    authorization: str = Header(..., convert_underscores=False),
) -> models.CategoryServicesListResponse:
    """Gets the list of services asociated to a category for an application in context
    """
    request = models.GetCategoryServicesRequest(
        categoryId=category_id,
        headers=models.CommonHeaders(
            authorization=authorization
        ),
        params=models.ListParams(
            active=active,
            offset=offset,
            limit=limit,
        ),
    )
    return handlers.get_category_services(request)
