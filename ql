#!/usr/bin/env python3
from parser import get_args
import yt_dlp
from downloader import downloadMP3, downloadMP4
import sys
import shutil
import sys

def check_ffmpeg():
    if shutil.which("ffmpeg") is None:
        print("❌ 'ffmpeg' is not installed or not found in your system PATH.")
        print("Please install it: https://ffmpeg.org/download.html")
        sys.exit(1)

def main():
    check_ffmpeg()

    args = get_args()
    qlversion = "v0.1.0"

    args = get_args()

    if args.version:
        print(f"QuickLoader (ql) {qlversion}")
        sys.exit(0)

    if not args.link and not any([args.search, args.preset, args.info]):
        parser.print_help()
        sys.exit(1)

    link = args.link
    path = args.output

    if args.format == "mp4":
        downloadMP4(f"{link}", f"{path}")
    elif args.format == "mp3":
        downloadMP3(f"{link}", f"{path}")


if __name__ == "__main__":
    main()
