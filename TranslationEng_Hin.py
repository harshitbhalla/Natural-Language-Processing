# This is a placeholder - replace with your actual translation code
def english_to_hindi(text):
    # Replace this with your translation logic
    translations = {
        "hello": "नमस्ते",
        "world": "दुनिया"
    }
    return translations.get(text.lower(), "Translation not found")

if __name__ == "__main__":
    english_text = input("Enter English text: ")
    hindi_translation = english_to_hindi(english_text)
    print(f"Hindi translation: {hindi_translation}")

##Second Change