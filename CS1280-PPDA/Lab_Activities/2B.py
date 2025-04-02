def word_count(text):
    """Counts occurrences of each word in a text."""
    words = text.split()
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq
