from nlg.loader import load_triples, load_templates
from nlg.generator import generate_sentence
from nlg.aggregator import aggregate
from nlg.realiser import realise

def main():
    triples = load_triples("data/triples.json")
    templates = load_templates("data/templates.yaml")

    sentences = [generate_sentence(t, templates) for t in triples]
    realised = [realise(s) for s in sentences]

    aggregated = aggregate(realised)

    with open("data/output.txt", "w", encoding="utf-8") as f:
        for s in aggregated:
            f.write(s + "\n")

    print("✅ Generation complete. Check data/output.txt")

if __name__ == "__main__":
    main()
