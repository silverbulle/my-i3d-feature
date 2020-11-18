import os
import sys
# import re

video_path = '/home/silverbullet/Videos/MSR_Video_Description_Corpus/YouTubeClips'
save_path = '/home/silverbullet/Videos/MSR_Video_Description_Corpus/YouTubeClips-25fps'
count = 0

videos = os.listdir(video_path)
for video in videos:
    name = video.split('.')[0]
    count += 1
    frame_path = os.path.join(save_path, name)
    # print(frame_path)
    if not os.path.exists(frame_path):
        os.makedirs(frame_path)
    print("extractor {} : {}".format(count, name))
    os.system("ffmpeg -i " + os.path.join(video_path, video) + " -r 25 " + frame_path + "/%d.jpg")
    # cmd = 'ffmpeg -i $fi -r 25 /home/silverbullet/Videos/MSR_Video_Description_Corpus/YouTubeClips-25fps/%d.jpg'
    print("process success!!!")