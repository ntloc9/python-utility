from pathlib import Path
import subprocess
import json
import os
from datetime import datetime  
from datetime import timedelta  


def video_length_seconds(filename):
    result = subprocess.run(['ffprobe', filename, '-print_format', 'json', '-show_streams', '-loglevel', 'quiet'], capture_output=True, text=True)
    return float(json.loads(result.stdout)['streams'][0]['duration'])

# all mp4 files in the current directory in seconds
# print(str(datetime.timedelta(seconds=sum(video_length_seconds(f) for f in Path('/mnt/Docs/spring/14. Spring MVC - Form Tags and Data Binding').glob('*.mp4')))))

# for f in Path('/mnt/Docs/spring/spring/14. Spring MVC - Form Tags and Data Binding').glob('*.mp4'):
#   print('filename {} : {}'.format(f, video_length_seconds(f)))

# for f in Path('/mnt/Docs/spring/14. Spring MVC - Form Tags and Data Binding').glob('*.mp4'):
#     print('check')
# # all files in the current directory
# print(sum(video_length_seconds(f) for f in Path('/mnt/Code/doc code/reactjs/loc').iterdir() if f.is_file()))



#loop folder and count
    rootdir = '/mnt/Docs/spring'
    count = timedelta(seconds=0)  
    # print(count + timedelta(seconds=10))
    for subdir, dirs, files in os.walk(rootdir):
        count = count + timedelta(seconds=sum(video_length_seconds(f) for f in Path(subdir).glob('*.mp4')))

    print(count)
