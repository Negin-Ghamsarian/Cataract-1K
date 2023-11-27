
import os
import subprocess
import math
import shutil
import numpy as np
from os.path import isfile, join
from PIL import Image
import random
import csv
from datetime import datetime, timedelta

path1 = 'phase_recognition_annotations/'


case_list = os.listdir(path1)
case_list.sort()



for i in range(0,len(case_list)-4):
    case_folder = path1 + case_list[i]
    subfolders = [ f.path for f in os.scandir(case_folder) if f.is_dir() ]

    for j in range(len(subfolders)):
        phase_folder = subfolders[j]

        vid_list = os.listdir(phase_folder)
        print(f'vid_list: {vid_list}')



        for k in range(len(vid_list)):

            vid_path = phase_folder + '/' + vid_list[k]
            vid_path_out = vid_path[:-4] + '30fps.mp4'

            cmd = f'ffmpeg -i {vid_path} -filter:v fps=30 {vid_path_out}'
            subprocess.check_output(cmd, shell =True)    



