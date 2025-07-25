from design_add_and_search_words_data_structure import WordDictionary

def test1():
    wordDictionary = WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    assert wordDictionary.search("pad") == False
    assert wordDictionary.search("bad") == True
    assert wordDictionary.search(".ad") == True
    assert wordDictionary.search("b..") == True