import os
import string
import random
import time
#-------------------------------------------------------------------------------------------#
N = 4
String = ""
def randomString():
    for i in range(90):
        String = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
        os.system(f"start https://www.bing.com/search?q={String}")
        time.sleep(0.4)
        os.system("echo Hi")
randomString()
