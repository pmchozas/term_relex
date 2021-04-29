import argparse
import configparser
import dataclasses
import logging
from pathlib import Path

from data_loader import load_and_cache_examples
from trainer import Trainer
from utils import init_logger, load_tokenizer, set_seed


@dataclasses.dataclass
class TrainerArgs:
    data_dir: str
    train_tsv: str
    dev_tsv: str
    model_dir: str
    eval_dir: str
    train_file: str
    test_file: str
    label_file: str
    model_name_or_path: str = 'bert-base-multilingual-uncased'
    task: str = 'semeval'

    seed = 77
    train_batch_size = 4
    eval_batch_size = 32
    max_seq_len = 384
    learning_rate = 2e-5
    num_train_epochs = 3.0
    weight_decay = 0.0
    gradient_accumulation_steps = 1
    adam_epsilon = 1e-8
    max_grad_norm = 1.0
    max_steps = -1
    warmup_steps = 0
    dropout_rate = 0.1
    logging_steps = 250
    save_steps = 250
    do_train = True
    do_eval = True
    no_cuda = True
    add_sep_token = True


def main(args: TrainerArgs):
    init_logger()
    set_seed(args)
    tokenizer = load_tokenizer(args)

    train_dataset = load_and_cache_examples(args, tokenizer, mode="train")
    test_dataset = load_and_cache_examples(args, tokenizer, mode="test")

    trainer = Trainer(args, train_dataset=train_dataset, test_dataset=test_dataset)

    if args.do_train:
        trainer.train()
        trainer.evaluate("test")

    if args.do_eval:
        trainer.load_model()
        trainer.evaluate("test")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('config_path',
                        type=str,
                        help='Relative (to this script) path to the config file')
    args = parser.parse_args()
    this_dir = Path(__file__).parent
    config_paths = this_dir / args.config_path
    config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
    config.read(config_paths)
    logger = logging.getLogger()
    # logging.config.fileConfig(config)
    logger.info(f'Config: {config.items("convert")}')
    ########
    args = TrainerArgs(
        **config['rbert_training']
    )

    main(args)
