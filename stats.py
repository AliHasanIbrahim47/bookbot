def sort_on(items):
    return items["num"]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters_dict(text):
    characters = {}
    for char in text:
        if char.isalpha() and char.lower() in characters:
            characters[char.lower()] += 1
        else:
            if char.isalpha():
                characters[char.lower()] = 1
    
    return characters

def print_list_of_characters_dict(text):
    characters = get_characters_dict(text)
    characters_list = []
    for char, count in characters.items():
        characters_list.append({"char": char, "num": count})

    characters_list.sort(reverse=True, key=sort_on)
    for item in characters_list:
        print(f"{item['char']}: {item['num']}")