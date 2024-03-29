from __future__ import print_function, absolute_import, division
import json
import numpy as np
import os
from PIL import Image, ImageDraw
from collections import namedtuple

data_folder = 'semantic_segmentation_images_annotations/Images_and_Supervisely_Annotations/'
folder = 'json'
folder_masks_anatomy_inst = 'mask_instruments'

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




case_list = os.listdir(data_folder)

for p in range(len(case_list)):

    case_folder = data_folder + '/' + case_list[p]
    case_json_folder = data_folder + '/' + case_list[p]+ '/' + 'ann'
    jlist = os.listdir(case_json_folder)
    print(jlist)
    print(len(jlist))



    try:
        os.mkdir(case_folder + '/' + folder_masks_anatomy_inst)
    except:
        print("Re-writing in the existing folder")
             
    
    


    for i in range(len(jlist)):
        with open(case_json_folder + '/' + jlist[i], "r") as read_file:
            data = json.load(read_file)
            # print(data)
        name = jlist[i][:-5]    
        objects = data['objects']    
        image_Mix =  Image.new(mode = "RGB", size = (1024,768), color = 0)

        draw1 = ImageDraw.Draw(image_Mix)
                 

        # Forth: Instruments
        for j in range(len(objects)):
            title = objects[j]['classTitle']
            exterior = objects[j]['points']['exterior']
            ext = []
            for k in range(len(exterior)):
                ext.append(tuple(exterior[k]))
                
            if title in instrument_names:
                print(title)
                draw1.polygon(ext,fill=(255, 255, 255))             

        image_Mix.save(case_folder + '/' + folder_masks_anatomy_inst + '/'+name)

 

    
    
    
