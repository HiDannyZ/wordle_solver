import config

target = "wrong"
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
    print_state()
    for word in words:
        if no_wrong_letters(word):
            print(f"wrong:{word}")
        if correct_greens(word):
            print(f"green:{word}")
        if yellow_position(word):
            print(f"yellow:{word}")
        else:
            continue
        return word
    return "ERROR"

def no_wrong_letters(word):
    if not wrong_letters:
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
        if word[key] != value:
            continue
        else:
            return False
    return True
# GREEN = "="
# YELLOW = "+"
# WRONG = "-"
# MOIST
# +=-=+
def match_word(guess_word,result_colors):
    for index in range(len(result_colors)):
        if result_colors[index] == "=":
            ans[index] = guess_word[index]
        elif result_colors[index] == "+":
            yellow[index] = guess_word[index]
        elif result_colors[index] == "-":
            wrong_letters.append(guess_word[index])

def take_a_guess(guess_word):
    result_colors = ""
    return result_colors

def print_state():
    print(ans)
    print(yellow)
    print(wrong_letters)
        
if __name__ == "__main__":
    # words = load_dict()
    # result_colors = take_a_guess(pick_word())
    # match_word(guess_word,result_colors)
    # filter_words()

    match_word("toasm","+=-=+")
    words = ['aback', 'mogst', 'moist']
    a = filter_words(words)
    print(a)