from transformers_ner import TransformersNER


def run_bert():
    cfg1 = {'checkpoint_dir': 'logs/xlm-roberta-base',
            'dataset': 'dataset/mitre',
            'transformers_model': 'xlm-roberta-base',
            'lr': 1e-5,
            'epochs': 20,
            'batch_size': 8,
            'max_seq_length': 128}
    model1 = TransformersNER(cfg1)
    model1.train()

    # cfg2 = {'checkpoint_dir': 'logs/xlm-roberta-large',
    #         'dataset': 'dataset/mitre',
    #         'transformers_model': 'xlm-roberta-large',
    #         'lr': 5e-6,
    #         'epochs': 20,
    #         'max_seq_length': 256}
    # model2 = TransformersNER(cfg2)
    # model2.train()


if __name__ == '__main__':
    run_bert()
