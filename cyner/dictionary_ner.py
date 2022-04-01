import re
import csv

from .entity_extraction import EntityExtraction
from .entity import Entity


class DictionaryNER(EntityExtraction):
    """
    Cybersecurity entity extraction using words in dictionary

    """
    def __init__(self, config):
        super().__init__(config)
        file_name = config['file']
        
        self.dict = {}
        
        with open('dictionary.csv') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)
            for row in reader:
                self.dict[row[0]] = row[1]

    def train(self):
        pass

    def get_entities(self, text):
        entities = []
        for mention, cls in self.dict.items():
            matches = [m.start() for m in re.finditer(mention, text)]
            for match in matches:
                entities.append(Entity(match, match+len(mention), mention, cls, 1))
        return entities
