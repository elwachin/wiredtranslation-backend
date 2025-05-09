translations = {
    "spanish": "Hola. ¿Cómo estás?",
    "german": "Hallo. Wie geht es dir?",
    "french": "Bonjour. Comment ça va?",
    "italian": "Ciao. Come stai?",
    "danish": "Hej. Hvordan har du det?"
}

def translate_text(text, language):
    return translations.get(language.lower())

def to_jeringoza(text):
    result = ""
    vowels = "aeiouAEIOU"
    for char in text:
        result += char
        if char in vowels:
            result += "p" + char.lower()
    return result
