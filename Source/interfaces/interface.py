from interfaces.credentials_manager \
    import CredentialsManager


class Interface:
    def __init__(
        self,
        credentials: CredentialsManager | None = None
    ):
        self.credentials: CredentialsManager | None = credentials

    
    def getCredentialsManager(
        self
    ) -> CredentialsManager:
        return self.credentials
    
    def setCredentialsManager(
        self, 
        parameter: CredentialsManager
    ) -> None:
        self.credentials = parameter