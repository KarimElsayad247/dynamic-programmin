# boxes can only be stacked on boxes where L1 < L2, W1 < W2
# We want to find the height of the tallest possible stack
def stack(boxes):
    # First, sort the boxes by length (or width) to establish
    # a clear ordering upon which we can base our subproblems.
    # Boxes down the list can carry boxes up the list
    boxes.sort(key=lambda x: x[0])

    # A dictionary that will contain the height of the heighest stack 
    # with a particular box as the base. Initialized as the length of 
    # each box
    heights = {box:box[2] for box in boxes}

    # Then we iterate over all the boxes, starting from the smallest 
    # box which we got by sorting the box list
    for i in range(1, len(boxes)):
        box = boxes[i]  # This is the current box for which we want to 
                        # Figure out the heigest stack with it at the base
        
        # The list of boxes that can be stacked on current box
        # We only need to check out the smaller boxes i.e. boxes
        # earlier in the list. 
        S = [boxes[j] for j in range(i) if canBeStacked(boxes[j], box)]

        # The maximum height of a stack with the current box as its base
        # the height of current box {box[2]} + the height of the heighest stack 
        # with the other box (from the boxes in S) at its base
        heights[box] = box[2] + max([heights[box] for box in S], default=0)

    # the heigest stack is the largest value in the dictionary
    # to figure out what boxes constitute the heighest stack,
    # we can construct a companion dictionary where we keep the track
    # of which box lies over which other box
    return max(heights.values(), default=0)




# Helper function to figure out if a box can be stacked on another
def canBeStacked(top, bottom):
    # true if both width and length of top is smaller than bottom
    return top[0] < bottom[0] and top[1] < bottom[1]


b1 = [(2,3,3), (2,2,4), (4,4,2)]
b2 = [(4,5,3), (2,3,2), (3,6,2), (1,5,4), (2,4,1), (1,2,2)]

x1 = stack(b1)
x2 = stack(b2)

print(x1)
print(x2)
