"""
args:
1 corpus file (tokenized)
2 K
prints K most frequent vocab items
"""
import sys
from collections import Counter

default = ['<unk>', '<pad>', '<s>', '</s>']
for tok in default:
    with open('vocab.txt', 'a') as f:
        f.write(tok)
        f.write("\n")

c = Counter()
for l in open(sys.argv[1]):
    for tok in l.strip().split():
        tok = tok.lower()
        c[tok] += 1

for tok, _ in c.most_common(int(sys.argv[2])):
    with open('vocab.txt', 'a') as f:
        f.write(tok)
        f.write("\n")



