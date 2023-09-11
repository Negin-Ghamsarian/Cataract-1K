import os
import csv
import glob
import random
import pandas as pd

def ID_shuffler(list1, list2):

        temp = list(zip(list1, list2))
        random.shuffle(temp)
        res1, res2 = zip(*temp)
        # res1 and res2 come out as tuples, and so must be converted to lists.
        res1, res2 = list(res1), list(res2)

        return res1, res2

def csv_saver(save_path, a, b, c, d, i, name='instrument_MultiClass'):


        dict = {"imgs": a , "masks": b }
        df = pd.DataFrame(dict)
        df.to_csv(save_path + name + '_' + str(i)+ '_train' +'.csv')  

        dict = {"imgs": c , "masks": d}
        df = pd.DataFrame(dict)
        df.to_csv(save_path + name + '_' + str(i)+ '_test' + '.csv')     


save_path = '/storage/homefs/ng22l920/Codes/DeepPyramid_IJCARS/TrainIDs_Dataset_paper_instrument_MultiClass/'
Cat30_dir = '/storage/workspaces/artorg_aimi/ws_00000/Negin/Dataset_paper/Cat3K_30Vids_Segmentation/30videos_FinalRevision/'

image_dir = 'img/'
mask_dir = 'mask_instruments_MultiClass/'

cases = os.listdir(Cat30_dir)
folds = []
for i in range(5):

    fold = cases[i*6 : (i+1)*6]
    folds.append(fold)


for i in range(len(folds)):

    locals()['imgs_Cat3K_test_fold_' + str(i)] = []
    locals()['masks_Cat3K_test_fold_' + str(i)] = []

    locals()['imgs_Cat3K_train_fold_' + str(i)] = []
    locals()['masks_Cat3K_train_fold_' + str(i)] = []

    
    fold_train_Cat3K = cases.copy()


    for k in range(len(folds[i])):
        print(f'fold_test_Cat3K: {fold_train_Cat3K}')
        print(f'folds_Cat3K[i]: {folds[i]}')  
        fold_train_Cat3K.remove(folds[i][k])  


    
    for j in range(len(folds[i])):  
        print(Cat30_dir + str(folds[i][j]) + image_dir + '/' + '*.png')  
        for f in glob.glob(Cat30_dir + str(folds[i][j]) + '/' +image_dir +  '*.png'):
            locals()['imgs_Cat3K_test_fold_' + str(i)].append(f)    

        for f in glob.glob(Cat30_dir + str(folds[i][j]) + '/' + mask_dir + '*.png'):
            locals()['masks_Cat3K_test_fold_' + str(i)].append(f)     

        locals()['imgs_Cat3K_test_fold_' + str(i)].sort()  
        locals()['masks_Cat3K_test_fold_' + str(i)].sort()

    print(locals()['imgs_Cat3K_test_fold_' + str(i)])    

    # locals()['imgs_Cat3K_train_fold_' + str(i)], locals()['masks_Cat3K_train_fold_'  + str(i)] \
    #     = ID_shuffler(locals()['imgs_Cat3K_train_fold_' + str(i)], locals()['masks_Cat3K_train_fold_'  + str(i)])


    for j in range(len(fold_train_Cat3K)):    
        for f in glob.glob(Cat30_dir + str(fold_train_Cat3K[j]) + '/' +image_dir +  '*.png'):
            locals()['imgs_Cat3K_train_fold_' + str(i)].append(f)    

        for f in glob.glob(Cat30_dir + str(fold_train_Cat3K[j]) +'/' + mask_dir +  '*.png'):
            locals()['masks_Cat3K_train_fold_' + str(i)].append(f)     

        locals()['imgs_Cat3K_train_fold_' + str(i)].sort()  
        locals()['masks_Cat3K_train_fold_' + str(i)].sort()

    # locals()['imgs_Cat3K_test_fold_' + str(i)], locals()['masks_Cat3K_test_fold_'  + str(i)] \
    #     = ID_shuffler(locals()['imgs_Cat3K_test_fold_' + str(i)], locals()['masks_Cat3K_test_fold_'  + str(i)])
    


    csv_saver(save_path, locals()['imgs_Cat3K_train_fold_' + str(i)], locals()['masks_Cat3K_train_fold_' + str(i)],\
        locals()['imgs_Cat3K_test_fold_' + str(i)], locals()['masks_Cat3K_test_fold_' + str(i)], i)        
















