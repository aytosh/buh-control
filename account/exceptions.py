from rest_framework.exceptions import APIException
from rest_framework import status

class AccountException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "invalid_credentials"
    default_detail = "Invalid username or password"

