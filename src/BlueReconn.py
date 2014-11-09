
from cement.core import backend, foundation, hook, handler
from cement.utils.misc import init_defaults

import baseController

try:
    app = foundation.CementApp('BlueReconn')

    handler.register(baseController.baseController)

    app.setup()

    app.run()
finally:
    app.close()
