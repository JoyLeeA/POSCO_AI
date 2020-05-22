#20200518 Monday
import util


class NumberLineSearchProblem(util.SearchProblem):
    def __init__(self, size, end_state):
        self.size = size
        self.end_state = end_state
        
    def start_state(self):
        return 0
        
    def is_end(self, state):
        return state == self.end_state
        
    def succ_and_cost(self, state):
        results = []
        
        # West action
        if (state - 1) >= - self.size: #끝부분에 도달하지 않으면
            next_state = state - 1
            action = 'West'
            cost = 1
            results.append((action, next_state, cost))
        
        # East action
        if (state + 1) <= self.size:
            next_state = state + 1
            action = 'East'
            cost = 2
            results.append((action, next_state, cost))
        
        return results


if __name__ == '__main__':
    problem = NumberLineSearchProblem(5, 3) #왼쪽으로 5만큼 갈 수 있으면서, 골이 3인 문제 정의

    # import backtracking_search
    # bts = backtracking_search.BacktrackingSearch(verbose=3)
    # print(bts.solve(problem))  # backtracking_search won't end...

    import uniform_cost_search
    ucs = uniform_cost_search.UniformCostSearch(verbose=3)
    print(ucs.solve(problem)) #solve 해주면 알아서 해결해준다. 즉, problem정의가 중요하다.
