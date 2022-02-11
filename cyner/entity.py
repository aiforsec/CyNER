class Entity:
    def __init__(self, start, end, text, entity_type, confidence=1):
        """
        :param start: start position of the entity in the source text
        :param end: end position of the entity in the source text
        :param text: entity text
        :param entity_type: type of the entity
        :param confidence: probability or confidence (range [0, 1])
        """
        self.start = start
        self.end = end
        self.text = text
        self.entity_type = entity_type
        self.confidence = confidence

    def __str__(self, ):
        return 'Mention: {}, Class: {}, Start: {}, End: {}, Confidence: {:.2f}'.\
            format(self.text, self.entity_type, self.start, self.end, self.confidence)
