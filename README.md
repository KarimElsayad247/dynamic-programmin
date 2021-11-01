# Dynamic Programming

1- Visualize problem: directed asyclic graph
2- Find appropriate subproblem: a simple version of the overall problem
    - All increasing subsequences have a start and end
3- Find relationships among subproblems
    - Ask questions, try to find a recursive relation, e.g.
      "The longest subsequenc ending in index 5 is 1 plus the longest subsequence
      reaching 5: LIS[5] = 1 + max{LIS[3] + LIS[1]}, assuming there're edges
      leading from 3 to 5, and 1 to 5
4- Generalize the relationship
5- Implement by finding subproblems in order
