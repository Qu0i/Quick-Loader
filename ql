#!/usr/bin/env python3
from parser import get_args
import yt_dlp
from downloader import downloadMP3, downloadMP4
import sys


def main():
    args = get_args()
    qlversion = "v0.01"

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
