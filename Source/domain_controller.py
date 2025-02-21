from Source.interfaces.interface \
    import Interface


class DomainController:
    def __init__(
        self, 
        interface: Interface
    ):
        self.interface = interface
    
    def getInterface(
        self
    ) -> Interface | None:
        return self.interface
    
    def setInterface(
        self, 
        parameter: Interface
    ) -> None:
        self.interface = parameter

    