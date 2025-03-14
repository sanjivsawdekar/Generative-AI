# Types of Text Splitters

Besides **RecursiveCharacterTextSplitter**, there are several other
**text splitters** available in **LangChain** and other libraries for
RAG systems. Here’s a list of some commonly used ones:

## 1. CharacterTextSplitter (Basic)

- Splits text based on characters (e.g., \n, spaces).

- Simpler and faster than RecursiveCharacterTextSplitter but can break
  sentences.
```
from langchain.text_splitter import CharacterTextSplitter

splitter = CharacterTextSplitter(

separator="\n\n", \# Split by paragraphs

chunk_size=1000,

chunk_overlap=50

)

chunks = splitter.split_text(document)
```
✅ **Best for:** Simple documents, blogs, raw text.

## 2. TokenTextSplitter (Token-Based)

- Splits based on **LLM tokens** instead of characters.

- Useful when working with OpenAI models to fit within token limits.
```
from langchain.text_splitter import TokenTextSplitter

splitter = TokenTextSplitter(

chunk_size=512,

chunk_overlap=50

)

chunks = splitter.split_text(document)
```
✅ **Best for:** Ensuring chunk sizes match LLM context limits.

## 3. NLTKTextSplitter (Sentence-Based)

- Uses **NLTK** to split by sentences, preventing mid-sentence breaks.
```
from langchain.text_splitter import NLTKTextSplitter

splitter = NLTKTextSplitter()

chunks = splitter.split_text(document)
```
✅ **Best for:** News articles, structured reports.

## 4. SpacyTextSplitter (Linguistic-Based)

- Uses **SpaCy** for sentence-based chunking.

- More **accurate** than NLTKTextSplitter for some languages.
```
from langchain.text_splitter import SpacyTextSplitter

splitter = SpacyTextSplitter()

chunks = splitter.split_text(document)
```
✅ **Best for:** NLP-heavy applications, multi-language text.

## 5. MarkdownTextSplitter (Markdown Docs)

- Splits text while **preserving Markdown structure** (# Headings, -
  Lists, \*\*Bold\*\*).
```
from langchain.text_splitter import MarkdownTextSplitter

splitter = MarkdownTextSplitter()

chunks = splitter.split_text(markdown_document)
```
✅ **Best for:** Documentation, technical blogs.

## 6. HTMLHeaderTextSplitter (Web Content)

- Splits text based on **HTML tags** (\<h1\>, \<p\>, etc.).

- Extracts structured sections from webpages.
```
from langchain.text_splitter import HTMLHeaderTextSplitter

splitter = HTMLHeaderTextSplitter(

headers_to_split_on=\[("h1", "Title"), ("h2", "Subsection")\]

)

chunks = splitter.split_text(html_document)
```
✅ **Best for:** Web scraping, FAQs, structured articles.

## 7. SentenceTransformersTextSplitter (Semantic Chunking)

- Uses **SBERT** embeddings to split text **by meaning**, not just size.

- Ensures semantically coherent chunks.
```
from langchain.text_splitter import SentenceTransformersTextSplitter

splitter = SentenceTransformersTextSplitter(

model_name="all-MiniLM-L6-v2", \# Any SBERT model

chunk_size=256

)

chunks = splitter.split_text(document)
```
✅ **Best for:** Legal, medical, and structured documents.

## 8. TiktokenTextSplitter (OpenAI Token-Aware)

- Uses **OpenAI’s tiktoken** for precise token splitting.

- Ensures chunks fit within **GPT’s context window**.
```
from langchain.text_splitter import TiktokenTextSplitter

splitter = TiktokenTextSplitter(

model_name="gpt-4",

chunk_size=1000

)

chunks = splitter.split_text(document)
```
✅ **Best for:** OpenAI API calls, optimizing token usage.

# Comparison Table

| **Splitter** | **Method** | **Best for** |
|----|----|----|
| RecursiveCharacterTextSplitter | Overlapping chunks | General-purpose RAG |
| CharacterTextSplitter | Simple character-based | Blogs, articles |
| TokenTextSplitter | Token-based splitting | LLM token optimization |
| NLTKTextSplitter | Sentence-based (NLTK) | News, reports |
| SpacyTextSplitter | Sentence-based (SpaCy) | NLP-heavy apps |
| MarkdownTextSplitter | Markdown-aware | Technical docs, wikis |
| HTMLHeaderTextSplitter | HTML-aware | Web scraping, FAQs |
| SentenceTransformersTextSplitter | Semantic-based | Legal, structured docs |
| TiktokenTextSplitter | OpenAI token-aware | GPT models |

## Which one should you use?

- **Short documents:** CharacterTextSplitter

- **LLM context optimization:** TiktokenTextSplitter

- **Semantic chunking:** SentenceTransformersTextSplitter

- **Technical docs (Markdown/HTML):** MarkdownTextSplitter /
  HTMLHeaderTextSplitter


Reference - https://www.analyticsvidhya.com/blog/2025/02/types-of-chunking-for-rag-systems/
