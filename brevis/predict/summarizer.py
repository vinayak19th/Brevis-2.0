from .bart import SummaryModel

def summarizer(text,maxlen=200):
    model = SummaryModel()
    summary = model.pred(text,maxlen=maxlen)
    if (len(summary[0])>2):
        summary = summary[0]
    print("Summary:",len(summary))
    print("Summary[0]:",len(summary[0]))
    return summary