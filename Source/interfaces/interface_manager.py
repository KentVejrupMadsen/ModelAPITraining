from interfaces.credentials_manager \
    import CredentialsManager

from interfaces.image_interface \
    import ImageInterface

from interfaces.project_interface \
    import ProjectInterface

from interfaces.task_interface \
    import TaskInterface

from interfaces.prediction_interface \
    import PredictionInterface


class InterfaceManager:
    def __init__(
        self,
        credentials: CredentialsManager | None 
    ):
        self.credentials: CredentialsManager | None = credentials

        self.imageInterface: ImageInterface | None              = ImageInterface(
            self.getCredentialsManager()
        )
        
        self.projectInterface: ProjectInterface | None          = ProjectInterface(
            self.getCredentialsManager()
        )

        self.taskInterface: TaskInterface | None                = TaskInterface(
            self.getCredentialsManager()
        )

        self.predictionInterface: PredictionInterface | None    = PredictionInterface(
            self.getCredentialsManager()
        )

        self.streamline()


    def getCredentialsManager(
        self
    ) -> CredentialsManager:
        return self.credentials
    
    def setCredentialsManager(
        self, 
        parameter: CredentialsManager
    ) -> None:
        set.credentials = parameter
    
    def streamline(
        self
    ):
        pass

