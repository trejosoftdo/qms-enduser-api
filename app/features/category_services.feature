
Feature: Categories services list endpoint
    As a consumer, I want an endpoint able to list of service categories in the context of an application

    Background:
        Given a request url "/api/v1/categories/1/services"

    Scenario: List category services success
        Given a device and user code have been obtained for scope "read_services"
        And the device has been authorized
        And access token has been obtained
        And the request query param "offset" to "0"
        And the request query param "limit" to "2"
        When the request sends "GET"
        Then the response status is "HTTP_200_OK"
        And the response total of items is equal to "2"
        And the response property "[0].name" is equal to "Cuenta de Ahorro"
        And the response property "[1].name" is equal to "Cuenta Corriente"


    Scenario: List category services invalid query params
        Given a device and user code have been obtained for scope "read_services"
        And the device has been authorized
        And access token has been obtained
        And the request query param "offset" to "bad_value"
        And the request query param "limit" to "bad_value"
        When the request sends "GET"
        Then the response status is "HTTP_400_BAD_REQUEST"
        And the response property "code" is equal to "BAD_REQUEST"
        And the response property "type" is equal to "VALIDATION_ERROR"
        And the response property "message" is equal to "value is not a valid integer (query.offset). value is not a valid integer (query.limit)"


    Scenario: List category services invalid token
        Given a device and user code have been obtained for scope "read_services"
        And the device has been authorized
        And access token has been obtained
        And access token is invalid
        When the request sends "GET"
        Then the response status is "HTTP_401_UNAUTHORIZED"


    Scenario: List category services unexpected scope
        Given a device and user code have been obtained for scope "read_serviceturns"
        And the device has been authorized
        And access token has been obtained
        When the request sends "GET"
        Then the response status is "HTTP_403_FORBIDDEN"
