"""Service API helpers
"""

import requests
from .. import environment
from .. import constants
from . import models
from .constants import CUSTOMERS_EXTERNAL_PATH, APPOINTMENTS_EXTERNAL_PATH


def get_common_headers() -> dict:
    """Gets the common headers

    Returns:
        dict: common headers data
    """
    return {
        "Content-Type": "application/json",
        "api_key": environment.core_api_key,
    }


def create_appointment(request: models.CreateAppointmentRequest) -> requests.Response:
    """Creates a appointment for the given service

    Args:
        request (models.CreateAppointmentRequest): Request to create the appointment

    Returns:
        requests.Response: The response from the core api.
    """
    base_path = f"{environment.core_api_base_url}{CUSTOMERS_EXTERNAL_PATH}"
    url = f"{base_path}{APPOINTMENTS_EXTERNAL_PATH}"
    headers = {
        **get_common_headers(),
        "application": environment.auth_application,
        "authorization": request.headers.authorization,
    }
    payload = {
        "serviceId": request.serviceId,
        "locationId": request.payload.locationId,
        "date": request.payload.date,
    }
    return requests.post(url, headers=headers, json=payload, timeout=constants.TIMEOUT)
