from __future__ import print_function, absolute_import, division
import json
import numpy as np
# import matplotlib
import os
from PIL import Image, ImageDraw
from collections import namedtuple
import cv2
import glob

data_folder = '30videos_FinalRevision'
folder = 'json'
# folder_masks_mix = 'mask_mix'
folder_masks_mix_train = 'mask_mix_train'
folder_masks_anatomy_inst = 'mask_anatomy_inst'
folder_overlay = 'mask_overlay'

case_list = os.listdir(data_folder)



Label = namedtuple( 'Label' , [

    'name'        , # The identifier of this label, e.g. 'car', 'person', ... .
                    # We use them to uniquely name a class

    'id'          , # An integer ID that is associated with this label.
                    # The IDs are used to represent the label in ground truth images
                    # An ID of -1 means that this label does not have an ID and thus
                    # is ignored when creating ground truth images (e.g. license plate).
                    # Do not modify these IDs, since exactly these IDs are expected by the
                    # evaluation server.

    'color'       , # The color of this label
    'train_id'
    ] )


instrument_names = ['Slit Knife', 'Gauge', 'Capsulorhexis Cystotome', 'Spatula', 'Phacoemulsification Tip', 'Irrigation-Aspiration', 'Lens Injector', 'Incision Knife', 'Katena Forceps', 'Capsulorhexis Forceps']

labels = [
    #       name                     id       color
    Label(  'background'                         ,  0  , (  0,  0,  0), 0 ),
    Label(  'Cornea'                             ,  1  , (1,1,1), 1 ),
    Label(  'Pupil'                              ,  2  , (2  ,2,2), 2 ),
    Label(  'Lens'                              ,  3  , (3,3,  3), 3 ),
    Label(  'instrument_names'                   ,  4  , (4, 4,4), 4 )    
]


color_dict = {
   'Cornea':  '#AF3235',
   'Pupil': '#DFE674',
   'Lens': '#AF72B0',
   'Slit Knife': '#46C5DD',
   'Gauge': '#F282B4',
   'Capsulorhexis Cystotome': '#98CC70',
   'Spatula': '#671800',
   'Phacoemulsification Tip': '#009B55',
   'Irrigation-Aspiration': '#F7921D',
   'Lens Injector': '#613F99',
   'Incision Knife': '#46C5DD',
   'Katena Forceps': '#EE2967',
   'Capsulorhexis Forceps': '#0071BC'


}

color_dict1 = {
   'Iris':  'Maroon',
   'Pupil': 'GreenYellow',
   'Lens': 'Orchid',
   'Slit/Incision Knife': 'SkyBlue',
   'Gauge': 'CarnationPink',
   'Spatula': 'Sepia',
   'Capsulorhexis Cystotome': 'YellowGreen',
   'Phacoemulsifier Tip': 'ForestGreen',
   'Irrigation-Aspiration': 'BurntOrange',
   'Lens Injector ': 'RoyalPurple',
   'Capsulorhexis Forceps': 'RoyalBlue',
   'Katena Forceps': 'WildStrawberry'



}


case_list = os.listdir(data_folder)

total_width = 1024*2
max_height = 768

new_im = Image.new('RGB', (total_width, max_height))

for p in range(len(case_list)):

    case_folder = data_folder + '/' + case_list[p]
    case_json_folder = data_folder + '/' + case_list[p]+ '/' + 'ann'
    jlist = os.listdir(case_json_folder)
    print(jlist)
    print(len(jlist))

    try:
        os.mkdir(case_folder + '/' + folder_masks_mix_train)
    except:
        print("Re-writing in the existing folder")
             
    

    # To test mask creation:
    for i in range(len(jlist)):
        with open(case_json_folder + '/' + jlist[i], "r") as read_file:
            data = json.load(read_file)
            # print(data)
        name = jlist[i][:-5]    
        objects = data['objects']    
        image_Mix =  Image.new(mode = "RGB", size = (1024,768), color = 0)

        draw1 = ImageDraw.Draw(image_Mix)

        # First: Cornea
        for j in range(len(objects)):
            title = objects[j]['classTitle']
            exterior = objects[j]['points']['exterior']
            ext = []
            for k in range(len(exterior)):
                ext.append(tuple(exterior[k]))
                
            if title == 'Cornea':
                draw1.polygon(ext,fill=color_dict['Cornea'])
        
        # Second: Pupil
        for j in range(len(objects)):
            title = objects[j]['classTitle']
            exterior = objects[j]['points']['exterior']
            ext = []
            for k in range(len(exterior)):
                ext.append(tuple(exterior[k]))
                
            if title == 'Pupil':
                draw1.polygon(ext,fill=color_dict['Pupil'])    

        # Third: Lens
        for j in range(len(objects)):
            title = objects[j]['classTitle']
            exterior = objects[j]['points']['exterior']
            ext = []
            for k in range(len(exterior)):
                ext.append(tuple(exterior[k]))
                
            if title == 'Lens':
                draw1.polygon(ext,fill=color_dict['Lens'])  
        
        # Forth: Instruments
        for j in range(len(objects)):
            title = objects[j]['classTitle']
            exterior = objects[j]['points']['exterior']
            ext = []
            for k in range(len(exterior)):
                ext.append(tuple(exterior[k]))
                
            if title in instrument_names:
                print(title)
                draw1.polygon(ext,fill=color_dict[title]) 

        image_Mix.save(case_folder + '/' +folder_masks_mix_train+'/'+name)    

 

    


    try:
        os.mkdir(case_folder + '/' + folder_overlay)
    except:
        print("Re-writing in the existing folder")

    img_list = os.listdir(case_folder + '/img/') 
    # mask_list = os.listdir(case_folder + '/mask_mix_train/')   

    for i in range(len(img_list)):
             
        image = cv2.imread(case_folder + '/img/' + img_list[i])
        mask = cv2.imread(case_folder + '/mask_mix_train/'+ img_list[i])
        mask1 = mask.copy()
        mask1[(mask==255).all(-1)] = [0,255,125]
        # print(np.shape(mask1))
        # print(np.unique(mask))

        alpha = 0.45

        output = image.copy()
        out_name = img_list[i][:-4]+'overlayed.png'
        cv2.addWeighted(image, alpha, mask1, 1 - alpha,
                0, output)

        # cv2.imwrite(case_folder + '/' + folder_overlay+ '/' +out_name, output)     

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_pil = Image.fromarray(image)  

        output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
        output_pil = Image.fromarray(output)   

        new_im = Image.new('RGB', (total_width, max_height))
        x_offset = 0
        new_im.paste(image_pil, (x_offset,0))
        x_offset += image_pil.size[0]    
        new_im.paste(output_pil, (x_offset,0))  

        new_im.save(case_folder + '/' + folder_overlay+ '/' +out_name)  
        
dict_keys1 = list(color_dict1.keys())
print(dict_keys1)
str1 = ''
for i in range(len(dict_keys1)):
    str1 = str1 + dict_keys1[i] + ': \DP{0.9}{' + color_dict1[dict_keys1[i]] + '}, '
print(str1)    