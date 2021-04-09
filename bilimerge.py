import os
import subprocess
import sys


def merge_video(file, name):
    os.chdir(file)
    subprocess.call(['ffmpeg', '-i', 'video.m4s', '-i', 'audio.m4s', '-codec', 'copy',
                     sys.argv[1] + name + '.mp4'], 1000)
    return


def traversal(dir):
    fs = os.listdir(dir)
    for f in fs:
        print(f)
        file = dir + "/" + f
        if os.path.isdir(file):
            traversal(file)
        elif f == 'index.json':
            up_file_path = os.path.abspath(os.path.join(file, "../.."))
            merge_video(dir, os.path.basename(up_file_path))


if __name__ == '__main__':
    if len(sys.argv) < 2:
      print('usage: python bilimerge.py [source] [target]')
    else:
      traversal(sys.argv[0])
