# Media Harvester

A simple Python script for swiftly downloading video and audio from YouTube and other online streaming sites. Wraps some conveniences around the [youtube-dl](https://rg3.github.io/youtube-dl).

**Use case:** 

Say you like listening to free lectures archived on YouTube while you're at your desktop and wanted to do that on the go. You could use Media Harvester to download a bunch of MP3's of those lectures, throw them in Dropbox, then use the Dropbox mobile app to listen on your mobile.

**Installation / usage instructions:**

First, install the ffmpeg library system-wide on your computer and make sure the `ffmpeg` command is available on the command line.

Download the repo, then cd into it and set up the virtual environment:

`virtualenv venv`
`virtualenv -p /usr/bin/python2.7 my_project`
`source venv/bin/activate`
`pip install -r requirements.txt`

Then, run:

`python harvester.py [url of page to harvest media from]`