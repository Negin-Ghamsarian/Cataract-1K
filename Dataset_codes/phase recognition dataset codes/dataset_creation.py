

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

path1 = '/storage/workspaces/artorg_aimi/ws_00000/Negin/Cat3K_Phases/cases/'
path2 = '/storage/workspaces/artorg_aimi/ws_00000/Negin/Cat3K_Phases/Training_Dataset/'

case_list = os.listdir(path1)
case_list.sort()



for i in range(0,len(case_list)-4):
    case_folder = path1 + case_list[i]
    subfolders = [f.path for f in os.scandir(case_folder) if f.is_dir()]
    print(f'subfolders: {subfolders}')

    for j in range(len(subfolders)):

        files = os.listdir(subfolders[j])

        for k in range(len(files)):
            shutil.copy(subfolders[j] + '/' + files[k], path2 + subfolders[j].split(os.sep)[-1] + '/' + files[k])
