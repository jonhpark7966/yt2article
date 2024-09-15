# # This module defines an abstract base class for media downloaders.
# It includes methods for downloading media and extracting audio from videos. /downloader.py

from abc import ABC, abstractmethod

class Downloader(ABC):
    """Abstract base class for all media downloaders."""

    @abstractmethod
    def download(self, url: str, output_path: str) -> str:
        """Download media from the given URL and save it to the output path."""
        return ""

    @abstractmethod
    def extract_audio(self, video_path: str, output_path: str):
        """Extract audio from the downloaded video (if applicable)."""
        pass
