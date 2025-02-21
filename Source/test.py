from interfaces.interface_manager \
    import InterfaceManager

from interfaces.credentials_manager \
    import CredentialsManager

manager = InterfaceManager(
    CredentialsManager()
)