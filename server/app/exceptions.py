from fastapi import HTTPException, status


class MarketplaceException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = ''

    def __init__(self, detail: str | None = None):
        super().__init__(
            status_code=self.status_code, detail=detail or self.detail
        )


class ObjectAlreadyExistsException(MarketplaceException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Объект с указанными данными уже существует.'


class NotFoundException(MarketplaceException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Данные не найдены.'


class DatabaseErrorException(MarketplaceException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = 'Произошла ошибка при работе с базой данных.'
