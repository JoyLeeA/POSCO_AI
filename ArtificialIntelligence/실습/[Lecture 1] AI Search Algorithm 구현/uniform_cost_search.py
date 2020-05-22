#20200519 Tuesday
import util

class UniformCostSearch(util.SearchAlgorithm):
    def __init__(self, verbose=0):
        self.verbose = verbose

    def solve(self, problem, init_cost=0):
        numStatesExplored = 0

        # Initialize data structures
        frontier = util.PriorityQueue()  # Frontier states
        explored = set() # Explored states (집합으로 정의)
        backpointers = {}  # map state to (action, previous state)
        frontier.update(problem.start_state(), init_cost)

        while not frontier.is_empty(): #frontier가 텅 비어 질 때 까지 반복     
            numStatesExplored += 1
            
            # Remove the state from the queue with the lowest priority.
            state, priority = frontier.remove_min() #다음에 올 노드 찾음 (가작 작은)
            
            # Add state to explored
            explored.add(state)
            
            if self.verbose >= 2:
                print("Exploring %s with pastCost %s" % (state, priority))

            # Check if we've reached an end state; if so, extract solution.
            if problem.is_end(state): #state 가 Goal 이면
                totalCost = priority #(cost)
                actions = []
                while state != problem.start_state():
                    action, prevState = backpointers[state] #state G에 대해서 backpointer 잡음
                    actions.append(action) #backpointer에 저장
                    state = prevState #backpointer에 저장
                actions.reverse() # 과정을 반대로 뒤집어줌
                if self.verbose >= 1:
                    print("numStatesExplored = %d" % numStatesExplored)
                    print("totalCost = %s" % totalCost)
                    print("actions = %s" % actions)
                return actions, totalCost, numStatesExplored

            # Expand from |state| to new successor states,
            # updating the frontier with each newState.
            for action, newState, cost in problem.succ_and_cost(state): #S에서 취할 수 있는 모든 경우의 수 찾아봄
                if self.verbose >= 3:
                    print("  Action %s => %s with cost %s + %s" % (action, newState, priority, cost))
                if newState not in explored: #explored에 있는 것은 찾아
                    # Found better way to go to |newState|, update backpointer.
                    new_priority = priority + cost
                    is_updated = frontier.update(newState, new_priority)
                    if is_updated:
                        backpointers[newState] = (action, state)
        if self.verbose >= 1:
            print("No path found")
            
        return None, None, numStatesExplored
