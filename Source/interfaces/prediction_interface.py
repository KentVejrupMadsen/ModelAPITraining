import requests

from interfaces.credentials_manager \
    import CredentialsManager

from interfaces.interface \
    import Interface


class PredictionInterface(
    Interface
):
    def __init__(
        self,
        credentials: CredentialsManager | None
    ):
        super().__init__(
            credentials=credentials
        )
