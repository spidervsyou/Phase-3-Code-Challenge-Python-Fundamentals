def sort_by_age(persons):
    """Sorts a list of tuples by age in ascending order."""
    return sorted(persons, key=lambda x: x[1])
