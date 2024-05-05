"""Location API mappers
"""

from . import models



def map_location(item: dict) -> models.Location:
    """Maps a location item from the given data

    Args:
        item (dict): location data

    Returns:
        models.Location: Mapped location
    """
    return models.Location(
        id=item.get("id"),
        name=item.get("name"),
        description=item.get("description"),
        address=item.get("address"),
        iconUrl=item.get("iconUrl", "app://city"),
        isActive=item.get("isActive"),
    )
