# Media Harvester

A simple Python script for swiftly downloading video and audio from YouTube and other online streaming sites. Wraps some conveniences around [youtube-dl](https://github.com/rg3/youtube-dl) and adds an audio ripper via [ffmpeg](https://www.ffmpeg.org).

**Use case:** 

Say you like listening to free lectures archived on YouTube while you're at your desktop and wanted to do that on the go. You could use Media Harvester to download a bunch of MP3's of those lectures, throw them in Dropbox, then use the Dropbox mobile app to listen on your mobile.

**Installation / usage instructions:**

First, install the ffmpeg suite of tools system-wide on your computer and make sure the `ffmpeg` command is available on the command line.

Download the repo, then cd into it and set up the virtual environment with Python 2.7:

`virtualenv venv`

`virtualenv -p /usr/bin/python2.7 venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

Then, run:

`python harvester.py [url of page to harvest media from]`

**Note:** Only tested on Mac command line; should work similarly in Ubuntu or other *nix system.