from requests import get

from interfaces.credentials_manager \
    import CredentialsManager

from interfaces.interface \
    import Interface


class ProjectInterface(
    Interface
):
    def __init__(
        self,
        credentials: CredentialsManager | None
    ):
        super().__init__(
            credentials = credentials
        )
    
    def getHeader(self):
        return {
            'Authorization': 'Token ' + self.getCredentialsManager().getToken()
        }

    def listProjects(self):
        response = get(
            url=str(
                self.getCredentialsManager().getProtocol() + 
                '://' + 
                self.getCredentialsManager().getURI() + 
                ':' +
                self.getCredentialsManager().getPortAsText() + 
                '/api/projects'
            ),
            headers=self.getHeader()
        )

        results = response.json()

        return {
            'number_of_projects': results['count'],
            'projects': results['results']
        }