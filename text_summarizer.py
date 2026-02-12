# AI Text Summarizer using NLP
# Author: Juii Inamdar

import heapq
import re
from collections import defaultdict

# Sample text
text = """
Artificial Intelligence is transforming the world rapidly. It is used in healthcare,
finance, education, and many other industries. Machine learning is a subset of AI
that allows computers to learn from data. Deep learning is a more advanced form
of machine learning that uses neural networks. AI helps automate tasks and improve efficiency.
"""

# Step 1: Clean text
text = re.sub(r'\s+', ' ', text)

# Step 2: Split into sentences
sentences = text.split('.')

# Step 3: Word frequency
word_freq = defaultdict(int)

for word in text.lower().split():
    word_freq[word] += 1

# Step 4: Score sentences
sentence_scores = {}

for sentence in sentences:
    for word in sentence.lower().split():
        if word in word_freq:
            if sentence not in sentence_scores:
                sentence_scores[sentence] = word_freq[word]
            else:
                sentence_scores[sentence] += word_freq[word]

# Step 5: Get top sentences
summary_sentences = heapq.nlargest(2, sentence_scores, key=sentence_scores.get)

# Step 6: Print summary
summary = '. '.join(summary_sentences)

print("Original Text:\n", text)
print("\nSummary:\n", summary)
