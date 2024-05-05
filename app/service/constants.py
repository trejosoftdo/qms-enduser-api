"""Service API constants
"""

TAGS = ["services"]

# Operation Ids
CREATE_APPOINTMENT_OPERATION_ID = "createAppointment"

# Internal route paths
APPOINTMENTS_PATH = "/{service_id}/appointments"


# External paths
SERVICES_EXTERNAL_PATH = "/api/v1/services/"
CUSTOMERS_EXTERNAL_PATH = "/api/v1/customers/"
APPOINTMENTS_EXTERNAL_PATH = "current/appointments"
