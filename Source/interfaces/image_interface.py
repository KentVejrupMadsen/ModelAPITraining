import requests

from interfaces.interface \
    import Interface

from interfaces.credentials_manager \
    import CredentialsManager



class ImageInterface(
    Interface
):
    def __init__(
        self,
        credentials: CredentialsManager | None = None
    ):
        super().__init__(
            credentials=credentials
        )
    