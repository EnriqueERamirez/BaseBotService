import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod

class BaseModel(ABC):
    def to_dict(self):
        return self.__dict__

    def to_json(self):
        return json.dumps(self.__dict__)

    def to_xml(self):
        root = ET.Element(self.__class__.__name__)
        for key, value in self.__dict__.items():
            elem = ET.SubElement(root, key)
            elem.text = str(value)
        return ET.tostring(root, encoding="unicode")

    @abstractmethod
    def from_dict(self, data: dict):
        pass

    @abstractmethod
    def from_json(self, data: str):
        pass

    @abstractmethod
    def from_xml(self, data: str):
        pass
