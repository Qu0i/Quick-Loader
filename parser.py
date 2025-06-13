import argparse
import os

cwd = os.getcwd()


def get_args():
    parser = argparse.ArgumentParser(prog="ql", description="CLI YouTube downloader")

    parser.add_argument("--version", action="store_true", help="Display ql version")
    parser.add_argument("link", nargs="?", help="YouTube video URL")
    parser.add_argument(
        "-f", "--format", help="selecting file format (mp3/mp4)", default="mp4"
    )
    parser.add_argument(
        "-o", "--output", help="Selecting a download directory", default=cwd
    )
    parser.add_argument(
        "-v", "--video", help="Download video only (without audio)", action="store_true"
    )
    parser.add_argument(
        "-s",
        "--search",
        help="[COMING SOON]Search videos for download by title/request",
        action="store_true",
    )
    parser.add_argument(
        "--info", help="[COMING SOON] Only show video information", action="store_true"
    )
    parser.add_argument("--preset", help="Use selected preset", action="store_true")

    return parser.parse_args()
