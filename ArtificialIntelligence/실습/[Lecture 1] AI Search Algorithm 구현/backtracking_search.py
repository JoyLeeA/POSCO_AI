#20200518 Monday

#Search Alogithmn중에 성능이 제일 안좋음.
#대신 가장 optimal하게 찾아줌.
import util

class BacktrackingSearch(util.SearchAlgorithm): #UCS가 하는 역할
    def __init__(self, verbose=0):
        self.verbose = verbose
        
    def recurrence(self, state, path, path_cost): #최적의 경로를 찾음
        if self.verbose >= 2:
            print('state %s with path %s [%d]'%(state, path, path_cost))
        self.num_visited += 1
        
        # Check end condition
        if self.problem.is_end(state):
            if self.verbose >= 1:
                print('... new path %s [%d]'%(path, path_cost))
            if self.best_path is None or path_cost < self.best_path_cost:  # HINT: compare path_cost with self.best_path_cost
                self.best_path, self.best_path_cost = tuple(path), path_cost
        
        # Find minimum cost path
        else:
            for action, next_state, action_cost in self.problem.succ_and_cost(state):
                path.append(action)  # extend path
                extended_path_cost = path_cost + action_cost
                self.recurrence(next_state, path, extended_path_cost) # HINT: call self.recurrence
                path.pop()      # recover path

    def solve(self, problem):
        # Not thread-safe
        self.problem = problem
        self.num_visited = 0
        self.best_path, self.best_path_cost = None, None
        
        initial_state = problem.start_state()
        empty_path = [] #optimal path를 모르기 때문에 빈 것을 넣음.
        self.recurrence(initial_state, empty_path, 0)
        #recurrence('S') -> return [(S,A,G),3]
        return self.best_path, self.best_path_cost, self.num_visited
