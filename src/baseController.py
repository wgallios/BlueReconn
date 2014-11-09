from cement.core import backend, foundation, handler, hook, controller

class baseController(controller.CementBaseController):
    class Meta:
        interface = controller.IController
        label = 'base'
        description = 'Bluetooth Reconnection'

        config_defaults = {}
        arguments = []

    @controller.expose(hide=True, aliases=['run'])
    def default(self):
        print("default function")
