# Create a function that finds the maximum range of a triangles third edge.

def nextEdge(side1, side2):
    return (side1 + side2) - 1

print(nextEdge(8, 10)) # 17
print(nextEdge(5, 7)) # 11
print(nextEdge(9, 2)) # 10
