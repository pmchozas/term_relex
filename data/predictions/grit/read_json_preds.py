import dataclasses
import json
import os
from collections import Counter
from enum import Enum
from typing import List


@dataclasses.dataclass
class SentPred:
    text: str
    seq_type: str
    subject: List[List[str]]
    object: List[List[str]]
    relation: List[List[str]]
    complement: List[List[str]]


class Slots(Enum):
    subject = 'subject'
    object = 'object'
    relation = 'relation'
    complement = 'complement'


def read_preds(results_path) -> List[SentPred]:
    with open(results_path) as f:
        results = json.load(f)
    # for r in results:
    #     sent_pred = SentPred(text=r['doctext'], seq_type=r['seq_pred'],
    #                          subject=r['subject'], object=r['object'],
    #                          relation=r['relation'], complement=r['complement'])
    return [SentPred(text=r['doctext'], seq_type=r['seq_pred'],
                     subject=r['subject'], object=r['object'],
                     relation=r['relation'], complement=r['complement'])
            for r in results]


def count_stats(preds: List[SentPred], slot: Slots):
    fillers = sum([sum(sent_pred.__dict__[slot], []) for sent_pred in preds], [])
    fillers_cnt = Counter(fillers)
    return fillers_cnt


if __name__ == '__main__':
    sent_preds = read_preds(results_path=os.getenv('RESULTS_PATH', 'estatuto_predicted.json'))
    print(sent_preds[0])
    for t in ['Duty', 'Right', 'Noright', 'Privileg']:
        t_sents = [sent_pred for sent_pred in sent_preds if sent_pred.seq_type == t]
        print(f'{t}: {len(t_sents)} times predicted')
        subjects_cnt = count_stats(t_sents, 'subject')
        print(f'Subjects stats. all: {sum(subjects_cnt.values())}, unique: {len(subjects_cnt)}, most frequent: {subjects_cnt.most_common(5)}')

        objects_cnt = count_stats(t_sents, 'object')
        print(f'Objects stats. all: {sum(objects_cnt.values())}, unique: {len(objects_cnt)}, most frequent: {objects_cnt.most_common(5)}')

        rels_cnt = count_stats(t_sents, 'relation')
        print(f'Relations stats. all: {(sum(rels_cnt.values()))}, unique: {len(rels_cnt)}, most frequent: {rels_cnt.most_common(5)}')

        complements_cnt = count_stats(t_sents, 'complement')
        print(f'complements stats. all: {(sum(complements_cnt.values()))}, unique: {len(complements_cnt)}, most frequent: {complements_cnt.most_common(5)}')