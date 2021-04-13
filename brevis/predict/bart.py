import requests
import json
from transformers import BartTokenizer

class SummaryModel:
    model = "facebook/bart-large-xsum"
    tokenizer = BartTokenizer.from_pretrained(model)
    print("Tokenizer loaded")

    def __init__(self):
        print("model loaded")

    def preprocess(self,text,maxlen):
            """Function to pre-process text inputs

            Args:
                text [str]: Text to be summarized

            Returns:
                [list]: tokens to pass to the predictor
            """
            #Pre-Process Data
            assert(type(text) == str),"Text being passed is not a string"
            assert(type(maxlen) == int),"Maxlen must be an integer"
            print("datatype Text confirmed")
            tokens = SummaryModel.tokenizer(text) 
            print("Tokens generated")

            batch = dict(tokens)
            batch["maxlen"] = maxlen
            batch = [batch]
            
            #Send Server Request
            input_data = {"signature_name": "serving_default","instances": batch}
            input_data = json.dumps(input_data)
            return input_data
        
    def pred(self,text,maxlen=300,tokens_only=False):
        """Returns summaries from model

        Args:
            text ([str]): text to be summarized
            tokens_only (bool, optional): Flag to set decoding returns. Defaults to False.

        Returns:
            [list]: returns summary text if 'tokens_only' set to false, 
                    else returns summary tokens
        """
        input_data = self.preprocess(text,maxlen)
        print("Data pre-processed")
        r = requests.post("http://localhost:8501/v1/models/bart:predict", data=input_data)
        print("Model inference complete")
        flag = False
        try:
            output_tokens = json.loads(r.text)['predictions']
        except KeyError:
            output_tokens = "ERROR:" + json.loads(r.text)['error']
            flag = True

        if(tokens_only or flag):
            return output_tokens
        else:
            return self.decoder(output_tokens)

    def decoder(self,tokens):
            """Returns summary text from summary

            Args:
                tokens ([list]): summary tokens

            Returns:
                [list]: list containing the string summary
            """
            result = [SummaryModel.tokenizer.decode(g, skip_special_tokens=False, clean_up_tokenization_spaces=False) for g in tokens]
            return resultimport requests
import json
from transformers import BartTokenizer

class SummaryModel:
    model = "facebook/bart-large-xsum"
    tokenizer = BartTokenizer.from_pretrained(model)
    print("Tokenizer loaded")

    def __init__(self):
        print("model loaded")

    def preprocess(self,text):
            """Function to pre-process text inputs

            Args:
                text [str]: Text to be summarized

            Returns:
                [list]: tokens to pass to the predictor
            """
            #Pre-Process Data
            assert(type(text) == str),"Text being passed is not a string"
            print("datatype Text confirmed")
            tokens = SummaryModel.tokenizer(text) 
            print("Tokens generated")

            batch = dict(tokens)
            batch = [batch]
            
            #Send Server Request
            input_data = {"signature_name": "serving_default","instances": batch}
            input_data = json.dumps(input_data)
            return input_data
        
    def pred(self,text,tokens_only=False):
        """Returns summaries from model

        Args:
            text ([str]): text to be summarized
            tokens_only (bool, optional): Flag to set decoding returns. Defaults to False.

        Returns:
            [list]: returns summary text if 'tokens_only' set to false, 
                    else returns summary tokens
        """
        input_data = self.preprocess(text)
        print("Data pre-processed")
        r = requests.post("http://localhost:8501/v1/models/bart:predict", data=input_data)
        print("Model inference complete")
        output_tokens = json.loads(r.text)['predictions']

        if(tokens_only):
            return output_tokens
        else:
            return self.decoder(output_tokens)

    def decoder(self,tokens):
            """Returns summary text from summary

            Args:
                tokens ([list]): summary tokens

            Returns:
                [list]: list containing the string summary
            """
            result = [SummaryModel.tokenizer.decode(g, skip_special_tokens=False, clean_up_tokenization_spaces=False) for g in tokens]
            return result