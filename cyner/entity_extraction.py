from abc import ABC, abstractmethod


class EntityExtraction(ABC):
    @abstractmethod
    def __init__(self, config: dict):
        """
        initialize entity extraction model
        """
        pass

    @abstractmethod
    def train(self):
        """
        train the entity extraction model
        """
        pass

    @abstractmethod
    def get_entities(self, text):
        """

        :param text: input text
        :return: List of Entity objects
        """
        pass
