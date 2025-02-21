from Source.interfaces.credentials_manager \
    import CredentialsManager


class Interface:
    def __init__(
        self,
        credentials: CredentialsManager | None = None
    ):
        self.credentials: CredentialsManager | None = credentials
