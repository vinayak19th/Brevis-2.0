import os
import string
import pickle
import json
from pathlib import Path

import argparse
from tqdm import tqdm

punctuations = string.punctuation + "'' “”'-"

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ctx = self.root
    
    def reset_ctx(self):
        self.ctx = self.root

    def step(self, ch):
        if ch in self.ctx.children:
            self.ctx = self.ctx.children[ch]
            return True
        return False

    def insert(self, word):
        ptr = self.root
        for ch in word:
            if ch not in ptr.children:
                ptr.children[ch] = TrieNode()

            ptr = ptr.children[ch]

        ptr.is_end = True

    def insert_vocab_list(self, vocab_list: list):
        for word in tqdm(vocab_list):
            self.insert(word.lower())

    def insert_vocab_json(self, jsonfilepath):
        with open(jsonfilepath) as f:
            jsonfile = json.load(f)
            self.insert_vocab_list(jsonfile)

    def test_corpus__(self, corpus) -> bool:
        self.reset_ctx()
        c = 0
        not_in_vocab = []

        for word in corpus.lower().split():
            self.reset_ctx()
            stale = False

            for ch in word:

                if stale or not ch.isalpha():
                    continue

                if not self.step(ch):
                    c += 1
                    not_in_vocab.append(word)
                    stale = True

        print(f"{c} words not in vocab {not_in_vocab}")
        return True
                
            
    def test_corpus_(self, corpus) -> bool:
        # tests to see if there is any word in the corpus that is not in the dictionary
        ptr = self.root
        c = 0
        not_in_vocab = []

        stale = False

        for word in corpus.lower().split():
            stale = False
            ptr = self.root
            for ch in word:
                if stale:
                    continue
                if ch in punctuations:
                    print(word, ch)
                    continue
                    # test for punctuations
                    # if not ptr.is_end:
                    #     # return False
                    #     c += 1
                    #     not_in_vocab.append(word)
                    #     stale = True


                    ptr = self.root
                else:
                    if ch not in ptr.children:
                        # return False
                        c += 1
                        not_in_vocab.append(word)
                        stale = True

                    if not stale:
                        ptr = ptr.children[ch]

        print(f"{c} words not in vocab {not_in_vocab}")
        return True

    def test_corpus(self, corpus, dispbad=False) -> bool:
        # tests to see if there is any word in the corpus that is not in the dictionary
        ptr = self.root
        
        for ch in corpus.lower():
            if ch in punctuations:
                # test for punctuations
                if not ptr.is_end:
                    return False

                ptr = self.root
            else:
                if ch not in ptr.children:
                    return False
                ptr = ptr.children[ch]

        return ptr.is_end or ptr == self.root

    def save(self, filepath):
        with open(filepath, 'wb') as f:
            pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self, filepath):
        with open(filepath, 'rb') as f:
            trie_saved = pickle.load(f)
        self.root = trie_saved.root


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-json", "--jsonfilename", help="json vocab file name")
    parser.add_argument("-save", "--savefilename", help="trie save file name")

    args = parser.parse_args()

    BASE_DIR = Path(__file__).resolve().parent
    VOCAB_DIR = os.path.join(BASE_DIR, 'savedvocab')
    SAVED_TRIE_DIR = os.path.join(BASE_DIR, 'savedtries')

    trie = Trie()

    if args.jsonfilename:
        vocabjsonpath = os.path.join(VOCAB_DIR, args.jsonfilename)
        print(f"opening {vocabjsonpath}.")
        trie.insert_vocab_json(vocabjsonpath)


        if args.savefilename:
            print(f"Saving to {args.savefilename}.")
            trie.save(os.path.join(SAVED_TRIE_DIR, args.savefilename))


    print(VOCAB_DIR)