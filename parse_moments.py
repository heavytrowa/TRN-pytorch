import os
import threading
import os
import shutil
import random

categories_file = 'pretrain/moments_categories.txt'
categories = [line.rstrip() for line in open(categories_file, 'r').readlines()]

data_folder = "data/Moments_in_Time_256x256_30fps/validation/"

train_dir = "data/frame_train"
valid_dir = "data/frame_validation"

files_output = ['val_videofolder.txt','train_videofolder.txt']
lists_output = [[],[]]

os.mkdir(train_dir)
os.mkdir(valid_dir)

split = 0.2

for label in os.listdir(data_folder):
    print(label)
    t_dir = os.path.join(train_dir,label)
    os.mkdir(t_dir)
    v_dir = os.path.join(valid_dir,label)
    os.mkdir(v_dir)

    directory = os.path.join(data_folder,label)
    videos = os.listdir(directory)

    curIDX = categories.index(label)

    tmpl='%06d.jpg'

    if label != "crawling":
        videos = random.sample(videos,5)

    for i, video_file in enumerate(videos):
        if i < split*len(videos):
            # shutil.copyfile(os.path.join(directory,video_file), os.path.join(v_dir,video_file))
            FRAME_ROOT = v_dir
            VIDEO_ROOT = directory
            curFolder = os.path.join(FRAME_ROOT, video_file)
            os.makedirs(curFolder)
            os.system(f'ffmpeg -i {VIDEO_ROOT}/{video_file} -vf scale=256:256 '
                      f'{FRAME_ROOT}/{video_file}/{tmpl}')

            dir_files = os.listdir(curFolder)
            lists_output[0].append('%s %d %d'%(curFolder, len(dir_files), curIDX))

        else:
            # shutil.copyfile(os.path.join(directory,video_file), os.path.join(t_dir,video_file))
            FRAME_ROOT = t_dir
            VIDEO_ROOT = directory
            curFolder = os.path.join(FRAME_ROOT, video_file)
            os.makedirs(curFolder)
            os.system(f'ffmpeg -i {VIDEO_ROOT}/{video_file} -vf scale=256:256 '
                      f'{FRAME_ROOT}/{video_file}/{tmpl}')
            dir_files = os.listdir(curFolder)
            lists_output[1].append('%s %d %d'%(curFolder, len(dir_files), curIDX))
    shutil.rmtree(directory, ignore_errors = True)
with open(files_output[0],'w') as f:
        f.write('\n'.join(lists_output[0]))
with open(files_output[1],'w') as f:
        f.write('\n'.join(lists_output[1]))



