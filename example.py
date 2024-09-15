from yt2article.downloaders.youtube_downloader import YouTubeDownloader
from yt2article.transcribers.whisper_transcriber import WhisperTranscriber

def test_main_function():
    #downloaded_file = YouTubeDownloader().download("https://www.youtube.com/watch?v=6xlPJiNpCVw", "./downloads")
    downloaded_file = "./downloads/test.mp4"
    print(downloaded_file)
    WhisperTranscriber().transcribe(downloaded_file, "./downloads/transcription.txt")

if __name__ == "__main__":
    test_main_function()
