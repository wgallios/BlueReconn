from cement.core import controller
from pprint import pprint
import logging
import shutil
import sys
import os

class Install(controller.CementBaseController):
    daemonLocal = '../daemon/keyboard'
    daemonFile = '/etc/init.d/keyboard'


    class Meta:
        interface = controller.IController
        label = 'installer'
        description = 'Installer for bluetooth daemon'
        stacked_on = 'base'

    def default(self):
        pass

    @controller.expose(help='Install Bluetooth connection daemon')
    def install(self):
        self._copyDaemon()

    def _copyDaemon(self):
        print("Installing Bluetooth Reconn Daemon ...")
        
        check = self._checkDaemon()
        
        if not check:
            # copies over daemon
            shutil.copyfile(self.daemonLocal, self.daemonFile)
            print('Done')
        else:
            sys.exit(1);

        return True;

    # checks to see if daemon file exists
    def _checkDaemon(self):
        if self.app.pargs.debug:
            print("Checking if 'keyboard' daemon already exists")

        if os.path.exists(self.daemonFile):
            return True
        else:
            return False



