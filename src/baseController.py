from cement.core import controller
from colorama import init, Fore, Back, Style

class baseController(controller.CementBaseController):
    class Meta:
        interface = controller.IController
        label = 'base'
        description = 'Bluetooth Reconnection'

        config_defaults = {}
        arguments = [
            (['-r', '--remove'], dict(action='store_true', help='Remove bluetooth device')),
            (['-b', '--bin'], dict(action='store', help='path to bin folder (Example: /usr/local/bin)'))
            ]

    @controller.expose(hide=True, aliases=['run'])
    def default(self):
        print(Style.BRIGHT + "Try 'bluereconn --help' for more information" + Style.RESET_ALL)
