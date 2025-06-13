from parser import get_args
import yt_dlp
import ffmpeg
import os

cwd = os.getcwd()
args = get_args()

def downloadMP4(URL, path=None):
    if path:
        output_template = f"{path}/%(title)s.%(ext)s"
    else:
        output_template = f"{cwd}/"

    # TODO: check for `/` at the end of the argument

    if args.video:
        options = {
            "format": "bestvideo[ext=mp4]",
            "outtmpl": output_template,
        }
    else:
        options = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": output_template,
            "quiet": False,
        }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(URL, download=True)
        title = info.get("title")
        downloaded_file = f"{title}.mp4"


def downloadMP3(URL, path=None):
    if path:
        output_template = f"{path}/%(title)s.%(ext)s"
    else:
        output_template = f"{cwd}/%(title)s.%(ext)s"

    # TODO: check for `/` at the end of the argument

    options = {
        "format": "bestaudio/best",
        "outtmpl": output_template,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192", 
            }
        ],
        "quiet": False,
        "extractaudio": True,  
        "keepvideo": False,  
    }

    with yt_dlp.YoutubeDL(options) as ydl:

        info = ydl.extract_info(URL, download=True)
        title = info.get("title", "audio")
        downloaded_file = f"{title}.mp4"

