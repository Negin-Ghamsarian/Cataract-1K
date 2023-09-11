from __future__ import print_function, absolute_import, division
import json
import numpy as np
# import matplotlib
import os
from PIL import Image, ImageDraw
# from skimage.morphology import convex_hull_image
# import matplotlib.pyplot as plt
from collections import namedtuple

data_folder = '30videos_FinalRevision'
folder = 'json'
# folder_masks_mix = 'mask_mix'
# folder_masks_mix_train = 'mask_mix_train'
folder_masks_inst = 'mask_instruments_MultiClass'

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

instrument_names = ['slit knife', 'gauge', 'rhexis', 'spatula', 'phaco tip', 'IA', 'cartridge', 'incision knife', 'katena forceps', 'rhexis forceps']
final_instrument_names = ['slit/incision knife', 'gauge/cannula/spatula', 'gauge/cannula/spatula', 'gauge/cannula/spatula', 'phacoemulsifier tip', 'irrigation-aspiration', 'slit/incision knife', 'lens injector', 'forceps', 'forceps']
instrument_dictionary = {
    'slit knife': 1,
    'gauge': 2, 
    'rhexis': 2,
    'spatula': 2,
    'phaco tip': 3,
    'IA': 4,
    'cartridge': 5,
    'incision knife': 1,
    'katena forceps': 6,
    'rhexis forceps': 6
    

}



case_list = os.listdir(data_folder)

for p in range(len(case_list)):

    case_folder = data_folder + '/' + case_list[p]
    case_json_folder = data_folder + '/' + case_list[p]+ '/' + 'ann'
    jlist = os.listdir(case_json_folder)
    print(jlist)
    print(len(jlist))



    try:
        os.mkdir(case_folder + '/' + folder_masks_inst)
    except:
        print("Re-writing in the existing folder")
             
    
    


    for i in range(len(jlist)):
        with open(case_json_folder + '/' + jlist[i], "r") as read_file:
            data = json.load(read_file)
            # print(data)
        name = jlist[i][:-5]    
        objects = data['objects']    
        image_Mix =  Image.new(mode = "L", size = (1024,768), color = 0)

        draw1 = ImageDraw.Draw(image_Mix)
        
        
        for j in range(len(objects)):
            title = objects[j]['classTitle']
            exterior = objects[j]['points']['exterior']
            ext = []
            for k in range(len(exterior)):
                ext.append(tuple(exterior[k]))
                
            for k in range(len(instrument_names)):
                if title == instrument_names[k]:
                    draw1.polygon(ext,fill=instrument_dictionary(instrument_names[k]))

            

        image_Mix.save(case_folder + '/' + folder_masks_inst + '/'+name)


    # # To test mask creation:
    # for i in range(len(jlist)):
    #     with open(case_json_folder + '/' + jlist[i], "r") as read_file:
    #         data = json.load(read_file)
    #         # print(data)
    #     name = jlist[i][:-5]    
    #     objects = data['objects']    
    #     image_Mix =  Image.new(mode = "RGB", size = (1024,768), color = 0)

    #     draw1 = ImageDraw.Draw(image_Mix)

    #     # First: Cornea
    #     for j in range(len(objects)):
    #         title = objects[j]['classTitle']
    #         exterior = objects[j]['points']['exterior']
    #         ext = []
    #         for k in range(len(exterior)):
    #             ext.append(tuple(exterior[k]))
                
    #         if title == 'cornea':
    #             draw1.polygon(ext,fill=(255,160,122))
        
    #     # Second: Pupil
    #     for j in range(len(objects)):
    #         title = objects[j]['classTitle']
    #         exterior = objects[j]['points']['exterior']
    #         ext = []
    #         for k in range(len(exterior)):
    #             ext.append(tuple(exterior[k]))
                
    #         if title == 'pupil':
    #             draw1.polygon(ext,fill=(0,154,205))    

    #     # Third: Lens
    #     for j in range(len(objects)):
    #         title = objects[j]['classTitle']
    #         exterior = objects[j]['points']['exterior']
    #         ext = []
    #         for k in range(len(exterior)):
    #             ext.append(tuple(exterior[k]))
                
    #         if title == 'lense':
    #             draw1.polygon(ext,fill=(255,215,  0))  
        
    #     # Forth: Instruments
    #     for j in range(len(objects)):
    #         title = objects[j]['classTitle']
    #         exterior = objects[j]['points']['exterior']
    #         ext = []
    #         for k in range(len(exterior)):
    #             ext.append(tuple(exterior[k]))
                
    #         if title in instrument_names:
    #             print(title)
    #             draw1.polygon(ext,fill=(104,34,139)) 

    #     image_Mix.save(case_folder + '/' +folder_masks_mix_train+'/'+name)    

 

    
    
    
