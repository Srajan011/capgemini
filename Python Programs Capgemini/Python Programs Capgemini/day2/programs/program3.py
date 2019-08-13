def map_to_lengths_for(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths

words = ['abv', 'try me', 'test']
print(map_to_lengths_for(words))
