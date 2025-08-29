def select_content(triples, max_triples=3):
    """
    Simple heuristic: select most 'important' triples
    Importance can be based on relation frequency or salience.
    """
    return triples[:max_triples]
