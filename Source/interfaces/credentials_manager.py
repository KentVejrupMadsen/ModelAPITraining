class CredentialsManager:
    def __init__(
        self
    ):
        self.protocol:  str | None = 'http'
        self.uri:       str | None = '192.168.0.189'
        self.port:      int | None = 8080
        self.token:     str | None = '3b5c3ed6d6799a0909c3b1c5b2a58a929bd67af1'
    
    def getToken(
        self
    ) -> str:
        return self.token
    
    def setToken(
        self, 
        value: str
    ) -> None:
        self.token = value

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
