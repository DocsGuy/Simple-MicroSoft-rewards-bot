from logging import error
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
        Id: 62naj2aga2n3fn3
        Time it took to make it: 3min
    """
)), 1))
#-------------------------------------------------------------------------------------------#
N = 4
String = ""
count = 0
def bot():
    for i in range(90):
        try:
            randomTitles = ["Simple Microsoft Search Bot made by SoloDev#7416","github.com/DocsGuy","discord.gg/h3sExDK6uQ"]
            os.system(f"title {random.choice(randomTitles)}")
            count =+ 1
            String = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
            os.system(f"start https://www.bing.com/search?q={String}")
            time.sleep(7)
            os.system('taskkill /f /im "msedge.exe"')
            print(Colorate.Vertical(Colors.blue_to_purple, (Center.XCenter(
            f"""
              _________      .__             .___           
             /   _____/ ____ |  |   ____   __| _/_______  __
             \_____  \ /  _ \|  |  /  _ \ / __ |/ __ \  \/ /
             /        (  <_> )  |_(  <_> ) /_/ \  ___/\   / 
            /_______  /\____/|____/\____/\____ |\___  >\_/  
                      \/                        \/    \/   
            Made by: SoloDev#7416
            Successfully searched: {String}
            """
            )), 1))
        except:
            print(Colorate.Vertical(Colors.blue_to_purple, (Center.XCenter(
            f"""
              _________      .__             .___           
             /   _____/ ____ |  |   ____   __| _/_______  __
             \_____  \ /  _ \|  |  /  _ \ / __ |/ __ \  \/ /
             /        (  <_> )  |_(  <_> ) /_/ \  ___/\   / 
            /_______  /\____/|____/\____/\____ |\___  >\_/  
                      \/                        \/    \/   
            Made by: SoloDev#7416
            Error: {error}
            """
        )), 1))
bot()
