"""Location API handlers
"""

from . import models
from . import api
from . import mappers


def get_locations(req: models.GetLocationsRequest) -> models.LocationsListResponse:
    """Get list of locations

    Args:
        req (str): The request to get the list of locations

    Returns:
        models.LocationsListResponse: List of locations
    """
    response = api.get_locations(req)
    locations = response.json()
    return list(map(mappers.map_location, locations))
