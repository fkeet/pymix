#!/usr/bin/python
#import
import time
import subprocess
import os
import random

#config
root_dir = "/home/fred/Downloads/Bird sounds/"
intermittent_dir = "intermittent"
constant_dir = "constant"
weather_dir = "loop"
volume_flag = "-volume"
quiet_flag = "-quiet"
max_constant_vol = 60
min_constant_vol = 40
max_intermittent_vol = 100
min_intermittent_vol = 50
max_weather_vol = 80
min_weather_vol = 30
player = "/usr/bin/mplayer"
time_scale = 10
chance_of_constant = 1
chance_of_weather = 0.1
chance_of_intermittent = 0.8

random.seed()

#get list of files
intermittent_files = os.listdir(root_dir + '/' + intermittent_dir)
constant_files = os.listdir(root_dir + '/' + constant_dir)
weather_files = os.listdir(root_dir + '/' + weather_dir)

#start constant background
if random.random() < chance_of_constant:
    filename = root_dir + '/' + constant_dir + '/' + constant_files[
            int(random.random() * len(constant_files))]
    volume = int(random.random() * (max_constant_vol
            - min_constant_vol) + min_constant_vol)
    print player, quiet_flag, volume_flag, str(volume), filename
    subprocess.Popen([player, quiet_flag, volume_flag, str(volume), filename])

#loop
while (True):
    #start intermittent weather sound
    if random.random() < chance_of_weather:
        filename = root_dir + '/' + weather_dir + '/' + weather_files[
                int(random.random() * len(weather_files))]
        volume = int(random.random() * (max_weather_vol
                - min_weather_vol) + min_weather_vol)
        subprocess.Popen(
                [player, quiet_flag, volume_flag, str(volume), filename])

    #start intermittent sound
    if random.random() < chance_of_intermittent:
        filename = root_dir + '/' + intermittent_dir + '/' + \
                intermittent_files[int(random.random() *
                    len(intermittent_files))]
        volume = int(random.random() * (max_intermittent_vol
                - min_intermittent_vol) + min_intermittent_vol)
        subprocess.Popen(
                [player, quiet_flag, volume_flag, str(volume), filename])

    time.sleep(time_scale * random.random())
