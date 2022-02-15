# CyNER: Python Library for Cybersecurity Named Entity Recognition

#### TODO: Add summary

### Get Started
`pip install git+https://github.com/aiforsec/CyNER.git`


### Prediction
To get prediction with pretrained NER model  

```
import cyner

model = cyner.CyNER(transformer_model='xlm-roberta-large', use_heuristic=False, flair_model=None)

text = 'Proofpoint report mentions that the German-language messages were turned off once the UK messages were established, indicating a conscious effort to spread FluBot 446833e3f8b04d4c3c2d2288e456328266524e396adbfeba3769d00727481e80 in Android phones.'

entities = model.get_entities(text)

for e in entities:
    print(e)
```

Please check `CyNER Demo` notebook for more details.


## Training 
To finetune model on user provided dataset  

```
cfg = {'checkpoint_dir': '.ckpt',
        'dataset': 'dataset/mitre',
        'transformers_model': 'xlm-roberta-large',
        'lr': 5e-6,
        'epochs': 20,
        'max_seq_length': 128}
model = cyner.TransformersNER(cfg)
model.train()
```

