'''The while Loop
With the while loop we can execute a set of statements as long as a condition is true.'''
#####1
i = 1
while i < 6:
  print(i)
  i += 1  #Note: remember to increment i, or else the loop will continue forever.
#########2 The break Statement - With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
#######3   The continue Statement ---------- With the continue statement we can stop the current iteration, and continue with the next:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Note that number 3 is missing in the result

