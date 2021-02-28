
import os
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

text = \
"""
This is a project for the AngelHacks 2021 hackathon. We are trying to create a simple web application that summarizes notes for students. Simply
upload a text file or directly paste your text in the textbox below. The frontend will be created with the React framework. The backend includes
a Flask application and a natural language processing library in Python. The project will be posted on Devpost by Sunday.
"""

parser_string = PlaintextParser.from_string(text, Tokenizer('english'))
file_root_path = '../test'
file_name = 'mason_city.txt'
file_path = str(os.path.join(file_root_path, file_name))
print(f'file_path: {file_path}')
parser_file = PlaintextParser.from_file(file_path, Tokenizer('english'))

# LexRank
# Chooses top k sentences deemed most important, but does not change the exact words.
from sumy.summarizers.lex_rank import LexRankSummarizer
print('\nLexRank')
summarizer = LexRankSummarizer()
# Summarize the document with 2 sentences
summary = summarizer(parser_string.document, 2)
print('\nSummarizing text from string:')
for sent in summary:
    print(sent)

print('\nSummarizing text from .txt file:')
summary = summarizer(parser_file.document, 2)
for sent in summary:
    print(sent)

# Luhn
# Based on the frequency of important words only, while ignoring stop words (unimportant fillers e.g. the, a, at, for) and less frequent words
from sumy.summarizers.luhn import LuhnSummarizer
print('\nLuhn')
summarizer = LuhnSummarizer()
# Summarize the document with 2 sentences
summary = summarizer(parser_string.document, 2)
print('\nSummarizing text from string:')
for sent in summary:
    print(sent)

print('\nSummarizing text from .txt file:')
summary = summarizer(parser_file.document, 2)
for sent in summary:
    print(sent)

# LSA (Latent Semantic Analysis)
# Computes SVD on term frequencies
from sumy.summarizers.lsa import LsaSummarizer
print('\nLSA')
summarizer = LsaSummarizer()
# Summarize the document with 2 sentences
summary = summarizer(parser_string.document, 2)
print('\nSummarizing text from string:')
for sent in summary:
    print(sent)

print('\nSummarizing text from .txt file:')
summary = summarizer(parser_file.document, 2)
for sent in summary:
    print(sent)

# KL
# Selects sentences by trying to match word distribution of sample as close to the original text as possible
from sumy.summarizers.kl import KLSummarizer
print('\nKL')
summarizer = KLSummarizer()
# Summarize the document with 2 sentences
summary = summarizer(parser_string.document, 2)
print('\nSummarizing text from string:')
for sent in summary:
    print(sent)

print('\nSummarizing text from .txt file:')
summary = summarizer(parser_file.document, 2)
for sent in summary:
    print(sent)

