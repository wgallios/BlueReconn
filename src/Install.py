from cement.core import controller

class Install(controller.CementBaseController):
    class Meta:
        interface = controller.IController
        label = 'installer'
        description = 'Installer for bluetooth daemon'
        stacked_on = 'base'

    def default(self):
        pass

    @controller.expose(help='Install Bluetooth connection daemon')
    def install(self):

        print("Install Bluetooth Reconn Daemon")

