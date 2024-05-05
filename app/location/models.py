"""Location API models
"""

from typing import List
from pydantic import BaseModel


class Location(BaseModel):
    """Location data
    """

    id: int
    name: str
    description: str
    address: str
    iconUrl: str
    isActive: bool


class LocationListParams(BaseModel):
    """Location List params data
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


class GetLocationsRequest(BaseModel):
    """Get locations request
    """

    headers: CommonHeaders
    params: LocationListParams



LocationsListResponse = List[Location]
