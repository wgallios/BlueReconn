from cement.core import controller


class baseController(controller.CementBaseController):
    class Meta:
        interface = controller.IController
        label = 'base'
        description = 'Bluetooth Reconnection'

        config_defaults = {}
        arguments = [
            (['-r', '--remove'], dict(action='store_true', help='Remove bluetooth device'))
            ]

    @controller.expose(hide=True, aliases=['run'])
    def default(self):
        print("BlueReconn"),
