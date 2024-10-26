def main():
    file_path = "books/frankenstein.txt"
    print(character_count(file_path))


def count_words(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        words = content.split()
        return len(words)
    
def print_text(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        return content
    
def character_count(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        char_count = {}
        for char in content:
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        return char_count
    

main()