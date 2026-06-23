from utils import flattenList

# =========practice 1===========
# Build a word-frequency counter for a paragraph using a dictionary.

para = "he old oak tree stood proudly at the center of the bustling city park, its sprawling branches offering a cool sanctuary from the midday sun. Beneath its canopy, children laughed while chasing pigeons, an artist quietly sketched the historic fountain, and a golden retriever patiently waited for its owner to toss a worn-out tennis ball. Meanwhile, the faint aroma of freshly roasted coffee drifted from a nearby café, blending seamlessly with the warm afternoon breeze."

wordCounter = dict()
para = para.lower()

word = ""
for l in para:
    if l.isalpha():
        word += l
    else:
        if word:
            wordCounter[word] = wordCounter.get(word, 0) + 1
            word = ""

for k, v in wordCounter.items():
    print(f"{k} appeared {v} time(s)")


# ==========practice 2=============
# Create a function that flattens a nested list. Architect a small utils.py module and import it into a main script.

nested_list = [
    ["The", "old", "oak"],
    ["tree", "stood"],
    [[["proudly", ["at"]], "the"]],
    "center",
]

print('\n', flattenList(nested_list))


# =========checkpoint==========
# Write a function group_by_first_letter(words) that returns a dictionary mapping each letter to a list of corresponding words.

words = [
    "Apple",
    "apricot",
    "Banana",
    "blueberry",
    "Cherry",
    "avocado",
    "blackberry",
    "Cranberry",
    "Date",
    "",
]

def group_by_first_letter(words):
    wordsLetter = dict()
    for word in words:
        if word:
            first = word[0].lower()
            wordsLetter[first] = wordsLetter.get(first, 0) + 1

    return wordsLetter

print('\n', group_by_first_letter(words))
