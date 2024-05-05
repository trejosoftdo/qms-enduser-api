"""User API mappers
"""

from . import models

def map_user(item: dict) -> models.User:
    """Maps user data

    Args:
        item (dict): user data

    Returns:
        models.User: Mapped user
    """
    first_name = item.get("firstName", "")
    last_name = item.get("lastName", "")
    full_name = f"{first_name} {last_name}"
    return models.User(
        id=item.get("id"),
        fullName=full_name,
        username=item.get("username", ""),
        email=item.get("email"),
        imageUrl=item.get("imageUrl", "https://cdn.iconscout.com/icon/free/png-256/free-avatar-370-456322.png?f=webp"),
    )

def map_appointment(item: dict) -> models.Appointment:
    """Maps a appointment item from the given data

    Args:
        item (dict): appointment data

    Returns:
        models.Appointment: Mapped appointment
    """
    location = item.get('location', {})
    service = item.get('service', {})
    category = service.get('category', {})
    category_name = category.get('name', '')
    service_name = service.get('name', '')
    location_name = location.get('name', 'N/A')
    date = item.get('serviceEndingExpected', '')

    return models.Appointment(
        id=item.get("id"),
        category=category_name,
        service=service_name,
        location=location_name,
        date=date,
    )
