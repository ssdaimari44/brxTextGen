# Triple-to-Text NLG (Template-based)

This project converts structured triples (subject, predicate, object) into natural language sentences using rule-based templates.

## Structure
- `data/` → triples.json (input), templates.yaml (rules), output.txt (generated text)
- `nlg/` → core Python modules
- `main.py` → run pipeline

## Usage
```bash
pip install -r requirements.txt
python main.py
