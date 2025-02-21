from Source.interfaces.credentials_manager \
    import CredentialsManager


class InterfaceManager:
    def __init__(
        self,
        credentials: CredentialsManager | None = None
    ):
        self.credentials: CredentialsManager | None = credentials
    
    def getCredentials(
        self
    ) -> CredentialsManager:
        return self.credentials
    
    def setCredentials(
        self, 
        parameter: CredentialsManager
    ) -> None:
        set.credentials = parameter
