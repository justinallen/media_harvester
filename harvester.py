from __future__ import unicode_literals
from sys import argv
import os
import time
import youtube_dl
import subprocess
from slugify import slugify

script, url = argv

print "harvesting..."
print "from url:", url

options = {
    'format': 'mp4',
    'outtmpl': '%(title)s.%(ext)s'	
}

with youtube_dl.YoutubeDL(options) as ydl:
	# grab the video data
	info = ydl.extract_info(url, download=False)
	video_title = info.get('title', None)
	# slugify it for the directory name
	dir_name = slugify(video_title)
	# make directory
	print('creating ' + dir_name + ' directory')
	os.mkdir(dir_name)
	# go to that directory
	os.chdir(dir_name)	
	# print('my title is ' + info.get('title', None))
	ydl.download([url])

# create file for meta info
print('creating metadata file')
meta = open("about.txt", 'w')
# write meta info to that file
date = time.strftime('%m.%d.%Y')
meta.write('Harvested on ' + date + '\n')
meta.write('Title: ' + video_title + '\n')
meta.write('From: ' + url + '\n')
meta.close()

# now for the audio
print('now for the audio rip...')

# prep audio filename
filename = video_title + '.mp4'
audio_filename = video_title + '.mp3'

# create mp3 version
# subprocess is like issuing a unix command
# ffmpeg must be installed
# does ffmpeg -i filename audio_filename
subprocess.call(['ffmpeg', '-i', filename, audio_filename])



