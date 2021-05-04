# Thesaurus Enhanced Extraction of Hohfeld's Relations from Spanish Labour Law

The code and data of the related project.

## Structure

* [data](./data) contains the raw and the manually annotated data
* [model_training](./model_training) contains the scripts to train the model

## Training

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

## Publications

Recently our paper was accepted to [DeepOntoNLP @ EXWC 2021](https://sites.google.com/view/deepontonlp-eswc2021/)!

Citation information will appear here when the proceedings are published.