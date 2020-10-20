#!/usr/bin/env python3
from functools import partial
from pprint import pprint

def get_textstat(text, stat):
    from textstat.textstat import textstat
    return getattr(textstat, stat)(text)


def report_stats(text):
    
    stat_funcs = [
        "text_standard",  # aggregate of several reading gradelevel metrics
        "difficult_words",
    ]
    report = dict(zip(
        stat_funcs,
        map(partial(get_textstat,text), stat_funcs)
    ))
    pprint(report)
    return report

if __name__ == "__main__":
    import sys
    text  = sys.argv[1]
    report_stats(text)