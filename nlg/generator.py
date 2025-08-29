def generate_sentence(triple, templates):
    subject, predicate, obj = triple
    rules = templates["templates"]
    default = templates.get("defaults", {}).get("generic", "{subject} {predicate} {object}.")

    template = rules.get(predicate, default)
    return template.format(subject=subject, predicate=predicate, object=obj)