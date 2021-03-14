from json import decoder
from django.apps import AppConfig
from transformers import BartTokenizer
import requests
import json

class PredictConfig(AppConfig):
    name = 'predict'
    model = "facebook/bart-large-xsum"
    tokenizer = BartTokenizer.from_pretrained(model)
    
    def preprocess(self,text):
        #Pre-Process Data
        tokens = PredictConfig.tokenizer(text) 
        batch = dict(tokens)
        batch = [batch]
        
        #Send Server Request
        input_data = {"signature_name": "serving_default","instances": batch}
        input_data = json.dumps(input_data)
        return input_data
    
    def pred(self, text,tokens_only=False):
        input_data = self.preprocess(text)
        r = requests.post("http://localhost:8501/v1/models/bart:predict", data=input_data)
        output_tokens = json.loads(r.text)['predictions']
        if(tokens_only):
            return output_tokens
        else:
            return decoder(output_tokens)
    
    def decoder(self,tokens):
        result = [PredictConfig.tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in tokens]
        return result
