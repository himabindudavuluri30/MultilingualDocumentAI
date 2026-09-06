from utils.language import detect_language

text = """
Artificial intelligence is transforming the way people work and communicate.
Machine learning systems can analyze large amounts of data and find useful patterns.
Natural language processing allows computers to understand and process human language.
"""

language = detect_language(text)

print("Detected language:", language)