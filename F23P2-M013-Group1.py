import random
import statistics

total_days = 200
happiness_value = [7, 4, 10, 5]
deviation_values = [3, 10, 6, 2]
optimum_happiness = max(happiness_value) * total_days


def exploitOnly() -> float:
    total = 0
    visit_c1 = random.normalvariate(7, 3)  # creates random happiness level for first cafeteria - 1st day
    visit_c2 = random.normalvariate(4, 10)  # creates random happiness level for second cafeteria - 2nd day
    visit_c3 = random.normalvariate(10, 6)  # creates random happiness level for third cafeteria - 3rd day
    visit_c4 = random.normalvariate(5, 2)  # creates random happiness level for fourth cafeteria - 4th day
    max_happiness = max(visit_c1, visit_c2, visit_c3, visit_c4)  # takes max happiness level between 4 cafeterias
    # adds happiness levels for first 4 days to sum
    total += visit_c1
    total += visit_c2
    total += visit_c3
    total += visit_c4

    # if c1 has max happiness value, go to c1 next 196 days and add happiness levels for each day to sum
    if max_happiness == visit_c1:
        for i in range(196):
            total += random.normalvariate(7, 3)

    # if c2 has max happiness value, go to c2 next 196 days and add happiness levels for each day to sum
    elif max_happiness == visit_c2:
        for i in range(196):
            total += random.normalvariate(4, 10)

    # if c3 has max happiness value, go to c3 next 196 days and add happiness levels for each day to sum
    elif max_happiness == visit_c3:
        for i in range(196):
            total += random.normalvariate(10, 6)

    # if c4 has max happiness value, go to c4 next 196 days and add happiness levels for each day to sum
    elif max_happiness == visit_c4:
        for i in range(196):
            total += random.normalvariate(5, 2)

    return total


def exploreOnly() -> float:
    # Visit each cafeteria the same number of times.
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    # 50 days, visit cafeteria 1 and generate a new happiness value
    for i in range(50):
        n1 = random.normalvariate(happiness_value[0], deviation_values[0])
        sum1 += n1
    # 50 days, visit cafeteria 2 and generate a new happiness value
    for i in range(50):
        n2 = random.normalvariate(happiness_value[1], deviation_values[1])
        sum2 += n2
    # 50 days, visit cafeteria 3 and generate a new happiness value
    for i in range(50):
        n3 = random.normalvariate(happiness_value[2], deviation_values[2])
        sum3 += n3
        # 50 days, visit cafeteria 4 and generate a new happiness value
    for i in range(50):
        n4 = random.normalvariate(happiness_value[3], deviation_values[3])
        sum4 += n4
    # Return the total happiness generated over the 200 days
    total = sum1 + sum2 + sum3 + sum4
    return total


def eGreedy(e=10) -> float:
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
    c1 = random.normalvariate(m1, d1)
    # visit cafeteria 2
    c2 = random.normalvariate(m2, d2)
    # visit cafeteria 3
    c3 = random.normalvariate(m3, d3)
    # visit cafeteria 4
    c4 = random.normalvariate(m4, d4)
    total_happiness = c1 + c2 + c3 + c4
    if c1 > c2 and c1 > c3 and c1 > c4:
        best_mean = m1
        best_dev = d1
    elif c2 > c1 and c2 > c3 and c2 > c4:
        best_mean = m2
        best_dev = d2
    elif c3 > c1 and c3 > c2 and c3 > c4:
        best_mean = m3
        best_dev = d3
    else:
        best_mean = m4
        best_dev = d4
    day = 1
    cafe1 = 1
    cafe2 = 1
    cafe3 = 1
    cafe4 = 1
    for i in range(196):
        r = random.random()
        if r < (e / 100):
            # pick random
            which_one = random.randint(1, 4)
            if which_one == 1:
                day_happiness = random.normalvariate(m1, d1)
                c1 += day_happiness
                cafe1 += 1
            elif which_one == 2:
                day_happiness = random.normalvariate(m2, d2)
                c2 += day_happiness
                cafe2 += 1
            elif which_one == 3:
                day_happiness = random.normalvariate(m3, d3)
                c3 += day_happiness
                cafe3 += 1
            else:
                day_happiness = random.normalvariate(m4, d4)
                c4 += day_happiness
                cafe4 += 1

        else:
            day_happiness = random.normalvariate(best_mean, best_dev)
        avg_hap1 = c1 / cafe1
        avg_hap2 = c2 / cafe2
        avg_hap3 = c3 / cafe3
        avg_hap4 = c4 / cafe4
        if avg_hap1 > avg_hap2 and avg_hap1 > avg_hap3 and avg_hap1 > avg_hap4:
            best_mean = m1
            best_dev = d1
        elif avg_hap2 > avg_hap1 and avg_hap2 > avg_hap3 and avg_hap2 > avg_hap4:
            best_mean = m2
            best_dev = d2
        elif avg_hap3 > avg_hap1 and avg_hap3 > avg_hap2 and avg_hap3 > avg_hap4:
            best_mean = m3
            best_dev = d3
        elif avg_hap4 > avg_hap1 and avg_hap4 > avg_hap3 and avg_hap4 > avg_hap2:
            best_mean = m4
            best_dev = d4
        total_happiness += day_happiness
        day += 1
    return total_happiness


def simulation(t: int, e=10) -> None:
    # Make a list of the simulated values for each trial
    exploit_only = []
    explore_only = []
    e_greedy = []

    # Simulate the three strategies (exploitOnly, exploreOnly, and eGreedy) t times & ADD VALUES TO LIST
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
    print("Expected Regret: " + str("%.2f" % expr_expected_regret))
    print("Simulated Happiness: " + str("%.2f" % expr_simulated_happiness))
    print("Simulated Regret: " + str("%.2f" % expr_simulated_regret))
    print()

    print("Exploit Only: ")
    print("Expected Happiness: " + str("%.2f" % expl_expected_happiness))
    print("Expected Regret: " + str("%.2f" % expl_expected_regret))
    print("Simulated Happiness: " + str("%.2f" % expl_simulated_happiness))
    print("Simulated Regret: " + str("%.2f" % expl_simulated_regret))
    print()

    print("eGreedy: ")
    print("Expected Happiness: " + str("%.2f" % grd_expected_happiness))
    print("Expected Regret: " + str("%.2f" % grd_expected_regret))
    print("Simulated Happiness: " + str("%.2f" % grd_simulated_happiness))
    print("Simulated Regret: " + str("%.2f" % grd_simulated_regret))
