import re
from re import finditer

from .entity_extraction import EntityExtraction
from .entity import Entity


class HeuristicsNER(EntityExtraction):
    """
    Cybersecurity entity extraction using Heuristics
    Most are based on the paper "Cybersecurity Named Entity Recognition Using Multi-Modal Ensemble Learning"
    https://ieeexplore.ieee.org/document/9051704
    URL - https://stackoverflow.com/a/17773849/5131287
    IPv4 - https://stackoverflow.com/a/36760050/5131287
    IPv6 - https://stackoverflow.com/a/17871737/5131287

    """
    def __init__(self, config):
        super().__init__(config)
        self.patterns = {
            'Filename': [r'[A-Za-z0-9-_\.]+\.(txt|php|exe|dll|bat|sys|htm|html|js|jar|jpg|png|vb|scr|pif|chm|zip|rar|cab|pds|doc|docx|ppt|pptx|xls|xlsx|swf|gif)',
            '^[a-zA-Z0-9](?:[a-zA-Z0-9 ._-]*[a-zA-Z0-9])?\.[a-zA-Z0-9_-]+$',
                         "^([A-Za-z]{1}[A-Za-z\\d_]*\\.)+[A-Za-z][A-Za-z\\d_]*$"],
            'Filepath': [r'[a-zA-Z]:\\([0-9a-zA-Z]+)', r'(\/[^\s\n]+)+'],
            'Email': [r'[a-z][_a-z0-9-.]+@[a-z0-9-]+[a-z]+'],
            'SHA1': [r'[a-f0-9]{40}|[A-F0-9]{40}'],
            'SHA256': [r'[a-f0-9]{64}|[A-F0-9]{64}'],
            'Hash': ['r"([a-fA-F\d]{32})"'],
            'Domain': ['"^(((([A-Za-z0-9]+){1,63}\.)|(([A-Za-z0-9]+(\-)+[A-Za-z0-9]+){1,63}\.))+){1,255}$"',
                       '(//|\s+|^)(\w\.|\w[A-Za-z0-9-]{0,61}\w\.){1,3}[A-Za-z]{2,6}'],
            'CVE': [r'CVE—[0-9]{4}—[0-9]{4,6}'],
            'URL': [r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})', r"https?:[a-zA-Z0-9_.+-/#~]+ "],
            'IPv4': [r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}$'],
            'IPAddress': ['r"^\d{1,3}\[.]\d{1,3}\.\d{1,3}\.\d{1,3}$"'],
            'Protocol': ['HTTP', 'SMS', 'HTTPS', 'AES'],
            'IPv6': [r'(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'],
        }

    def train(self):
        pass

    def get_entities(self, text):
        entities = []
        for label, pattern in self.patterns.items():
            for p in pattern:
                for match in finditer(p, text):
                    entities.append(Entity(match.span()[0], match.span()[1], match.group(), label))
        return entities
