def popular_words(text, words):
    text_words = text.lower()
    text_words = text_words.split()
    result = {}

    for word in words:
        matches = list(filter(lambda x: x == word, text_words))
        result[word] = len(matches)

    return result
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')


