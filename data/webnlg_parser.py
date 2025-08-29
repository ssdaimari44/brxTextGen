import xml.etree.ElementTree as ET
import json

def parse_webnlg(xml_path, output_path="data/triples.json"):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    triples_list = []

    for entry in root.findall(".//entry"):
        for triple in entry.findall(".//triple"):
            parts = triple.text.split(" | ")
            if len(parts) == 3:
                subj, pred, obj = parts
                triples_list.append([subj.strip(), pred.strip(), obj.strip()])

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(triples_list, f, indent=2, ensure_ascii=False)

    print(f"✅ Parsed {len(triples_list)} triples from {xml_path}")

if __name__ == "__main__":
    parse_webnlg("data/webnlg/train.xml")
