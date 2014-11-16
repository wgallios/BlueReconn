
from __future__ import print_function
from colorama import init, Fore, Back, Style
from config import Config

class Msg:

    def init(self):
        self.cfg = config('resrc/Msgs.cfg')

    def Error(n):
        std = self.cfg.CONFIG.Errors[n][0]
        txt = self.cfg.CONFIG.Errors[n][1]
        print(Fore.RED + Style.BRIGHT + '\n%s' + Style.RESET_ALL % , file=std)
