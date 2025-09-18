# File: rc_ICA4.py
# Description: Program that translates english text to pig latin.
# Input(s): English text
# Output(s): Pig latin translation
# By: Rodrigo Casanova-Aleman
#
# Three things I learned:
# 1. How to manipulate strings and implement simple text processing in Python.
# 2. How to structure a program with helper functions for clarity and reusability.
# 3. How to handle user input and loop for repeated actions.

# Helper functions
def clean_text(text):
    text = text.lower()
    for p in [".", ",", "!", "?"]:
        text = text.replace(p, "")
    return text

# Translate a single word to pig latin
def translate_word(word):
    vowels = "aeiou"

    # Find index of first vowel
    first_vowel_idx = -1
    for i in range(len(word)):
        ch = word[i]
        if (ch in vowels) or (ch == "y" and i != 0):
            first_vowel_idx = i
            break

    # If word starts with a vowel
    if first_vowel_idx == 0:
        return word + "way"

    # Consonant start: move all leading consonants to the end + "ay"
    if first_vowel_idx == -1:
        return word + "ay"
    else:
        return word[first_vowel_idx:] + word[:first_vowel_idx] + "ay"

# Translate a full sentence to pig latin
def to_pig_latin(text):
    # words are always separated by a single space
    words = text.split(" ")  
    out_words = []
    for w in words:
        out_words.append(translate_word(w))
    return " ".join(out_words)

# main program
def main():
    print("Welcome to Pig Latin Translator!")

    # Loop to allow multiple translations
    again = "y"
    while again and again[0].lower() == "y":
        print()  # blank line
        user_text = input("Enter text: ")

        english = clean_text(user_text)
        pig = to_pig_latin(english)

        print("English: ", english)
        print("Pig Latin:", pig)

        again = input("\nRepeat the program? (y/n): ")

    # Exit message
    print("\nThank you for using the program. Goodbye!")

# Call main to start the program
if __name__ == "__main__":
    main()