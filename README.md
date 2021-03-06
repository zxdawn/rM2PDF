# rM2PDF

rM2PDF script for the reMarkable reader

## Features

These scripts are based on Linux. You should run scripts on Linux or [Win10_ubuntu](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/). Feel free to adopt for mac or win.

1. Download files from the reMarkable paper tablet;
2. Combine notes and PDF together.
3. Set the color of stroke. (change line 67, eg. 0: "blue")

## Requirements

1. Python
2. [rsvg-convert](http://manpages.ubuntu.com/manpages/trusty/man1/rsvg-convert.1.html)
```
apt-get install librsvg2-bin
```

## Introduction

1. Download or clone this repository;
2. Change the name of directory between `#----------#` and `#----------#` in rMsync.sh and rM2PDF.py.
3. Run rMsync.sh and rM2PDF.py successively.

## Improvements Needed

* Avoid duplicates in original_pdf folder (You can check [rm-sync](https://github.com/simonschllng/rm-sync) for updates);
* Better combination between Python and Bash Shell.

## Tools used

* [rm-sync](https://github.com/simonschllng/rm-sync)
* [rM2svg](https://github.com/reHackable/maxio/tree/master/tools)
* [cpdf](https://github.com/coherentgraphics/cpdf-binaries)

## Screenshot

![Screenshot](https://github.com/zxdawn/rM2PDF/blob/master/Screenshot.png)

## Support

Raise an issue in this github repository, or email xinzhang1215@gmail.com
