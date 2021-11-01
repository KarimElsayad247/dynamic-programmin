def lis(A):
    # L is a list, the same size of the input list, but with all
    # elements initialzed as 1, this being the length of the initial
    # longest subsequence. 
    L = [1] * len(A)    

    # for each element in the original sequence:
    for i in range(1, len(L)):
        # the relation between subproblems. in this step, find the LIS
        # from the 1st element until the current element. In each loop, 
        # the required subproblems will have been already solved in the
        # previous loop. 
        # Equation: LIS[n] = 1 + max{LIS[i] | k < i, A[k] < A[i]}
        # Using this formalized equatin, construct an expression 
        # doing the same thing.
        # First, find the possible subproblems which go into the max
        # operator. Possible subroblems are those at indices smaller
        # than i (before current element) and whose contents are smaller
        # than the contents of current node
        subproblems = [ L[k] for k in range(i) if A[k] < A[i]]
        
        # Per equation, LIS is 1 + max of possible subproblems
        L[i] = 1 + max(subproblems, default=0)
    print(L)
    return max(L, default=0)

l = [5, 2 ,8, 6, 3 ,6, 9, 5]

x = lis(l)
print(x)
