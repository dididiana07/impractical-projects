import json

def load(json_file):
    """Return the content of a JSON file."""
    try:
        with open(json_file, "r") as file_open:
            data = json.load(file_open)
    except json.decoder.JSONDecodeError:
        return "Not a JSON file."
    return data


def palingram(word: str, dictionary_words: dict):
    """Find if a word is a palingram"""
    palingram_lst = []
    reversed_word = word[::-1]
    for w in dictionary_words:
        if reversed_word in w and len(reversed_word) > 2:
            palingram_lst.append(w)
    return palingram_lst

def main():
    dictionary = load("2_finding_palingram_spells/words_dictionary.json")
    word = input("Word: ")
    results = palingram(word, dictionary)
    print(f"Results: {len(results)}")
    print("---------------")
    print("\n".join(results))



if __name__ == "__main__":
    main()
