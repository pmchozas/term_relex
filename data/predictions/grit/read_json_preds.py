import dataclasses
import json
import os
from collections import Counter
from typing import List


@dataclasses.dataclass
class SentPred:
    text: str
    seq_type: str
    subject: List[List[str]]
    object: List[List[str]]
    relation: List[List[str]]
    complement: List[List[str]]


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


if __name__ == '__main__':
    sent_preds = read_preds(results_path=os.getenv('RESULTS_PATH', 'estatuto_predicted.json'))
    print(sent_preds[0])
    for t in ['Duty', 'Right', 'Noright', 'Privileg']:
        t_sents = [sent_pred for sent_pred in sent_preds if sent_pred.seq_type == t]
        print(f'{t}: {len(t_sents)} times predicted')
        subjects = sum([sum(sent_pred.subject, []) for sent_pred in t_sents], [])
        subjects_cnt = Counter(subjects)
        print(f'Subjects stats. all: {len(subjects)}, unique: {len(subjects_cnt)}, most frequent: {subjects_cnt.most_common(5)}')
        objects = sum([sum(sent_pred.object, []) for sent_pred in t_sents], [])
        objects_cnt = Counter(objects)
        print(f'Objects stats. all: {len(objects)}, unique: {len(objects_cnt)}, most frequent: {objects_cnt.most_common(5)}')
        rels = sum([sum(sent_pred.relation, []) for sent_pred in t_sents], [])
        rels_cnt = Counter(rels)
        print(f'Relations stats. all: {len(rels)}, unique: {len(rels_cnt)}, most frequent: {rels_cnt.most_common(5)}')