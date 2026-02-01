class APIClientError(Exception):
    '''base class for Api client'''
    
class NetworkError(APIClientError):
    '''Raised when a network issue occurs'''
    
class TimeoutError(APIClientError):
    '''Raised when a request times out'''
    
class UnauthorizedError(APIClientError):
    """Raised for 401 responses."""


class NotFoundError(APIClientError):
    """Raised for 404 responses."""


class ServerError(APIClientError):
    """Raised for 5xx responses."""


class BadRequestError(APIClientError):
    """Raised for 400 responses."""