def merge_dicts(dict1, dict2):
    """Merges two dictionaries, summing the values of common keys."""
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = merged.get(key, 0) + value
    return merged
