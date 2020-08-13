import micropip
import pprint

def get_textstat(stat, text):
    import textstat
    return getattr(textstat, stat)(text)


def report_stats(text):
    
    stat_funcs = [
        "text_standard",  # aggregate of several reading gradelevel metrics
        "difficult_words",
    ]
    report = dict(zip(
        stat_funcs,
        map(get_textstat, stat_funcs)
    ))
    pprint(report)
    return report

from js import value as text 
report = micropip.install('textstat').then(report_stats(text))

