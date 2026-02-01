def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    # Write code here
    mapping = {}
    for i in range(len(ordering)):
        mapping[ordering[i]] = i
    l = []
    for v in values:
        l.append(mapping[v])
    return l