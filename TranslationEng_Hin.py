# Install Packages
# pip install transformers
# pip install torch
# pip install sentencepiece

import sys
import os
from transformers import pipeline

# Set environment variables for proper Unicode handling
os.environ["PYTHONIOENCODING"] = "utf-8"

# Set console output encoding to UTF-8
if sys.platform.startswith('win'):
    # For Windows
    import locale
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def initialize_translator():
    # Initialize the translation pipeline
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")
    return translator

def english_to_hindi(translator, text):
    # Translate the text
    translation = translator(text, max_length=400)
    return translation[0]['translation_text']

def main():
    # Print a test Unicode string to verify encoding
    print("Testing Unicode: नमस्ते")
    print("\nInitializing translator (this may take a moment)...")
    
    try:
        translator = initialize_translator()
        print("Translator ready!")
        
        while True:
            # Get input from user
            english_text = input("\nEnter English text (or 'quit' to exit): ")
            
            # Check if user wants to quit
            if english_text.lower() == 'quit':
                break
                
            try:
                # Perform translation
                hindi_translation = english_to_hindi(translator, english_text)
                print(f"\nEnglish: {english_text}")
                print(f"Hindi: {hindi_translation}")
            except Exception as e:
                print(f"An error occurred during translation: {str(e)}")
    
    except Exception as e:
        print(f"An error occurred during initialization: {str(e)}")

if __name__ == "__main__":
    main()



