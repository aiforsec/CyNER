import spacy

from .entity_extraction import EntityExtraction
from .entity import Entity


class Spacy(EntityExtraction):
    """
    Entity extraction using Flair NER model
    """
    def __init__(self, config):
        super().__init__(config)
        try:
            self.tagger = spacy.load(config['model'], disable=['tagger', 'attribute_ruler', 'lemmatizer'])
        except OSError:
            spacy.cli.download(config['model'])
            self.tagger = spacy.load(config['model'], disable=['tagger', 'attribute_ruler', 'lemmatizer'])

    def train(self):
        pass

    def get_entities(self, text):
        pred = self.tagger(text)
        entities = []
        for x in pred.ents:
            # Spacy does not provide confidence score
            # https://stackoverflow.com/questions/54085997/is-it-possible-to-get-a-confidence-score-on-spacy-named-entity-recognition
            entities.append(Entity(x.start_char, x.end_char, x.text, x.label_))
        return entities
