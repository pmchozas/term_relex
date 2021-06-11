import dataclasses
import logging.config
from enum import Enum
from pathlib import Path

import configparser


class RelationTypes(Enum):
    dut = 'Duty'
    right = 'Right'
    noright = 'Noright'
    privilege = 'Privilege'
    norelation = 'Norelation'

    @classmethod
    def set(cls):
        return set(map(lambda c: c.value, cls))

    @classmethod
    def has_value(cls, value):
        return value in cls.set()


@dataclasses.dataclass
class RelationSample:
    id_: int
    context: str
    # head_start: int
    # head_end: int
    # tail_start: int
    # tail_end: int
    type_: RelationTypes

    def to_tsv(self):
        out = f'{self.type_}\t{self.context}'
        return out


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path',
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

    with open(config['convert']['txt_annotations']) as f:
        txt_data = f.read()
    rels = []
    for rel_block in txt_data.split('\n\n'):
        id_ = None
        for line in rel_block.split('\n'):
            if '\t' in line and line.strip():
                id_, cxt = line.split('\t')
                id_ = int(id_)
                cxt = cxt.strip()
                cxt = cxt.replace('<rel>', '').replace('</rel>', '')
            elif line.startswith('RelationType'):
                _, info = line.split(':')
                rel_type = info.split('(')[0].strip()
        if id_ is not None:
            assert RelationTypes.has_value(rel_type), repr(rel_type)
            rel_inst = RelationSample(id_=id_, context=cxt, type_=rel_type)
            rels.append(rel_inst)

    labels_str = '\n'.join(RelationTypes.set())
    dev_insts = rels[:int(config['convert']['dev_samples'])]
    train_insts =  rels[int(config['convert']['dev_samples']):]

    with open(config['convert']['output_dev'], 'w') as f:
        out = '\n'.join(x.to_tsv() for x in dev_insts)
        f.write(out)
    with open(config['convert']['output_train'], 'w') as f:
        out = '\n'.join(x.to_tsv() for x in train_insts)
        f.write(out)
    with open(config['convert']['output_labels'], 'w') as f:
        f.write(labels_str)
