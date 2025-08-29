import json, yaml

def load_triples(path="data/triples.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_templates(path="data/templates.yaml"):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)