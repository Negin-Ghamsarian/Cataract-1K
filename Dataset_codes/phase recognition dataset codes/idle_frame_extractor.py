

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

path = '/storage/workspaces/artorg_aimi/ws_00000/Negin/Cat3K_Phases/cases/'

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
    # cmd = f'ffmpeg -r 10 -start_number {sn} -i {path}/{imageName1}%06d.png -q:v 0 -c:v copy -y {pathOut1}/{vidName}.avi'
    # cmd = f'ffmpeg -ss {frame_1_secs_str} -i {vid} -to {duration_secs_str} -c:v -b:v 1M -maxrate 1M {idle_folder}/{name}'
    cmd = f'ffmpeg -i {vid} -ss {frame_1_secs_str} -t {duration_secs_str} -c:v copy -c:a copy {idle_folder}/{name}'
#    cmd = f'ffmpeg -r 25 -i {path}/*.jpg {pathOut1}/{vidName}.avi'
    subprocess.check_output(cmd, shell =True)    

for i in range(0,len(case_list)-4):
    case_folder = path + case_list[i]
    video_inf_csv = case_folder + '/' + case_list[i] + '_video.csv'
    video_annot_csv = case_folder + '/' + case_list[i] + '_annotations.csv'
    video = case_folder + '/' + case_list[i] + '.mp4'

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









# list1 = os.listdir(path)
# list1.sort()
# print(list1)
# print(len(list1))



# fps = 10
# for j in range(155,len(list1)):
    
#     shutil.rmtree(pathMed1)
#     os.mkdir(pathMed1)
    
#     shutil.rmtree(pathMed2)
#     os.mkdir(pathMed2)

#     video = list1[j]
#     print(video)
#     imageName = str(video)[:-4]  
#     vidpath = pathOut + '/' + imageName
#     os.mkdir(vidpath)
#     imageName = imageName[:-4]
#     imageName1 = imageName+'_'
    
#     cmd = f'ffmpeg -i {path}/{video} -q:v 0 -r 10 {pathMed1}/{imageName1}%06d.png -hide_banner'
#     subprocess.check_output(cmd, shell =True)
    
#     imList = os.listdir(pathMed1)
#     imList.sort()
#     l = len(imList) 
      
#     for k in range (l):   
#         x = Image.open(pathMed1 + '/' + imList[k])
#         x = x.resize((512, 512))
#         x.save(pathMed1 + '/' + str(imList[k]))
       
# #    imageName = 'A' 
# #    cmd1 = f'python3 Bounding_box_eyeExtract_imSave.py splash --weights=MaskR_CNN__EyeClass_V4_5.h5 --image=Eye_callibration/med1'
# #    subprocess.check_output(cmd1, shell =True)   
# #    
            
#     c = (l - 50)//20 # 20 clips of 50 frames per video
#     if c<50:
#         print('inappropriate video length')
#         continue
#     for i in range(20):
#         shutil.rmtree(pathMed2)
#         os.mkdir(pathMed2)

#         start = random.randint(0,c-1)
#         for j in range(start+i*c,start+i*c+50):
#             str1 = str(imList[j])
#             shutil.copy(pathMed1 + '/' + imList[j], pathMed2 + '/' + str1)
            
            
        
#         vidName = imageName1+str(i)
#         sn = start+i*c
#         convert_frames_to_video(pathMed2, vidpath, imageName1, vidName, sn, fps)
            
        

        
# # test: imp:1, irr:5, phako:5, rhexis:2, allOther:4
# # train: imp:1, irr:5, phako:5, rhexis:3, allOther:3
        
        
        

