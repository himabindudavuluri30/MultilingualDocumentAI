from utils.summarizer import summarize_text


text = """
Artificial intelligence is transforming many industries around the world.
Machine learning allows computers to learn patterns from data and make
predictions. Deep learning uses neural networks with multiple layers to
process complex information such as images, speech, and text. Generative AI
goes one step further by creating new content such as text, images, audio,
and code. These technologies are increasingly being used in education,
healthcare, finance, customer service, and software development.
"""


summary = summarize_text(text)

print("Original Text:")
print(text)

print("\nSummary:")
print(summary)