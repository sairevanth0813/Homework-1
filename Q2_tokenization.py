import spacy

# Sample paragraph
paragraph = """Natural Language Processing is exciting! 
It’s used in chatbots, search engines, and translation. 
However, tokenization isn’t always easy."""

# Naïve space-based tokenization
naive_tokens = paragraph.split()
print("Naïve tokens:", naive_tokens)

# Manually corrected tokens
manual_tokens = [
    "Natural","Language","Processing","is","exciting","!","It","’s",
    "used","in","chatbots",",","search","engines",",","and","translation",".",
    "However",",","tokenization","is","n’t","always","easy","."
]
print("\nManual tokens:", manual_tokens)

# spaCy tokenizer
nlp = spacy.load("en_core_web_sm")
doc = nlp(paragraph)
spacy_tokens = [t.text for t in doc]
print("\nspaCy tokens:", spacy_tokens)

# Multiword expressions
mwes = ["Natural Language Processing", "search engine", "machine learning"]
print("\nMultiword expressions:", mwes)

# Reflection
reflection = """
The hardest part of tokenization was handling punctuation and clitics like "isn’t".
English tokenization requires splitting contractions and handling apostrophes properly.
Compared to other languages (e.g., agglutinative ones), English is easier, but MWEs still complicate it.
Punctuation, morphology, and fixed phrases make naive approaches insufficient.
"""
print("\nReflection:", reflection)