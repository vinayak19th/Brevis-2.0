from .bart import SummaryModel

def summarizer(text,maxlen=200):
    model = SummaryModel()
    summary = model.pred(text,maxlen=maxlen)[0]
    print("Summary:",len(summary))
    return summary