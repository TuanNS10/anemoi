from BuildingBlocks.Application.Responses.ErrorDetailResponse import ErrorDetailResponse


class GlobalErrors:
    @staticmethod
    def unexpected_error() -> ErrorDetailResponse:
        return ErrorDetailResponse(messages=["UnexpectedError"], code="500")
    