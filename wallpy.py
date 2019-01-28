"GHOST"


import os
import datetime

a=os.listdir('/home/ghost/Pictures/Wallpapers')
date=datetime.datetime.now()
b=int(date.day % 7)

wallp= a[b]

os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/ghost/Pictures/Wallpapers/"+wallp)
