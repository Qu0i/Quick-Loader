#!/usr/bin/env python3
import yt_dlp
import sys
import shutil
import sys

from downloader import downloadMP3, downloadMP4
from parser import get_args
from download_playlist import downloadPlaylist


def check_ffmpeg():
    if shutil.which("ffmpeg") is None:
        print("[ERROR] 'ffmpeg' is not installed or not found in your system PATH.")
        print("Please install it: https://ffmpeg.org/download.html")
        sys.exit(1)


def main():
    check_ffmpeg()

    args = get_args()
    qlversion = "v0.2.0"

    if args.version:
        print(f"Quick-Loader (ql) {qlversion}")
        sys.exit(0)

    if not args.link and not any([args.search, args.preset, args.info]):
        print(f"Quick-Loader (ql) {qlversion}")
        print("[ERROR]: No link or action specified.")
        sys.exit(1)

    link = args.link
    path = args.output
    fmt = args.format
    
    if args.playlist:
        downloadPlaylist(link, fmt, path)
    elif fmt == "mp4":
        downloadMP4(link, path)
    elif fmt == "mp3":
        downloadMP3(link, path)
    else:
        print(f"[ERROR]: Unknown format '{fmt}'")
        sys.exit(1)


if __name__ == "__main__":
    main()
