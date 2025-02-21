from interfaces.interface \
    import Interface

from domain_controller \
    import DomainController


class ApplicationFramework:
    def __init__(
        self
    ):
        self.interface = None
        self.controller = None

    def initialise(
        self
    ):
        self.setInterface(
            Interface()
        )

        self.setController(
            DomainController(
                self.getInterface()
            )
        )

    def execute(
        self
    ):
        pass

    def garbage(
        self
    ):
        pass

    def getController(
        self
    ) -> DomainController | None:
        return self.controller
    
    def setController(
        self, 
        parameter: DomainController
    ) -> None:
        self.controller = parameter

    def getInterface(
        self
    ) -> Interface | None:
        return self.interface

    def setInterface(
        self,
        parameter: Interface
    ) -> None:
        self.interface = parameter
