from pathlib import Path
from typing import Optional, Union

import requests


class DownloadFile(object):
    def __init__(self, url: str, filepath: Union[Path, str]) -> None:
        """Download and save files

        Args:
            url: _description_
            filepath: _description_
        """
        self.url = url
        self.filepath = filepath
        self.response: Optional[requests.Response] = None

    def request_data(self) -> None:
        self.response = requests.get(self.url, allow_redirects=True)

    def save(self) -> None:
        if isinstance(self.response, requests.Response):
            with open(self.filepath, "wb") as f:
                f.write(self.response.content)
        else:
            raise ValueError(
                "There is no response to write. Please execute request first."
            )

    def request_and_save(self) -> None:
        self.request_data()
        self.save()
