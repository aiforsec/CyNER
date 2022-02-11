from .entity_extraction import EntityExtraction
from .entity import Entity
from .tner import TrainTransformersNER
from .tner import TransformersNER as PredictTransformersNER


class TransformersNER(EntityExtraction):
    """
    Entity extraction using Transformers
    """
    def __init__(self, config):
        super().__init__(config)
        self.config = config
        self.classifier = None

    def train(self):
        config = self.config
        checkpoint_dir = config.get('checkpoint_dir', './ckpt')
        dataset = config.get('dataset', 'dataset/mitre')
        transformers_model = config.get('model', 'xlm-roberta-base')
        random_seed = config.get('random_seed', 1)
        lr = config.get('lr', 1e-5)
        epochs = config.get('epochs', 20)
        warmup_step = config.get('warmup_step', 0)
        weight_decay = config.get('weight_decay', 1e-7)
        batch_size = config.get('batch_size', 32)
        max_seq_length = config.get('max_seq_length', 128)
        fp16 = config.get('fp16', False)
        max_grad_norm = config.get('max_grad_norm', 1)
        lower_case = config.get('lower_case', False)
        num_worker = config.get('num_worker', 0)
        cache_dir = config.get('cache_dir', None)

        trainer = TrainTransformersNER(checkpoint_dir=checkpoint_dir,
                                        dataset=dataset,
                                        transformers_model=transformers_model,
                                        random_seed=random_seed,
                                        lr=lr,
                                        epochs=epochs,
                                        warmup_step=warmup_step,
                                        weight_decay=weight_decay,
                                        batch_size=batch_size,
                                        max_seq_length=max_seq_length,
                                        fp16=fp16,
                                        max_grad_norm=max_grad_norm,
                                        lower_case=lower_case,
                                        num_worker=num_worker,
                                        cache_dir=cache_dir)

        trainer.train(monitor_validation=True)

    def get_entities(self, text):
        if self.classifier is None:
            self.classifier = PredictTransformersNER(self.config.get('model', 'xlm-roberta-base'))
        ret = self.classifier.predict([text])
        entities = []
        for x in ret[0]['entity']:
            start, end = x['position']
            text = x['mention']
            entity_type = x['type']
            confidence = x['probability']
            entities.append(Entity(start, end, text, entity_type, confidence))
        
        return entities
