class APICredentials:
    def __init__(
        self
    ):
        self.uri = 'http://192.168.0.189:8080'
        self.token = '3b5c3ed6d6799a0909c3b1c5b2a58a929bd67af1'
    
    def getToken(
        self
    ) -> str:
        return self.token
    
    def getTokenHeaderString(
        self
    ) -> str:
        return str(
            'Token ' 
            + 
            self.token
        )
    
