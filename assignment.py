# QUESTION 1
def process(matrix):
  matrix=[list(i) for i in matrix]
  m,p=None,None
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if matrix[i][j]=="m":
        m=[i,j]
      if matrix[i][j]=="p":
        p=[i,j]
  return m,p

matrix=["---","-m-","p--"]
m,p=process(matrix)
print(m,p)
while True:
  print("Down\n" if m[0]-p[0]<0 else "UP\n" if m[0]-p[0]>0 else "", end="")
  m[0] += 1 if m[0]-p[0]<0 else -1 if m[0]-p[0]>0 else 0
  print("Left\n" if m[1]-p[1]>0 else "RIGHT\n" if m[1]-p[1]<0 else "", end="")
  m[1] += -1 if m[1]-p[1]>0 else 1 if m[1]-p[1]<0 else 0
  if m==p:
    break



# QUESTION 2
def simulate(n,m):
  '''Write your code Here'''
  
  if (n<0 and n<=100) or (m<0 and m<=100):
    return ValueError("valid int and less than should be count")

    # Initialize counter for valid outcomes
  valid_outcomes = 0

  # Loop through all possible outcomes of two dice rolls
  for i in range(1, n + 1):
      for j in range(1, m + 1):
          # If the sum of the two rolls equals n, increment counter
          if i + j == n:
              valid_outcomes += 1

  # Calculate probability by dividing valid outcomes by total possible outcomes
  probability = valid_outcomes / (n * m)

  return probability

print(simulate(6,4))

# QUESTION4
def two_sum(nums,target):
    seen={}
    for i in range(len(nums)):
      left=target-nums[i]
      if left in seen:
        return [i,seen[left]]
      seen[nums[i]]=i
    return None

print(two_sum([3, 2, 4], 6))
