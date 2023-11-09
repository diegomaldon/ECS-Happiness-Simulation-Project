import random
import statistics


total_days = 200
happiness_value = [7, 4, 10, 5]
deviation_values = [3, 10, 6, 2]
optimum_happiness = max(happiness_value) * total_days


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
 # mean and deviation c1
    m1 = 7
    d1 = 4
    # mean and deviation c2
    m2 = 4
    d2 = 10
    # mean and deviation c3
    m3 = 10
    d3 = 6
    # mean and deviation c4
    m4 = 5
    d4 = 2
    # visit cafeteria 1
    c1 = rand.normalvariate(m1, d1)
    # visit cafeteria 2
    c2 = rand.normalvariate(m2, d2)
    # visit cafeteria 3
    c3 = rand.normalvariate(m3, d3)
    # visit cafeteria 4
    c4 = rand.normalvariate(m4, d4)
    total_happiness = c1 + c2 + c3 + c4
    if c1 > c2 and c1 > c3 and c1 > c4:
        Best_Mean = m1
        Best_Dev = d1
    elif c2 > c1 and c2 > c3 and c2 > c4:
        Best_Mean = m2
        Best_Dev = d2
    elif c3 > c1 and c3 > c2 and c3 > c4:
        Best_Mean = m3
        Best_Dev = d3
    else:
        Best_Mean = m4
        Best_Dev = d4
    day = 1
    cafe1 = 1
    cafe2 = 1
    cafe3 = 1
    cafe4 = 1
    for i in range(196):
        r = rand.random(0, 1)
        if r < (e / 100):
            # pick random
            which_one = rand.randint(1, 4)
            if which_one == 1:
                dayhappiness = rand.normalvariate(m1, d1)
                c1 += dayhappiness
                cafe1 += 1
            elif which_one == 2:
                dayhappiness = rand.normalvariate(m2, d2)
                c2 += dayhappiness
                cafe2 += 1
            elif which_one == 3:
                dayhappiness = rand.normalvariate(m3, d3)
                c3 += dayhappiness
                cafe3 += 1
            else:
                dayhappiness = rand.normalvariate(m4, d4)
                c4 += dayhappiness
                cafe4 += 1

        else:
            dayhappiness = rand.normalvariate(Best_Mean, Best_Dev)
        avghap1 = c1 / cafe1
        avghap2 = c2 / cafe2
        avghap3 = c3 / cafe3
        avghap4 = c4 / cafe4
        if avghap1 > avghap2 and avghap1 > avghap3 and avghap1 > avghap4:
            Best_Mean = m1
            Best_Dev = d1
        elif avghap2 > avghap1 and avghap2 > avghap3 and avghap2 > avghap4:
            Best_Mean = m2
            Best_Dev = d2
        elif avghap3 > avghap1 and avghap3 > avghap2 and avghap3 > avghap4:
            Best_Mean = m3
            Best_Dev = d3
        elif avghap4 > avghap1 and avghap4 > avghap3 and avghap4 > avghap2:
            Best_Mean = m4
            Best_Dev = d4
        total_happiness += dayhappiness
        day += 1
    return total_happiness


def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def simulation(t: int, e=10) -> None:
    # Make a list of the simulated values for each trial
    exploit_only = []
    explore_only = []
    e_greedy = []

# Run a simulation of the three strategies (exploitOnly, exploreOnly, and eGreedy) t times & ADD VALUES TO LIST
    for i in range(t):
        val_of_exploit = exploitOnly()
        exploit_only.append(val_of_exploit)

        val_of_explore = exploreOnly()
        explore_only.append(val_of_explore)

        val_of_e_greedy = eGreedy(e)
        e_greedy.append(val_of_e_greedy)

# Calculate the average total happiness generated over t trials
    avg_exploit_only = statistics.mean(exploit_only)
    avg_explore_only = statistics.mean(explore_only)
    avg_e_greedy = statistics.mean(e_greedy)

# Calculate expected and simulated values:
    expr_expected_happiness = (50 * (happiness_value[0] + happiness_value[1] + happiness_value[2] + happiness_value[3]))
    expr_expected_regret = optimum_happiness - expr_expected_happiness
    expr_simulated_happiness = avg_explore_only
    expr_simulated_regret = optimum_happiness - expr_simulated_happiness

    expl_expected_happiness = ((196 * max(happiness_value))
                               + happiness_value[0] + happiness_value[1] + happiness_value[2] + happiness_value[3])
    expl_expected_regret = optimum_happiness - expl_expected_happiness
    expl_simulated_happiness = avg_exploit_only
    expl_simulated_regret = optimum_happiness - expl_simulated_happiness

    grd_expected_happiness = (((((100 - e) / 100) * total_days) * max(happiness_value))
                              + (((e / 400) * total_days) * happiness_value[0])
                              + (((e / 400) * total_days) * happiness_value[1])
                              + (((e / 400) * total_days) * happiness_value[2])
                              + (((e / 400) * total_days) * happiness_value[3]))
    grd_expected_regret = optimum_happiness - grd_expected_happiness
    grd_simulated_happiness = avg_e_greedy
    grd_simulated_regret = optimum_happiness - grd_simulated_happiness


# Print expected and simulated values (rounded to 2 decimal places) for each method
    print("Optimum Happiness: " + str("%.2f" % optimum_happiness))
    print()

    print("Explore Only: ")
    print("Expected Happiness: " + str("%.2f" % expr_expected_happiness))
    print("Expected Regret: " + str(truncate(expr_expected_regret, 2)))
    print("Simulated Happiness: " + str(truncate(expr_simulated_happiness, 2)))
    print("Simulated Regret: " + str(truncate(expr_simulated_regret, 2)))
    print()

    print("Exploit Only: ")
    print("Expected Happiness: " + str("%.2f" % expl_expected_happiness))
    print("Expected Regret: " + str(truncate(expl_expected_regret, 2)))
    print("Simulated Happiness: " + str(truncate(expl_simulated_happiness, 2)))
    print("Simulated Regret: " + str(truncate(expl_simulated_regret, 2)))
    print()

    print("eGreedy: ")
    print("Expected Happiness: " + str("%.2f" % grd_expected_happiness))
    print("Expected Regret: " + str(truncate(grd_expected_regret, 2)))
    print("Simulated Happiness: " + str(truncate(grd_simulated_happiness, 2)))
    print("Simulated Regret: " + str(truncate(grd_simulated_regret, 2)))
