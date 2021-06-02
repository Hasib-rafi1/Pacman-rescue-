# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    dfs_path = util.Stack()
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    open = util.Stack()
    open.push((problem.getStartState(), 'Start', 1))
    closed = []
    path_stack = util.Stack()
    path=[]
    parent_map = {}
    while open.isEmpty() is not True:
        x = open.pop()
        if problem.isGoalState(x[0]):
            SearchProblem.dfs_path.push(x)
            searchParent(parent_map,x[0])
            while not SearchProblem.dfs_path.isEmpty():
                    l = SearchProblem.dfs_path.pop()
                    path.append(l[1])
            return path
        else:
            successor = problem.getSuccessors(x[0])
            z = len(successor)
            temp_stack = util.Stack()
            for y in range(0,z):
                k = successor.pop()
                temp_stack.push(k)
            for y in range(0,z):
                c = temp_stack.pop()
                if c[0] not in closed:
                    open.push(c)
                    parent_map[c[0]]= x
            closed.append(x[0])

    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    open = util.Queue()
    open.push([problem.getStartState(), []])
    closed = []
    while not open.isEmpty():
        x = open.pop()
        if x[0] not in closed:
            closed.append(x[0])
            if problem.isGoalState(x[0]):
                return x[1]
            for successor in problem.getSuccessors(x[0]):
                if successor[0] not in closed:
                    open.push([successor[0], x[1] + [successor[1]]])

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    open = util.PriorityQueue()
    open.push([problem.getStartState(), [], 0],0)
    closed = []
    # while open.isEmpty() is not True:
    #     x = open.pop()
    #     if problem.isGoalState(x[0]):
    #         SearchProblem.dfs_path.push(x)
    #         searchParent(parent_map,x[0])
    #         while not SearchProblem.dfs_path.isEmpty():
    #                 l = SearchProblem.dfs_path.pop()
    #                 path.append(l[1])
    #         return path
    #     else:
    #         successor = problem.getSuccessors(x[0])
    #         z = len(successor)
    #         for y in range(0,z):
    #             k = successor.pop()
    #             if k[0] not in closed:
    #                 action = x[1]+[k[1]]
    #                 open.update(k,problem.getCostOfActions(action))
    #                 opend.append(k[0])
    #                 parent_map[k[0]]= x
    #         closed.append(x[0])

    while not open.isEmpty():
        x = open.pop()
        if x[0] not in closed:
            if problem.isGoalState(x[0]):
                return x[1]
            closed.append(x[0])
            for successor in problem.getSuccessors(x[0]):
                if successor[0] not in closed:
                    action = x[1] + [successor[1]]
                    open.push([successor[0], action,successor[0]], problem.getCostOfActions(action))


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    open = util.PriorityQueue()
    open.push([problem.getStartState(), [], 0],0)
    closed = []
    while not open.isEmpty():
        x = open.pop()
        if x[0] not in closed:
            if problem.isGoalState(x[0]):
                return x[1]
            closed.append(x[0])
            for successor in problem.getSuccessors(x[0]):
                if successor[0] not in closed:
                    action = x[1] + [successor[1]]
                    open.push([successor[0], action,successor[1]], problem.getCostOfActions(action) + heuristic(successor[0], problem))

def searchParent(parent_map,current):
    x = parent_map[current]
    if x[1] is not 'Start':
        SearchProblem.dfs_path.push(parent_map[current])
        searchParent(parent_map,x[0])
    else:
        return SearchProblem.dfs_path




# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
