"""Location API helpers
"""

import requests
from .. import environment
from .. import constants
from . import models
from .constants import LOCATIONS_EXTERNAL_PATH


def get_common_headers() -> dict:
    """Gets the request common headers

    Returns:
        dict: common headers
    """
    return {
        "Content-Type": constants.CONTENT_TYPE_JSON,
        "api_key": environment.core_api_key,
    }


def get_locations(req: models.GetLocationsRequest) -> requests.Response:
    """Gets the list of available locations for the application in context

    Args:
        req (models.GetLocationsRequest): Request to get locations

    Returns:
        requests.Response: The response from the core api.
    """
    locations_url = f"{environment.core_api_base_url}{LOCATIONS_EXTERNAL_PATH}"
    params = {
        "active": req.params.active,
        "offset": req.params.offset,
        "limit": req.params.limit,
    }
    headers = {
        **get_common_headers(),
        "application": environment.auth_application,
        "authorization": req.headers.authorization,
    }
    return requests.get(
        locations_url, headers=headers, params=params, timeout=constants.TIMEOUT
    )
