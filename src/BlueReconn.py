
from cement.core import backend, foundation, hook, handler
from cement.utils.misc import init_defaults

import sys
import os
import baseController, Install

if os.getuid() == 0:
    try:
        app = foundation.CementApp('BlueReconn')

        handler.register(baseController.baseController)
        handler.register(Install.Install)

        app.setup()

        app.run()
    finally:
        app.close()
else:
    print("Permission denied, please run as sudo")
    sys.exit(0)
