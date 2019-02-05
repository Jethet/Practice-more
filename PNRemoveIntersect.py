# Given the following two sets find the intersection and remove those elements
# from the first set

#firstSet = {10, 30, 40 , 60, 45}
#secondSet = {20, 50, 10 , 40, 55}
# Expected Outcome: firstSet = {30, 60, 45}

firstSet  = {23, 42, 65, 57, 78, 83, 29}
secondSet = {57, 83, 29, 67, 73, 43, 48}
print(firstSet - secondSet)

# outcome: {65, 42, 78, 23}
