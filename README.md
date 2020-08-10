# screenlapse

## Getting started
Setup your AWS environment to allow programmatic S3 access on your machine.

Then:

`pip install -r requirements.txt`

`python aws_setup_init.py`


## Image capture

Usage: `screenlapse-capture.py [-t secs] [-o]`

Captures screenshots on your machine every `t` seconds. Uploads them to the preconfigured S3 bucket, or stores them in `img/` if running in offline mode.

Optional arguments:
  
  `-t secs, --time secs`  Number of seconds between screenshots. Default is 3
  
  `-o, --offline`         Use filesystem for image storage instead of S3

## Image download

Usage: `python screenlapse-download.py session_key`

Downloads images from the specified S3 location into `img/`. Exits if this folder already exists.

Positional arguments:

  `session_key`  The session key (ie. folder name in S3) to download images from


## Image conversion to video

Usage: `python screenlapse-convert.py`

Converts the images in `img/` into a 10fps mp4 video. Images are ordered by their last modified date.
