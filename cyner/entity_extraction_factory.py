from .entity_extraction import EntityExtraction
from .flair_ner import Flair
from .spacy_ner import Spacy
from .heuristics_ner import HeuristicsNER
from .transformers_ner import TransformersNER


class EntityExtractionFactory:
    def __init__(self):
        pass

    @staticmethod
    def get_entity_extraction_model(name: str, config: dict) -> EntityExtraction:
        name = name.lower()
        if name == 'flair':
            return Flair(config)
        elif name == 'spacy':
            return Spacy(config)
        elif name == 'heuristics':
            return HeuristicsNER(config)
        elif name == 'transformers':
            return TransformersNER(config)
        else:
            raise ValueError('Unknown entity extraction model')
