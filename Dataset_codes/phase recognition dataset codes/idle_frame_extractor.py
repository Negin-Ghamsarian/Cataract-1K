

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

path = 'phase_recognition_annotations/'
video_path = 'dataset_videos/phase_recognition/'

case_list = os.listdir(path)
case_list.sort()


def csv_read_annot(csv_file):
    idle_inf = []
    with open(csv_file, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            final = row
            idle_inf.append([float(final[2]), float(final[3])])
    return idle_inf

def csv_read_fps(csv_file):
    with open(csv_file, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            final = row
    return float(final[4])   

def frame_to_secs(in_frame, fps) -> float:
	return int(in_frame) / fps


def secs_to_timedelta(sec_float: float) -> str:
	seconds = int(sec_float)
	microseconds = (sec_float * 1000000) % 1000000
	return timedelta(0, seconds, microseconds)    


def convert_frames_to_video(vid,frame_1_secs_str, duration_secs_str, idle_folder, name):

    cmd = f'ffmpeg -i {vid} -ss {frame_1_secs_str} -t {duration_secs_str} -c:v copy -c:a copy {idle_folder}/{name}'
    subprocess.check_output(cmd, shell =True)    

for i in range(0,len(case_list)-4):
    case_folder = path + case_list[i]
    video_inf_csv = case_folder + '/' + case_list[i] + '_video.csv'
    video_annot_csv = case_folder + '/' + case_list[i] + '_annotations.csv'
    video = video_path + case_list[i] + '/' + case_list[i] + '.mp4'

    idle_folder = case_folder + '/idle'

    try:
        shutil.rmtree(idle_folder)
    except:
        print("Does not exist")    

    os.makedirs(idle_folder, exist_ok = True)

    fps = csv_read_fps(video_inf_csv)
    annot = csv_read_annot(video_annot_csv)

    print(f'case: {case_list[i]}')
    print(f'fps: {fps}')
    print(f'annot: {annot}')

    for j in range(len(annot)-1):

        frame_start = annot[j][1]
        frame_stop = annot[j+1][0]

        if (frame_stop-frame_start)/fps >3:

            frame_1_secs = frame_to_secs(frame_start, fps)
            frame_2_secs = frame_to_secs(frame_stop, fps)
            duration_secs = frame_2_secs - frame_1_secs
            frame_1_secs_str = str(secs_to_timedelta(frame_1_secs))
            duration_secs_str = str(secs_to_timedelta(duration_secs))

            print(f'timedelta(first): {frame_1_secs_str}')
            print(f'timedelta(duration): {duration_secs_str}')

            name = case_list[i] + '_idle_' + frame_1_secs_str + '-' + str(secs_to_timedelta(frame_2_secs)) + '.mp4'

            convert_frames_to_video(video,frame_1_secs_str, duration_secs_str, idle_folder, name)

