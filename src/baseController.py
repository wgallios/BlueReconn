from cement.core import controller


class baseController(controller.CementBaseController):
    class Meta:
        interface = controller.IController
        label = 'base'
        description = 'Bluetooth Reconnection'

        config_defaults = {}
        arguments = [
            (['-r', '--remove'], dict(action='store_true', help='Remove bluetooth device')),
            (['-b', '--bin'], dict(action='store_true', help='path to bin folder (Example: /usr/local/bin)'))
            ]

    @controller.expose(hide=True, aliases=['run'])
    def default(self):
        print("Try 'bluereconn --help' for more information")
