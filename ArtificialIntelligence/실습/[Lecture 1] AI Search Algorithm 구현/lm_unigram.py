#20200519 Tuesday
import math, collections


corpus = [
    'I am Sam',
    'Sam I am',
    'I do not like green'
]

# Counting
unigram_counts = collections.defaultdict(int)
for sentence in corpus:
    words = sentence.split()
    for word in words:
        unigram_counts[word] += 1 # 각 단어가 몇번 나오는지 카운트

# Printing unigram counts
print('- Unigram counts -')
for word in unigram_counts:
    print(('unigram_count[%s] = %d'%(word, unigram_counts[word])))
    # 특정 단어의 수 / 전체 단어의 수

# Unigram function
def unigram(word):
    return float(unigram_counts[word]) / sum(unigram_counts.values())
        
# Printing results
print('\n- Unigram probabilities - ')
print(('P(Sam) = %f'%unigram('Sam')))
print(('P(I) = %f'%unigram('I')))
print(('P(green) = %f'%unigram('green')))
