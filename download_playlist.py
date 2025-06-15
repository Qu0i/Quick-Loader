import yt_dlp as yt
import os
import sys


def downloadPlaylist(URL: str, format, output):
    output = os.path.expanduser(output)

    with yt.YoutubeDL({}) as ydl:
        info = ydl.extract_info(URL, download=False)

    title = info.get("title")

    os.makedirs(title, exist_ok=True)

    if "entries" not in info:
        print("[ERROR]: Not a playlist!")
        sys.exit(1)

    outputTemplate = f"{output}/{title}/%(playlist_index)s. %(title)s.%(ext)s"

    if format == "mp4":
        options = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": outputTemplate,
            "quiet": False,
        }
    elif format == "mp3":
        options = {
            "format": "bestaudio/best",
            "outtmpl": outputTemplate,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "quiet": False,
        }
    else:
        print(f"[ERROR]: Unsupported format ({format})")
        sys.exit(1)

    with yt.YoutubeDL(options) as ydl:
        ydl.extract_info(URL, download=True)
