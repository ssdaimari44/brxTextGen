def lexicalize(triple):
    subj, rel, obj = triple
    mapping = {
        "birthPlace": "was born in",
        "author": "was written by",
        "capital": "is the capital of"
    }
    if rel in mapping:
        return f"{subj} {mapping[rel]} {obj}"
    else:
        return f"{subj} {rel.replace('_',' ')} {obj}"

def microplan(triples):
    return [lexicalize(t) for t in triples]
