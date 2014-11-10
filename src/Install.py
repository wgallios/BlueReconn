from cement.core import controller
# from pprint import pprint
# import logging
import shutil
import sys
import os


class Install(controller.CementBaseController):
    daemonLocal = '../daemon/BlueReconn'
    daemonFile = '/etc/init.d/BlueReconn'
    configPath = '/etc/BlueReconn'
    configFile = 'BlueReconn.conf'
    configLocal = '../daemon/BlueReconn.conf'

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
        self._checkCreateConfig()
        self._copyConfig()

    def _copyDaemon(self):
        print("Installing Bluetooth Reconn Daemon ..."),

        check = self._checkDaemon()

        if not check:
            # copies over daemon
            shutil.copyfile(self.daemonLocal, self.daemonFile)
            self._setDaemonPermissions()
            print('Done')
        else:
            print('Fail: keyboard service already exists')
            sys.exit(1)

        return True

    # checks to see if daemon file exists
    def _checkDaemon(self):
        if self.app.pargs.debug:
            print("Checking if 'keyboard' daemon already exists")

        if os.path.exists(self.daemonFile):
            return True
        else:
            return False

    # sets permissions of files
    def _setDaemonPermissions(self):
        if self.app.pargs.debug:
            print('Setting permissions for daemon file')

        os.chmod(self.daemonFile, 0o744)

    # checks for config folder in /etc/bluetooth
    def _checkCreateConfig(self):
        print("Checking if %s path exists ...")

        if os.path.exists(self.configPath):
            print("Path exists!")
            return True
        else:
            print("Path does not exist, will now create it")

            # creates directory
            os.makedirs(self.configPath)

            # sets permissions
            os.chmod(self.configPath, 0o744)

            print("Done")

            return True

    # copies over new config file
    def _copyConfig(self):
        print("Copying config file")
        shutil.copyfile(self.configLocal, self.configPath + '/' + self.configFile)

    # backs up existing config file in /etc/bluetooth
    def _backupConfig(self):
        if self.app.pargs.debug:
            print("Backing up config file %s/%s" % (self.configPath, self.configFile))

        shutil.move(self.configPath + '/' + self.configFile, self.configPath + '/' + self.configFile + '.bak')

        return True
