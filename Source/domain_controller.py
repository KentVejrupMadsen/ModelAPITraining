from interfaces.credentials_manager \
    import CredentialsManager

from interfaces.interface_manager \
    import InterfaceManager


class DomainController:
    def __init__(
        self, 
        manager: InterfaceManager = InterfaceManager(
            credentials=CredentialsManager()
        )
    ):
        self.manager = manager
    
    def getManager(
        self
    ) -> InterfaceManager | None:
        return self.manager
    
    def setManager(
        self, 
        parameter: InterfaceManager
    ) -> None:
        self.manager = parameter

    