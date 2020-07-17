#!/usr/bin/env python
# coding: utf-8

import json
import pandas as pd

def to_df(entries):
    rows = []
    for ent_idx, entry in enumerate(entries):
        for par_idx, par in enumerate(entry['paragraphs']):
            for qa in par['qas']:

                row = {'entry_ind':ent_idx, 'title':entry['title'],
                      'paragraph_ind':par_idx, 'context':par['context'],
                      'qa_id':qa['id'],
                       'question':qa['question'],
                      'is_impossible': qa['is_impossible']}
                if len(qa['answers']) > 0:
                    row['answer_text'] = qa['answers'][0]['text']
                    row['answer_start'] = qa['answers'][0]['answer_start']
                rows.append(row)
    return pd.DataFrame(rows)
