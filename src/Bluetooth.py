from cement.core import controller
import bluetooth
import pprint

class Bluetooth(controller.CementBaseController):
    class Meta:
        interface = controller.IController
        label = 'Bluetooth'
        description = 'Used to control bluetooth adapter for connections'
        stacked_on = 'base'

    @controller.expose(hide=False, help='Scans for bluetooth devices')
    def scan(self):
        print("Scanning for bluetooth devices ...")

        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        # pprint.pprint(nearby_devices)

        print("Found %d devices" % len(nearby_devices))

        print("Please enter the device number you wish to pair")

        cnt = 1

        for addr, name in nearby_devices:
            print("%d) %s -%s" % (cnt, addr, name))
            cnt = cnt + 1

        hid = input("Please enter device Hardware ID: ")
