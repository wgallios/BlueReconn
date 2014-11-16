from cement.core import controller
from colorama import init, Fore, Back, Style
from config import Config

import bluetooth
# import pprint


class Bluetooth(controller.CementBaseController):
    nearby_devices = ''
    device = ''
    cfg = config('resrc/Msgs.cfg')

    class Meta:
        interface = controller.IController
        label = 'Bluetooth'
        description = 'Used to control bluetooth adapter for connections'
        stacked_on = 'base'

    @controller.expose(hide=False, help='Scans for bluetooth devices')
    def scan(self):
        print("Scanning for bluetooth devices ...")

        # scans for nearby bluetooth devices
        self.nearby_devices = bluetooth.discover_devices(lookup_names=True)

        print("Found %d devices" % len(self.nearby_devices))

        # lists each device for user to select to pair with
        for index, item in enumerate(self.nearby_devices):
            if index == 0:
                print("ID\tHardware Addr\tName")

            print("%d)\t%s\t%s" % (index + 1, item[0], item[1]))

        print("\n * Please enter the device ID you wish to pair with")

        # gets users selection (index + 1) of the device
        hid = input(Style.BRIGHT + "\nEnter device ID: " + Style.RESET_ALL)
        #subtracts 1 to be proper index num
        hid = int(hid) - 1

        # connects to device
        self.connect(hid);

    def connect(self, hid):
        hwd = self.nearby_devices[hid]
        port = 1

        print("Connecting Device: %s ... " % hwd[1])

        try:
            dsock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            dsock.connect((hwd[0],port))
            dsock.close()

            print("Socket now closed")

        except bluetooth.BluetoothError as be:
            print(Fore.RED + Style.BRIGHT + 'Bluetooth Error: %s' % str(be))
        except Exception as e:
            print(Fore.RED + Style.BRIGHT + 'Error: %s' % str(e))



