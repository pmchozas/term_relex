# Thesaurus Enhanced Extraction of Hohfeld's Relations from Spanish Labour Law

The code and data of the related project.

## Structure

* [data](./data) contains the raw and the manually annotated data
* [model_training](./model_training) contains the scripts to train the model

## Training

We use the cool and robust [R-BERT model](https://github.com/monologg/R-BERT) to recognize relations in the text.

### How to run

Check [train.conf](./model_training/train.conf) to provide the correct config values.

0. Create virtual environment (see [this link](https://docs.python.org/3/library/venv.html)). 
   
1. Clone R-BERT: `git clone https://github.com/monologg/R-BERT.git`, add R-BERT to your PYTHONPATH: `export PYTHONPATH=$PYTHONPATH:./R-BERT`. In `R-BERT/utils.py` comment oiut line 65 (`        "f1": official_f1(),`).
2. Convert the manually annotated data
   ```bash
   cd model_training
   python3 convert.py --config_path train.conf
   ```
3. Train model
   ```bash
   cd model_training
   python3 train.py --config_path train.conf
   ```

## Publications

Recently our paper was accepted to [DeepOntoNLP @ ESWC 2021](https://sites.google.com/view/deepontonlp-eswc2021/)!

Citation information will appear here when the proceedings are published.