def top_n(items, n):
    """
    docstring goes here
    """

    for i in range(n):  # Keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:  # If this item is bigger than next the item..
                items[j], items[j+1] = items[j+1], items[j]  # swap the two!

    # Get last two items
    top_n = items[-n:]

    # Return in descending order
    return top_n[::-1]