class CredentialsManager:
    def __init__(
        self
    ):
        self.protocol:  str | None = 'http'
        self.uri:       str | None = '192.168.0.189'
        self.port:      int | None = 8080
    
    def getProtocol(
        self
    ) -> str:
        return self.protocol
    
    def setProtocol(
        self, 
        value: str
    ) -> None:
        self.protocol = value
    
    def getURI(
        self
    ) -> str:
        return self.uri
    
    def setURI(
        self, 
        value: str
    ) -> None:
        self.uri = value
    
    def getPort(
        self
    ) -> int:
        return self.port
    
    def setPort(
        self, 
        value: int
    ) -> None:
        self.port = value
    

    def getPortAsText(
        self
    ) -> str:
        if self.port is None:
            return str(
                0
            )
        
        return str(
            self.getPort()
        )
