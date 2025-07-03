import re
#This file contains the code function for the V1 and V2 version of the tokenizer build from scratch
class SimpleTokenizerV1:
    def __init__ (self,vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}
    def encoder(self,text):
        preprocessed = re.split(r'([:,.;!-?_"\'()]|--|\s)',text)
        preprocessed = [result.strip() for result in preprocessed if result.strip()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    def decoder(self,ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([:,.;!-?_"\'()])',r'\1',text)
        return text
class SimpleTokenizerV2:
    def __init__ (self,vocab):
        self.str_to_int = vocab
        self.int_to_str = {i:s for s,i in vocab.items()}
    def encoder(self,text):
        preprocessed = re.split(r'([:,.;!-?_"\'()]|--|\s)',text)
        preprocessed = [result.strip() for result in preprocessed if result.strip()]
        preprocessed = [item if item in self.str_to_int else "<|unk|>" for item in preprocessed]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids
    def decoder(self,ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([:,.;!-?_"\'()])',r'\1',text)
        return text

def main():
    with open("texts/J. K. Rowling - Harry Potter 1 - Sorcerer's Stone.txt","r",encoding="utf-8") as f:
       raw_text = f.read()
    
    preprocessed = re.split(r'([:,.;!-?_"\'()]|--|\s)',raw_text)
    preprocessed = [result.strip() for result in preprocessed if result.strip()]
    words = sorted(set(preprocessed))
    tokens = {token:integer for integer ,token in enumerate(words)}
    #initializing V1 tokenizer
    tokenizer = SimpleTokenizerV1(tokens)
    text = """Harry said "Dumbledore is such a pain to deal with" """
    ids = tokenizer.encoder(text)
    text = tokenizer.decoder(ids)
    print(text)
    #initializing V2 tokenizer
    preprocessed = re.split(r'([:,.;!-?_"\'()]|--|\s)',raw_text)
    preprocessed = [result.strip() for result in preprocessed if result.strip()]
    preprocessed.extend(["<|unk|>","<|endoftext|>"])
    words = sorted(set(preprocessed))
    tokens = {token:integer for integer ,token in enumerate(words)}
    tokenizer = SimpleTokenizerV2(tokens)
    text = """Harry said to Dumbeldore "Dumbledore yo fam you gotta chill brh" """
    ids = tokenizer.encoder(text)
    text = tokenizer.decoder(ids)
    print(text)

if __name__=="__main__":
    main()
