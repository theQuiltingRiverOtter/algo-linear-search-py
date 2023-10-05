def linear_search(value_to_find, array_to_search_through):
    for ind, val in enumerate(array_to_search_through):
        if val == value_to_find:
            return ind
    return None


def linear_search_global(value_to_find, array_to_search_through):
    all_indices = []
    for ind, val in enumerate(array_to_search_through):
        if val == value_to_find:
            all_indices.append(ind)
    return all_indices
