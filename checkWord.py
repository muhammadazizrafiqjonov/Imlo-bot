from uzwords import words
from latin import latin
from difflib import get_close_matches

def checkWord(word, words = words, latin=latin) :
    word = word.lower()
    if word.isascii():
        matches = set(get_close_matches(word, latin))
        available = False

        if word in matches:
            available = True
            matches = word
        elif 'ҳ' in word:
            word = word.replace('ҳ', 'х')
            matches.update(get_close_matches(word, latin))
        elif 'х' in word:
            word = word.replace('х', 'ҳ')
            matches.update(get_close_matches(word, latin))

        return {'available' : available, 'matches' : matches}
    else:
        matches = set(get_close_matches(word, words))
        available = False

        if word in matches:
            available = True
            matches = word
        elif 'ҳ' in word:
            word = word.replace('ҳ', 'х')
            matches.update(get_close_matches(word, words))
        elif 'х' in word:
            word = word.replace('х', 'ҳ')
            matches.update(get_close_matches(word, words))

        return {'available' : available, 'matches' : matches}

if __name__ == '__main__':
    print(checkWord("mато"))