def sort_by_age(tuples_list):
    # Sort tuples by age (second element)
    return sorted(tuples_list, key=lambda x: x[1])

# Example
if __name__ == "__main__":
    data = [("niki", 31), ("jake", 24), ("mike", 36)]
    sorted_data = sort_by_age(data)
    print("Sorted by age:", sorted_data)
