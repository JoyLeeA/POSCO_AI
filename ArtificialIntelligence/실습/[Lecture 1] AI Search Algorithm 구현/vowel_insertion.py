#20200520 Wendsday
#모음을 채워주는 과정

import util
import wordsegUtil


class VowelInsertionProblem(util.SearchProblem):
    def __init__(self, queryWords, bigramCost, possibleFills):
        self.queryWords = queryWords #모음이 제거된 리스트 혹은 튜플
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills # 모든 경우를 고려하지 않도록 만들기 위함

    def start_state(self):
        return 0, wordsegUtil.SENTENCE_BEGIN  # word position & previous reconstructed word (단어의 위치와, 이전에 만들어진 단어)
        #(0, -Begin) (모음을 채운 갯수, 채우고자 하는 단어 이전에 있는 단어) ex> (1, Thats)

    def is_end(self, state):
        return state[0] == len(self.queryWords) #vowel_inesrtion을 다 수행하게 되면 같아짐

    def succ_and_cost(self, state):
        pos, prev_word = state #pos = position
        vowel_removed_word = self.queryWords[pos]
        fills = self.possibleFills(vowel_removed_word) | {vowel_removed_word} #자음으로만 구성된 단어도 포함시켜줌(거의 없음)
        #fills에 후보들이 담겨있음. (m, am, ym....)
        for fill in fills:
            next_state = pos + 1, fill
            cost = self.bigramCost(prev_word, fill) # 이전 단어와 현재 단어의 bigram (흐름의 자연스러움 측정)
            yield fill, next_state, cost  # return action, state, cost


if __name__ == '__main__':    
    unigramCost, bigramCost = wordsegUtil.makeLanguageModels('leo-will.txt')
    possibleFills = wordsegUtil.makeInverseRemovalDictionary('leo-will.txt', 'aeiou')
    problem = VowelInsertionProblem('thts m n th crnr'.split(), bigramCost, possibleFills)
    # problem = VowelInsertionProblem([wordsegUtil.removeAll(word, 'aeiou') for word in 'whats up'.split()], bigramCost, possibleFills)

    # import dynamic_programming_search
    # dps = dynamic_programming_search.DynamicProgrammingSearch(verbose=1)
    # # dps = dynamic_programming_search.DynamicProgrammingSearch(memory_use=False, verbose=1)
    # print(dps.solve(problem))

    import uniform_cost_search
    ucs = uniform_cost_search.UniformCostSearch(verbose=0)
    print(ucs.solve(problem))


# === Other Examples ===
# 
# QUERIES_INS = [
#     'strng',
#     'pls',
#     'hll thr',
#     'whats up',
#     'dudu and the prince',
#     'frog and the king',
#     'ran with the queen and swam with jack',
#     'light bulbs need change',
#     'ffcr nd prnc ndrw',
#     'ffcr nd shrt prnc',
#     'ntrntnl',
#     'smthng',
#     'btfl',
# ]
