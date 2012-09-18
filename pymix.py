#!/usr/bin/python
#import
import os
import random

#config
root_dir = "/home/fred/Downloads/Bird sounds/"
intermittent_dir = "intermittent"
constant_dir = "constant"
weather_dir = "loop"
volume_flag = "-volume"
quiet_flag = "-quiet"
max_constant_vol = 80
min_constant_vol = 50
max_intermittent_vol = 100
min_intermittent_vol = 50
max_weather_vol = 100
min_weather_vol = 50
player = "/usr/bin/mplayer"

#get list of files
intermittent_files = os.listdir(root_dir + '/' + intermittent_dir)
constant_files = os.listdir(root_dir + '/' + constant_dir)
weather_files = os.listdir(root_dir + '/' + weather_dir)

#start constant background
filename = root_dir + '/' + constant_dir + '/' + constant_files[
        int(random.random() * len(constant_files))]
volume = random.random() * (max_constant_vol
        - min_constant_vol) + min_constant_vol
os.popen()

#loop
while (True):
    #start intermittent weather sound
    volume = random.random() * (max_weather_vol
            - min_weather_vol) + min_weather_vol
    os.popen()

    #start intermittent sound
    volume = random.random() * (max_intermittent_vol
            - min_intermittent_vol) + min_intermittent_vol
    os.popen()
