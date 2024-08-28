import statistics

numbers=[4,4,5,5,5,5,5,7,9,0]

def mean(nums):
  return statistics.mean(nums)    
def median(nums):
    return statistics.median(nums)
def Mode(nums):
    return statistics.mode(nums)
print(mean(numbers))
print(median(numbers))
print(Mode(numbers))