def remove_duplicates(L):

    it = L
    while it:
        # Uses next_distinct to find the next distinct value.
        next_distinct = it.next
        while next_distinct and next_distinct.data == it.data:
            next_distinct = next_distinct.next
        it.next = next_distinct
        it = next_distinct
    return L
