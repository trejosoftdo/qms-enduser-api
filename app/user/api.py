"""User API helpers
"""

import requests
from .. import environment
from .. import constants
from . import models


def get_common_headers() -> dict:
    """Gets the request common headers

    Returns:
        dict: common headers
    """
    return {
        "Content-Type": constants.CONTENT_TYPE_JSON,
        "api_key": environment.core_api_key,
    }


def get_user_profile_data(authorization: str) -> requests.Response:
    """Gets the user profile data

    Args:
        authorization (str): User authorization

    Returns:
        requests.Response: The response from the core api.
    """
    url = f"{environment.core_api_base_url}/api/v1/customers/current"
    headers = {
        **get_common_headers(),
        "application": environment.auth_application,
        "authorization": authorization,
    }
    return requests.get(
        url, headers=headers, timeout=constants.TIMEOUT
    )

def get_appointments(req: models.GetAppointmentsRequest) -> requests.Response:
    """Gets the list of user appointments

    Args:
        req (models.GetAppointmentsRequest): Request to get appointments

    Returns:
        requests.Response: The response from the core api.
    """
    url = f"{environment.core_api_base_url}/api/v1/customers/current/appointments"
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
        url, headers=headers, params=params, timeout=constants.TIMEOUT
    )
