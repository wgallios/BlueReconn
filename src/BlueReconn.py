from cement.core import foundation, handler

import sys
import os

import baseController
import Install
import Config
import Bluetooth

if os.getuid() == 0:
    try:
        app = foundation.CementApp('BlueReconn')

        handler.register(baseController.baseController)
        handler.register(Install.Install)
        handler.register(Config.Config)
        handler.register(Bluetooth.Bluetooth)

        app.setup()

        app.run()
    finally:
        app.close()
else:
    print("Permission denied, please run as sudo")
    sys.exit(0)
