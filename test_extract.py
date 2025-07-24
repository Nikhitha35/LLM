# test_extract.py

from extract_and_chunk import extract_text_chunks

chunks = extract_text_chunks("data/BAJHLIP23020V012223.pdf")

print(f"Extracted {len(chunks)} chunks.")
print(chunks[0].page_content[:300])
