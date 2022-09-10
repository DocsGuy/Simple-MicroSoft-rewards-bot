import os
import string
import random
import time
from pystyle import Colorate, Colors, Write, Center
#-------------------------------------------------------------------------------------------#
print(Colorate.Vertical(Colors.blue_to_purple, (Center.XCenter(
    """
          _________      .__             .___           
         /   _____/ ____ |  |   ____   __| _/_______  __
         \_____  \ /  _ \|  |  /  _ \ / __ |/ __ \  \/ /
         /        (  <_> )  |_(  <_> ) /_/ \  ___/\   / 
        /_______  /\____/|____/\____/\____ |\___  >\_/  
                  \/                        \/    \/   
        Made by: SoloDev#7416
        Id: 62naj252ngfn2
        Time it took to make it: 1min
    """
)), 1))
#-------------------------------------------------------------------------------------------#
N = 4
String = ""
def bot():
    for i in range(90):
        String = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
        os.system(f"start https://www.bing.com/search?q={String}")
        time.sleep(0.4)
        os.system("echo Hi")
bot()
