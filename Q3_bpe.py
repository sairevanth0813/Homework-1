from collections import Counter, defaultdict

# Toy corpus
corpus = "low low low low low lowest lowest newer newer newer newer newer newer wider wider wider new new"
words = corpus.split()
words = [w + "_" for w in words]

def get_vocab(words):
    vocab = Counter(words)
    return vocab

def get_stats(vocab):
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[(symbols[i], symbols[i+1])] += freq
    return pairs

def merge_vocab(pair, vocab):
    new_vocab = {}
    bigram = ' '.join(pair)
    replacement = ''.join(pair)
    for word in vocab:
        new_word = word.replace(bigram, replacement)
        new_vocab[new_word] = vocab[word]
    return new_vocab

# Initial vocab
vocab = Counter([' '.join(list(w)) for w in words])
print("Initial Vocab:", vocab)

# Perform first 3 merges
for i in range(3):
    pairs = get_stats(vocab)
    best = max(pairs, key=pairs.get)
    print(f"\nStep {i+1}: most frequent pair = {best}")
    vocab = merge_vocab(best, vocab)
    print("Updated Vocab:", vocab)

# Demonstrate segmentation
examples = ["new_", "newer_", "lowest_", "widest_", "newestest_"]
print("\nSegmentation examples:")
for ex in examples:
    seg = ' '.join(list(ex))
    print(ex, "->", seg)

reflection = """
Subword tokens help solve OOV by splitting unknown words into known subwords.
For example, 'newestest' can be segmented into 'new est est_'.
Suffixes like 'er_' align with real morphemes.
This balances character-level models (too long) with whole-word models (OOV problem).
"""
print("\nReflection:", reflection)