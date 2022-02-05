import config

ans = {}
yellow = {}
wrong_letters = []

def load_dict():
    with open('dict.txt') as f:
        words = f.read().splitlines()
    return words


def pick_word(words):
    return words[0] if len(words) > 0 else ""

def filter_words(words):
    for word_index in range(len(words)):
        print(words[word_index])
        if no_wrong_letters(words[word_index]) and correct_greens(words[word_index]) and yellow_position(words[word_index]):
            print("SUCCESS WITH", words[word_index])
            return words[word_index:]
    return ""

def no_wrong_letters(word):
    if len(wrong_letters) == 0:
        return True
    for letter in wrong_letters:
        if letter in word:
            return False
    return True

def correct_greens(word):
    for key,value in ans.items():
        if word[key] == value:
            continue
        else:
            return False
    return True

def yellow_position(word):
    for key,value in yellow.items():
        if value in word and word[key] != value:
            print("YES IN with", word)
            continue
        else:
            return False
    print(word)
    return True
# GREEN = "="
# YELLOW = "+"
# WRONG = "-"
# MOIST

def match_word(guess_word,result_colors):
    for index in range(len(result_colors)):
        if result_colors[index] == "=":
            ans[index] = guess_word[index]
        elif result_colors[index] == "+":
            yellow[index] = guess_word[index]
        elif result_colors[index] == "-":
            wrong_letters.append(guess_word[index])

        
if __name__ == "__main__":
    word_bank = load_dict()
    correct = False
    while(correct == False):
        guess_word = pick_word(word_bank)
        print(f"Guess this word next! {guess_word}")
        result_colors = input("What was the Result:")
        print(result_colors)
        if result_colors == "=====":
            correct = True
        match_word(guess_word,result_colors)
        word_bank = filter_words(word_bank)

