import string
from collections import Counter

def analyze_text(text):
    # Supprimer la ponctuation et mettre le texte en minuscule
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    
    # Découper le texte en mots
    words = cleaned_text.split()
    
    # Calcul des statistiques
    num_characters = len(text)  # Inclut les espaces et la ponctuation
    num_words = len(words)
    num_sentences = text.count('.') + text.count('!') + text.count('?')
    word_frequencies = Counter(words)
    
    # Résultats
    results = {
        "Nombre de caractères (incluant espaces)": num_characters,
        "Nombre de mots": num_words,
        "Nombre de phrases": num_sentences,
        "Fréquence des mots": word_frequencies
    }
