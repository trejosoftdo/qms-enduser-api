"""User API handlers
"""

from . import models
from . import api
from . import mappers


def get_appointments(req: models.GetAppointmentsRequest) -> models.AppointmentsListResponse:
    """Gets list of appointments

    Args:
        req (models.GetAppointmentsRequest): The request to get the list of appointments

    Returns:
        models.AppointmentsListResponse: List of appointments
    """
    response = api.get_appointments(req)
    data = response.json()
    return list(map(mappers.map_appointment, data['appointments']))


def get_profile_data(authorization: str) -> models.ProfileDataResponse:
    """Gets the profile data

    Args:
        authorization (str): The user authorization

    Returns:
        models.ProfileDataResponse: Profile data
    """
    response = api.get_user_profile_data(authorization)
    user_data = response.json()
    return models.ProfileDataResponse(
        user=mappers.map_user(user_data)
    )

def get_home_data(authorization: str) -> models.HomeDataResponse:
    """Gets the home data

    Args:
        authorization (str): The user authorization

    Returns:
        models.HomeDataResponse: Home data
    """
    request = models.GetAppointmentsRequest(
        headers=models.CommonHeaders(
            authorization=authorization
        ),
        params=models.AppointmentListParams(
            active=True,
            offset=0,
            limit=10,
        ),
    )

    response = api.get_appointments(request)
    data = response.json()

    return models.HomeDataResponse(
        user=mappers.map_user(data['customer']),
        appointments=list(map(mappers.map_appointment, data['appointments']))
    )
