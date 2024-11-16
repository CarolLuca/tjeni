import bs4
from abc import ABC, abstractmethod
import chardet
class AIRoFile:
    name: str
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def parse_to_text(self) -> str:
        pass

    def read(self) -> tuple[bytes, str]:
        with open(self.name, mode='rb') as file:
            data = file.read()
            encoding_res = chardet.detect(data)
            encoding = encoding_res['encoding']
            return (data, encoding)

class AIRoHTMLFile(AIRoFile):
    def __init__(self, name: str):
        super().__init__(name)

    def parse_to_text(self) -> str:
        data, encoding = self.read()
        data_str = data.decode(encoding=encoding)
        soup = bs4.BeautifulSoup(data_str, "html.parser")
        return soup.get_text()




