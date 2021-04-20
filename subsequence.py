# Subsequence alignment algorithm demo

# sequences
# X = 'stopsign'
# Y = 'topssign'
X = 'aabbababbbabbabaaaabbbbababbb'
Y = 'abbbababbbbbbabaaaababbaabbbb'

# penalty costs
gapCost = 1

# x : int, index in X
# y : int, index in Y
# return int, cost of mismatch
def subsequence(x, y, Z=[]):

  # if end of string is reached
  if (x < 0 or y < 0):
    return 0, Z

  # if chars match 
  if (X[x] == Y[y]):
    # take the match
    return subsequence(x-1, y-1, Z + [(x,y)])

  # chars don't match
  else:
    c1, Z1 = subsequence(x, y-1, Z) # gap in Y
    c2, Z2 = subsequence(x-1, y, Z) # gap in X

    # return minimum cost step
    if (c1 <= c2):
      return c1 + gapCost, Z1
    else:
      return c2 + gapCost, Z2

# output sequence
cost, matches = (subsequence(len(X)-1, len(Y)-1))

# visualization
mapX, mapY = {}, {}
for pair in matches:
  mapX[pair[0]] = pair[1]
  mapY[pair[1]] = pair[0]

newX, newY = '', ''
for i in range(len(X)):
  # char in X is matched
  if i in mapX.keys():
    newX += Y[mapX[i]]
  # char in X is skipped
  else:
    newX += '-'
  
  # char in Y is matched
  if i in mapY.keys():
    newY += X[mapY[i]]
  # char in Y is skipped
  else:
    newY += '-'

print("matches: " + str(matches))
print("cost: " + str(cost))
print('X: ' + X)
print('Y: ' + Y)
print('X: ' + newX)
print('Y: ' + newY)