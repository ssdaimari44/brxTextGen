def aggregate(sentences):
    # Simple rule: merge same-subject sentences
    grouped = {}
    for sent in sentences:
        subj = sent.split()[0]  # crude: first token = subject
        grouped.setdefault(subj, []).append(sent)

    return [" ".join(group) for group in grouped.values()]