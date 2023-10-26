import random


def exploitOnly() -> int:
    # First four days, visit each cafeteria
    # Generate happiness values for each of the four cafeterias
    # Pick the one that returned the best happiness value
    # Visit only that cafeteria for the next 196 days.
    # Each day generate a new happiness value for that cafeteria.
    # Return the total happiness generated over the 200 days
    pass


def exploreOnly() -> int:
    # Visit each cafeteria the same number of times.
    import random
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    # 50 days, visit cafeteria 1 and generate a new happiness value
    for i in range(50):
      n1 = random.normalvariate(7,3)
      sum1 += n1
    # 50 days, visit cafeteria 2 and generate a new happiness value
    for i in range(50):
      n2 = random.normalvariate(4,10)
      sum2 += n2
    # 50 days, visit cafeteria 3 and generate a new happiness value
    for i in range(50):
      n3 = random.normalvariate(10,6)
      sum3 += n3 
    # 50 days, visit cafeteria 4 and generate a new happiness value
    for i in range(50):
      n4 = random.normalvariate(5,2)
      sum4 += n4
    # Return the total happiness generated over the 200 days
    sum = sum1 + sum2 + sum3 + sum4
    return sum


def eGreedy(e=10) -> int:
    # Take input value of e (between 0 and 100)
    # Defaults to 10 if no value is given when the function is called
    # First four days, visit each cafeteria
    # Generate happiness values for each of the four cafeterias
    # Next 196 days pick a cafeteria to visit and generate happiness
    # Visit best-so-far cafeteria 100-e% of the time
    # This means you need to be keeping track of the average happiness
    # generated for each cafeteria for the full 200 days! • Visit random cafeteria e% of the time
    # Return the total happiness generated over the 200 days
    pass


def simulation(t, e=10) -> None:
    # Run a simulation of the three strategies (exploitOnly, exploreOnly, and eGreedy) t times
    # Calculate the average total happiness generated over t trials
    # For eGreedy, be sure to use the e values input into your simulation function!
    # Print the Optimum Happiness followed by a new line
    # For each of the strategies print a header with the strategy name followed by
    # Expected total happiness • Expected regret
    # Simulated total happiness • Simulated regret
    pass
