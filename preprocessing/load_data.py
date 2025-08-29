from datasets import load_dataset
import json

def load_webnlg(split="train"):
    ds = load_dataset("GEM/web_nlg", "en", trust_remote_code=True)
    return ds[split]

def preprocess_triples(example):
    # Convert triples into a structured form
    triples = example["tripleset"]
    structured = [(t["subject"], t["property"], t["object"]) for t in triples]
    return structured

if __name__ == "__main__":
    data = load_webnlg("train")
    for ex in data[:2]:
        print(preprocess_triples(ex))
