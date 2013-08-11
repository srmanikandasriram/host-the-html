import os
import time
dir_name = "/home/action/workspace/export2pdf/media/"
file_list = os.listdir(dir_name)
for f in file_list:
  stat = os.stat(dir_name+f)
  if time.time() - stat.st_ctime > 300:
    os.remove(dir_name+f)
