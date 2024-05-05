"""Service API mappers
"""

from . import models

def map_appointment(data: dict) -> models.CreateAppointmentResponse:
    """Maps the appointment response from data
    
    Args:
        data (dict): response data

    Returns:
        models.CreateAppointmentResponse: Created appointment data
    """
    customer = data.get('customer', {})
    category = data.get('category', {})
    location = data.get('location', {})
    service = data.get('service', {})
    customer_name = f"{customer.get('firstName', '')} {customer.get('lastName', '')}"
    category_name = category.get('name', '')
    location_name = location.get('name', '')
    service_name = service.get('name', '')
    return models.CreateAppointmentResponse(
      id = data.get('id'),
      customerName = customer_name,
      categoryName = category_name,
      locationName = location_name,
      serviceName = service_name,
      date = data.get('date', ''),
    )
