import re


def split_text(text, max_len=500):
    sentences = re.split(r'(?<=[.!?]) +', text)
    chunks, current = [], ''
    for s in sentences:
        if len(current) + len(s) < max_len:
            current += ' ' + s
        else:
            chunks.append(current.strip())
            current = s
    if current:
        chunks.append(current.strip())
    return chunks