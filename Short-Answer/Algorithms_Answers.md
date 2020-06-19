#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
```python
# This is O(1)
 a = 0
 # This loop should run O(n) times
    while (a < n * n * n):
  # a is incremented by n**2 during each loop 
  # also multiplication, addition and assignment isO(1)     
      a = a + n * n

   # Hence the Total time complexity wiil be O(1 + n + 1 )   which equates to O(n)
```

b)

```python
    # This is O(1)
    sum = 0
    # The outer loop runs in O(n) * the complexity of the inner loop
    for i in range(n):
      # This is O(1)
      j = 1
      # j doubles in each iteration, so this loop will run in O(log n)
      while j < n:
        # this is O(1)
        j *= 2
        # This is O(1)
        sum += 1

    # The total time complexity is O(1) + O(n) * (O(log n) * O( 1 + 1))
    #                           == O(1) + O(n) * O(log n)
    #                           == O(n log n)
```

c)
```python
    def bunnyEars(bunnies):
      # This is O(1)
      if bunnies == 0:
        return 0

      # The state of 'bunnies' decreases by 1 on each recursion
      # so bunnyEars will recurse n times
      return 2 + bunnyEars(bunnies-1)

      # The total time complexity is O(1) + O(n)
      #                              == O(n)
```


## Exercise II
In my opinion the the best and most efficient approach is to apply the Binary Search  Tree  Concept.
The building floors are considered as a sorted array which is a basic requirement of a binary search.
Then follow theis approach :
 1. Initialize the lowest floor to 1 and the highest floor as n
 2. Set "f" as (lowest floor + highest floor) // 2
 3. Go to "f" and throw an egg
 4. If the egg breaks:
    4a. Go one floor below and throw an egg
   4b. If the egg does not break, return f
   4c. If the egg does break, we're too high. Set the max floor to f
   4d. Go back to step 1
5. If the egg doesn't break:
   5a. We're too low. Set the min floor to f
   5d. Go back to step 1
 
 RunTime: This should be O(log n) This is because it's basically a binary search whereby at each iteration we are halving
 the remaining number of floors



