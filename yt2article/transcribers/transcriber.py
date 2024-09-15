# This module defines an abstract base class for media transcriber.
# Input is video or audio file, and output is plain text.

from abc import ABC, abstractmethod

class Transcriber(ABC):
    """Abstract base class for all media transcribers."""

    @abstractmethod
    def transcribe(self, input_path: str, output_path: str):
        """Transcribe the media file at the given input path and save the text to the output path."""
        pass
