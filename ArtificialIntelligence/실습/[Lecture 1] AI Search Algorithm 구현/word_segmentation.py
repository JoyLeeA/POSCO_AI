#20200520 Wendsday
import util
import wordsegUtil


class SegmentationProblem(util.SearchProblem): #Seacrh Problem 정의
    def __init__(self, query, unigramCost):
        self.query = query # 분석하고자 하는 문자열 입력
        self.unigramCost = unigramCost #Unigram값 출력(-logP(w))

    def start_state(self):
        return 0  # num of characters used to construct words

    def is_end(self, state):
        return state == len(self.query)

#step: 현재 까지 띄어쓰기를 진행한 문자의 수

    def succ_and_cost(self, state): #다음에 취할 수 있는 모든 Action을 찾는 것
        for step in range(1, len(self.query) - state + 1):
            next_state = state + step 
            word = self.query[state: next_state] #현재 states 에서 다음 states에 해당하는 query
            cost = self.unigramCost(word)
            yield word, next_state, cost  # action, next_state, cost
            # yield를 할때마다 element가 list에 추가됨
            # action이 이루어지면 알아서 띄어쓰기가 된다고 이해하면 된다.

if __name__ == '__main__':
    unigramCost, bigramCost = wordsegUtil.makeLanguageModels('leo-will.txt') #함수를 만들어 주는 것(leo-will.txt = corpus, 이것을 통해서 Language Model을 만드는 것이다.)
    #Corpus에 없는 단어가 들어가면, 코스트가 무한대가 된다.(잘 작동하지 않는다.)
    problem = SegmentationProblem('thisisnotmybeautifulhouse', unigramCost)

    # import dynamic_programming_search
    # dps = dynamic_programming_search.DynamicProgrammingSearch(verbose=1)
    # # dps = dynamic_programming_search.DynamicProgrammingSearch(memory_use=False, verbose=1)
    # print(dps.solve(problem))

    import uniform_cost_search
    ucs = uniform_cost_search.UniformCostSearch(verbose=0)
    print(ucs.solve(problem))


# === Other Examples ===
#
# QUERIES_SEG = [
#     'thestaffofficerandprinceandrewmountedtheirhorsesandrodeon',
#     'hellothere',
#     'officerandshort',
#     'erprince',
#     'howdythere',
#     'whatsup',
#     'duduandtheprince',
#     'duduandtheking',
#     'withoutthecourtjester',
#     'lightbulbneedschange',
#     'imagineallthepeople',
#     'thisisnotmybeautifulhouse',
# ]
