def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    # Merge two dictionaries
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

# Example 
if __name__ == "__main__":
    dict1 = {'a': 10, 'b': 20}
    dict2 = {'b': 30, 'c': 40}
    merged_dict = merge_dicts(dict1, dict2)
    print("Merged dictionary:", merged_dict)
