
import os
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer

# text = \
# """
# This is a project for the AngelHacks 2021 hackathon. We are trying to create a
# simple web application that summarizes notes for students. Simply upload a text
# file or directly paste your text in the textbox below. The frontend will be
# created with the React framework. The backend includes a Flask application and a
# natural language processing library in Python. The project will be posted on
# Devpost by Sunday.
# """

# parser_string = PlaintextParser.from_string(text, Tokenizer('english'))
# file_root_path = './venv/flask/test'
# file_name = 'mason_city.txt'
# file_path = str(os.path.join(file_root_path, file_name))
# print(f'file_path: {file_path}')
# parser_file = PlaintextParser.from_file(file_path, Tokenizer('english'))

# LexRank
# Chooses top k sentences deemed most important, but does not change the exact words.
def summarizeLexRank(text):
    parser_string = PlaintextParser.from_string(text, Tokenizer('english'))
    from sumy.summarizers.lex_rank import LexRankSummarizer
    print('\nLexRank')
    summarizer = LexRankSummarizer()
    # Summarize the document with 2 sentences
    sentences = summarizer(parser_string.document, 2)
    summary = ''
    for sent in sentences:
        summary += str(sent)
        summary += '\n'

    return summary
    # print('\nSummarizing text from .txt file:')
    # summary = summarizer(parser_file.document, 2)
    # for sent in summary:
    #     print(sent)

# Luhn
# Based on the frequency of important words only, while ignoring stop words
# (unimportant fillers e.g. the, a, at, for) and less frequent words
def summarizeLuhn(text):
    parser_string = PlaintextParser.from_string(text, Tokenizer('english'))
    from sumy.summarizers.luhn import LuhnSummarizer
    print('\nLuhn')
    summarizer = LuhnSummarizer()
    # Summarize the document with 2 sentences
    sentences = summarizer(parser_string.document, 2)
    #print('\nSummarizing text from string:')
    summary = ''
    for sent in sentences:
        summary += str(sent)
        summary += '\n'
    return summary

    #print('\nSummarizing text from .txt file:')
    #summary = summarizer(parser_file.document, 2)
    #for sent in summary:
    #    print(sent)

# LSA (Latent Semantic Analysis)
# Computes SVD on term frequencies
def summarizeLSA(text):
    parser_string = PlaintextParser.from_string(text, Tokenizer('english'))
    from sumy.summarizers.lsa import LsaSummarizer
    print('\nLSA')
    summarizer = LsaSummarizer()
    # Summarize the document with 2 sentences
    sentences = summarizer(parser_string.document, 2)
    #print('\nSummarizing text from string:')
    summary = ''
    for sent in sentences:
        summary += str(sent)
        summary += '\n'
    return summary
    #print('\nSummarizing text from .txt file:')
    #summary = summarizer(parser_file.document, 2)
    #for sent in summary:
    #    print(sent)

# KL
# Selects sentences by trying to match word distribution of sample as close to
# the original text as possible
def summarizeKL(text):
    parser_string = PlaintextParser.from_string(text, Tokenizer('english'))
    from sumy.summarizers.kl import KLSummarizer
    print('\nKL')
    summarizer = KLSummarizer()
    # Summarize the document with 2 sentences
    sentences = summarizer(parser_string.document, 2)
    #print('\nSummarizing text from string:')
    summary = ''
    for sent in sentences:
        summary += str(sent)
        summary += '\n'
    return summary

    #print('\nSummarizing text from .txt file:')
    #summary = summarizer(parser_file.document, 2)
    #for sent in summary:
    #    print(sent)


# Reading from PDF and word documents
import PyPDF2
import docx
from typing import Iterable


def read_pdf(pdf_name: str, page_numbers: Iterable[int]=None, by_paragraph: bool=False):
    """
    Read text from PDF file into a list, with the option to specify page numbers. If PDF is corrupted, handritten, or photocopied, do not use.
    If page_numbers is not specified, all pages are extracted. For each page, extracted text can be optionally divvied up based on paragraphs.

    Args:
        pdf_name (str): Title of PDF file
        page_numbers (Iterable[int], optional): Iterable of page numbers, first page is 1. If None, whole PDF is read. Defaults to None.
        by_paragraph (bool): Whether to extract paragraph by paragraph, or by page (default). Defaults to False.

    Returns:
        Iterable[str]: Iterable of extracted pieces of text
    """
    pdf_file = open(file=pdf_name, mode='rb')
    pdfReader = PyPDF2.PdfFileReader(stream=pdf_file, strict=True)

    #Ignores negative page numbers, forces unique numbers, and adds 1 to each page number (PyPDF starts with 0 for first page)
    page_numbers_corrected = range(start=1, stop=pdf_file.numPages + 1) \
        if page_numbers is None \
        else sorted(list(set([pg + 1 for pg in page_numbers if pg >= 0])))

    # Extracting text from each page and possibly each paragraph
    extracted_text = list()
    for pgno in page_numbers_corrected:
        page = pdfReader.getPage(pageNumber=pgno)
        page_text = page.extractText()
        if by_paragraph:
            for paragraph in page_text.splitlines():
                if len(paragraph) > 0:
                    extracted_text.append(paragraph)
        else:
            extracted_text.append(page_text)

    return extracted_text

def read_word_docx(docx_name: str, by_paragraph: bool=False):
    """
    Read word document into a list. By default, the whole document is read as a single string element into the list.

    Args:
        docx_name (str): [description]
        by_paragraph (bool, optional): [description]. Defaults to False.

    Returns:
        Iterable[str]: Iterable of extracted pieces of text
    """
    document = docx.Document(docx=docx_name)
    full_text = list()
    for paragraph in document.paragraphs:
        full_text.append(paragraph.text)

    if by_paragraph == False:
        full_text = list([''.join(full_text)])

    return full_text

##########################
# # PDF and word docx demo

# print('\nPDF extract by pages only:\n')
# texts = read_pdf(pdf_name='./test/short_stories.pdf', page_numbers=[1,2,4])
# for text in texts:
#     print(f'{text}\n')

# print('\nPDF extract by pages and paragraphs:\n')
# texts = read_pdf(pdf_name='./test/short_stories.pdf', page_numbers=[1,2,4], by_paragraph=True)
# for text in texts:
#     print(f'{text}\n')

# print('\nWord docx extract full text only:\n')
# texts = read_word_docx(docx_name='./test/Feeling unproductive_ Maybe you should stop overthinking. .docx')
# for text in texts:
#     print(f'{text}\n')

# print('\nWord docx extract by paragraphs:\n')
# texts = read_word_docx(docx_name='./test/Feeling unproductive_ Maybe you should stop overthinking. .docx', by_paragraph=True)
# for text in texts:
#     print(f'{text}\n')
