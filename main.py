import config

target = "wrong"

def load_dict():
    with open('dict.txt') as f:
        words = f.read().splitlines()
    return words
    
def pick_word(words):
    return words[0] if len(words) > 0 else ""

def filter_words():
    return

# GREEN = "="
# YELLOW = "+"
# WRONG = "-"
def match_word():
    
        
if __name__ == "__main__":
    words = load_dict()
