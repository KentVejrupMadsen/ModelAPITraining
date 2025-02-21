from ultralytics \
    import Model


class SystemModel:
    def __init__(
        self, 
        location: str
    ):
        self.model = Model(
            location = location,
            task     = 'detect',
            verbose  = False
        )
    
    def getModel(
        self
    ) -> Model:
        return self.model
    
    def setModel(
        self, 
        parameter: Model
    ) -> None:
        self.model = parameter
