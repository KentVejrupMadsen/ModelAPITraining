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
        self.imageInterface: ImageInterface | None           = ImageInterface(None)
        self.projectInterface: ProjectInterface | None       = ProjectInterface(None)
        self.taskInterface: TaskInterface | None             = TaskInterface(None)
        self.predictionInterface: PredictionInterface | None = PredictionInterface(None)

        self.credentials: CredentialsManager | None = credentials

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
        self.imageInterface.setCredentialsManager(
            self.getCredentialsManager()
        )

        self.projectInterface.setCredentialsManager(
            self.getCredentialsManager()
        )

        self.taskInterface.setCredentialsManager(
            self.getCredentialsManager()
        )

        self.predictionInterface.setCredentialsManager(
            self.getCredentialsManager()
        )
        

