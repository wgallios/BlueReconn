from cement.core import controller
import Bluetooth
import pprint

class Config(controller.CementBaseController):
    # Bluetooth = Bluetooth.Bluetooth()
    class Meta:
        interface = controller.IController
        label = 'config'
        description = 'Configure BlueReconn Devices'
        # stacked_on = 'base'

    def default(self):
        pass

    @controller.expose(help='Scan, setup, and configure bluetooth devices')
    def config(self):
        print("Starting config process")
        # pprint.pprint(vars(Bluetooth))
        # self.Bluetooth.scan()
