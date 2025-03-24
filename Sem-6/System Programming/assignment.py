from collections import Counter
import re
from docx import Document

doc = Document('Demo.docx')

word_count = Counter()

for paragraph in doc.paragraphs:
    words = re.findall(r'\b\w+\b', paragraph.text.lower())
    word_count.update(words)  

for word, count in word_count.items():
    print(f"{word}: {count}")