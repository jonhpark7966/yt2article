# yt2article/downloaders/youtube_downloader.py

from yt_dlp import YoutubeDL
from .downloader import Downloader

class YouTubeDownloader(Downloader):
    """Downloader for YouTube videos."""

    def download(self, url: str, output_path: str) -> str:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4'
        }
        with YoutubeDL(ydl_opts) as ydl:
            print(f"Downloading video from {url}")
            result = ydl.extract_info(url, download=True)
            # Construct the file path using title and ext from the result
            downloaded_file = f"{output_path}/{result['title']}.{result['ext']}"

        return downloaded_file

    def extract_audio(self, video_path: str, output_path: str):
        # NOT IMPLEMENTED: Logic to extract audio from video file
        print(f"Extracting audio from {video_path} to {output_path}")
        print("NOT IMPLEMENTED: Logic to extract audio from video file")

# Test the YouTubeDownloader class
if __name__  == "__main__":
    yt = YouTubeDownloader()
    yt.download("https://www.youtube.com/watch?v=6xlPJiNpCVw", "downloads")
