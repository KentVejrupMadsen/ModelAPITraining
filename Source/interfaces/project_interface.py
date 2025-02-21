import requests

from interfaces.credentials_manager \
    import CredentialsManager

from interfaces.interface \
    import Interface


class ProjectInterface(
    Interface
):
    def __init__(
        self,
        credentials: CredentialsManager | None = None
    ):
        super(
            credentials
        )
    