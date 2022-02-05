import config

ans = {}
yellow_color = {}
wrong_letters = []

def load_dict():
    with open('dict.txt') as f:
        words = f.read().splitlines()
    return words


def pick_word(word_bank):
    return word_bank[0] if len(word_bank) > 0 else ""


def match_word(guess_word,result_colors):
    for index in range(len(result_colors)):
        if result_colors[index] == "=":
            ans[index] = guess_word[index]
        elif result_colors[index] == "+":
            yellow_color[index] = guess_word[index]
        elif result_colors[index] == "-":
            if(guess_word[index] in yellow_color.values()):
                continue
            else:
                wrong_letters.append(guess_word[index])

def filter_words(word_bank):
    for word_index in range(len(word_bank)):
        if gray(word_bank[word_index]) and yellow(word_bank[word_index]) and correct_greens(word_bank[word_index]):
            return word_bank[word_index:]

def gray(word):
    for letter in wrong_letters:
        if letter in word:
            return False
    return True

def yellow(word):
    for key,value in yellow_color.items():
        if word[key] != value and value in word:
            continue
        else:
            return False
    return True

def correct_greens(word):
    for key,value in ans.items():
        if word[key] == value:
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    word_bank = load_dict()
    print(len(word_bank))
    end_me = False
    while(end_me == False):
        guess_word = pick_word(word_bank)
        result_colors = input()
        if result_colors == "=====":
            print("DONE")
            end_me = True
        match_word(guess_word,result_colors)
        word_bank = filter_words(word_bank)
        print(len(word_bank))
        print(word_bank[0:15])