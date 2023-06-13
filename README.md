# Extraction of Domain-Specific Relations in Spanish Labour Law

The code and data of the related project.

<p align="center">
<img src="https://github.com/pmchozas/term_relex/blob/master/static/approach.png" width="80%" />
</p>

## Structure

* [data](./data) contains the raw and the manually annotated data
* [model_training](./model_training) contains the scripts to train the model

## OLD Training with R-BERT

We use the cool and robust [R-BERT model](https://github.com/monologg/R-BERT) to recognize relations in the text.

### How to run

Check [train.conf](./model_training/train.conf) to provide the correct config values.

0. Create virtual environment (see [this link](https://docs.python.org/3/library/venv.html)) and install requirements (`pip3 install -r requirements.txt`).
1. Convert the manually annotated data
   ```bash
   cd model_training
   python3 convert.py --config_path train.conf
   ```
2. Train model
   ```bash
   cd model_training
   python3 train.py --config_path train.conf
   ```

## More recent results
We use a modification of [GRIT model](https://github.com/xinyadu/grit_doc_event_entity), our code is not published yet, but you can find the produced predictions at [data/predictions/grit/estatuto_predicted.json](data/predictions/grit/estatuto_predicted.json).

## Publications

Recently our paper was accepted to [DeepOntoNLP @ ESWC 2021](https://sites.google.com/view/deepontonlp-eswc2021/)!

To cite that paper:
```
@inproceedings{DBLP:conf/esws/Martin-ChozasR21,
  author    = {Patricia Mart{\'{\i}}n{-}Chozas and
               Artem Revenko},
  editor    = {Sarra Ben Abb{\`{e}}s and
               Rim Hantach and
               Philippe Calvez and
               Davide Buscaldi and
               Danilo Dess{\`{\i}} and
               Mauro Dragoni and
               Diego Reforgiato Recupero and
               Harald Sack},
  title     = {Thesaurus Enhanced Extraction of Hohfeld's Relations from Spanish
               Labour Law},
  booktitle = {Joint Proceedings of the 2nd International Workshop on Deep Learning
               meets Ontologies and Natural Language Processing (DeepOntoNLP 2021)
               {\&} 6th International Workshop on Explainable Sentiment Mining
               and Emotion Detection {(X-SENTIMENT} 2021) co-located with co-located
               with 18th Extended Semantic Web Conference 2021, Hersonissos, Greece,
               June 6th - 7th, 2021 (moved online)},
  series    = {{CEUR} Workshop Proceedings},
  volume    = {2918},
  pages     = {30--38},
  publisher = {CEUR-WS.org},
  year      = {2021},
  url       = {http://ceur-ws.org/Vol-2918/paper4.pdf},
  timestamp = {Tue, 10 Aug 2021 16:26:49 +0200},
  biburl    = {https://dblp.org/rec/conf/esws/Martin-ChozasR21.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```
