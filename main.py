def main():
    file_path = "books/frankenstein.txt"
    print(generate_report(file_path))


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
    
def generate_report(file_name):
    words = count_words(file_name)
    char_count = character_count(file_name)
    
    report = f"--- Begin report of {file_name} ---\n"
    report += f"{words} words found in the document\n\n"
    for char, count in char_count.items():
        report += f"The '{char}' character was found {count} times\n"
    report += f"--- End report ---"

    return report
    

main()