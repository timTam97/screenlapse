# screenlapse

## Getting started

`pip install -r requirements.txt`

If you intend to use online image storage, setup your AWS environment to allow programmatic S3 access on your machine.

Then:

`python aws_setup_init.py`

This file creates a new bucket on S3 and saves the name of the newly created bucket.

## Image capture

Usage: `screenlapse-capture.py [-t secs] [-o] [-m]`

Captures screenshots on your machine every `t` seconds. Uploads them to the preconfigured S3 bucket, or stores them in `data/img/` if running in offline mode.

Optional arguments:
  
  `-t secs, --time secs`  Number of seconds between screenshots. Default is 3
  
  `-o, --offline`         Use filesystem for image storage instead of S3
  
  `-m, --multi`           Take multi-monitor screenshots
  
If you're uploading to S3, screenshots are organised into folders, with the folder name being the unix timestamp of when the current screenshot capture session first started. When downloading images (see next step), first find the folder on the S3 console, and then use this folder name as the `session_key` when you call `screenlapse-download.py`.

## Image download

Usage: `python screenlapse-download.py session_key`

Downloads images from the specified S3 location into `data/img/`. Exits if this folder already exists.

Positional arguments:

  `session_key`  The session key (ie. folder name in S3) to download images from


## Image conversion to video

Usage: `python screenlapse-convert.py`

Converts the images in `data/img/` into a 10fps mp4 video. Images are ordered by their last modified date.
