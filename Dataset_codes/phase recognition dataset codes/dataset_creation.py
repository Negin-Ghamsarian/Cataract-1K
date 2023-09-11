

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
path2 = 'Training_Dataset/'

case_list = os.listdir(path1)
case_list.sort()



for i in range(0,len(case_list)):
    case_folder = path1 + case_list[i]
    subfolders = [f.path for f in os.scandir(case_folder) if f.is_dir()]
    print(f'subfolders: {subfolders}')

    for j in range(len(subfolders)):

        files = os.listdir(subfolders[j])

        for k in range(len(files)):
            os.makedirs(path2 + subfolders[j].split(os.sep)[-1], exist_ok = True)
            shutil.copy(subfolders[j] + '/' + files[k], path2 + subfolders[j].split(os.sep)[-1] + '/' + files[k])
