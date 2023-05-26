from flair.data import Sentence
from flair.models import SequenceTagger

from .entity_extraction import EntityExtraction
from .entity import Entity


class Flair(EntityExtraction):
    """
    Entity extraction using Flair NER model
    """

    def __init__(self, config):
        super().__init__(config)
        self.tagger = SequenceTagger.load(config["model"])

    def train(self):
        pass

    def get_entities(self, text):
        sentence = Sentence(text)
        self.tagger.predict(sentence)
        entities = []
        for span in sentence.get_spans("ner"):
            # 'labels' are formatted as [(TAG prob), ...]
            entities.append(
                Entity(
                    span.start_position,
                    span.end_position,
                    span.text,
                    span.labels[0].value,
                    span.labels[0].score,
                )
            )
        return entities
