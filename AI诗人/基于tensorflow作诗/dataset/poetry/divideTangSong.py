# coding: utf-8
# divide tang and song poem

import os
import re
import shutil

if not os.path.exists("./tang"):
    os.mkdir("tang")
if not os.path.exists("./song"):
    os.mkdir("song")

for file in os.listdir("."):
    if os.path.isfile(os.path.join("./", file)) and re.match('(.*)(\.)(json)', file) != None:
        shutil.copyfile(os.path.join("./", file), os.path.join("./", file.split(".")[1], file))
