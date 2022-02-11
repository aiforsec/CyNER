import os

from .entity_extraction_factory import EntityExtractionFactory


def test_flair():
    config = {'model': 'ner'}
    entity_factory = EntityExtractionFactory()
    model = entity_factory.get_entity_extraction_model('flair', config)
    text = 'Apple is looking to buy USA startup for $1 billion.'
    print('Flair prediction for the text: {}'.format(text))
    entities = model.get_entities(text)
    for x in entities:
        print(x)


def test_spacy():
    config = {'model': 'en_core_web_trf'}
    entity_factory = EntityExtractionFactory()
    model = entity_factory.get_entity_extraction_model('spacy', config)
    text = 'Apple is looking to buy USA startup for $1 billion'
    print('Spacy prediction for the text: {}'.format(text))
    entities = model.get_entities(text)
    for x in entities:
        print(x)


def test_heuristics():
    config = {}
    entity_factory = EntityExtractionFactory()
    model = entity_factory.get_entity_extraction_model('heuristics', config)
    text = 'Example email abcd@gmail.com. Example website www.google.com. A sample file name xy_2.exe'
    print('Heuristics prediction for the text: {}'.format(text))
    entities = model.get_entities(text)
    for x in entities:
        print(x)


def test_ner():
    test_flair()
    test_spacy()
    test_heuristics()


if __name__ == '__main__':
    test_ner()
