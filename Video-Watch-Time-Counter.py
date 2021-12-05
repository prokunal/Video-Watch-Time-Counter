#!/usr/bin/env python3
# Author: Kunal Kumar
# website: procoder.in
# twitter: @l1v1n9h311

import os
import mimetypes
from pymediainfo import MediaInfo

mimetypes.init()
# for current folder name type '.' and for other type with path
folder_name = input("Enter folder name: ")

if len(folder_name) == 0:
    print("Enter folder name!")
    exit(0)


os.chdir(folder_name)
files = os.listdir(".")


v_files = []
for i in files:
    if os.path.isfile(i):
        temp_filename, ext = os.path.splitext(i)
        if len(ext) == 0:
            pass
        elif mimetypes.types_map[ext].find('video') == 0:
            v_files.append(i)
        else:
            pass



_sum = 0
total = 0
for filename in v_files:
    media_info = MediaInfo.parse(filename)
    for track in media_info.tracks:
        if track.track_type == 'Video':
            print("filename = %s"%filename.split("/")[-1])
            print("{} duration              {}s".format(track.track_type,track.to_data()["duration"]/1000.0))
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\n\n")
            time = track.to_data()["duration"]/1000.0
            _sum = time + _sum 
            total = total +1

print("Total files: %s"%total)
print("Total duration of all videos is: %.2f seconds, %s minutes and %.2f hours."%(_sum, int(_sum/60),float(_sum/60/60)))
