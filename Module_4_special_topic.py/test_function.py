"""Modify the simulate_population_growth function to also return the population at each generation in a list.

Add a if condition to make the population plateau after reaching a maximum population of 
10*10**8 cell."""

def simulate_population_growth(initial_population, growth_rate, generations):
    population = initial_population
    if population >= 10*10**8:
        return population
    population_list = []
    for generation in range(generations):
        population = population * growth_rate
        population_list.append(population)
        print(f"Generation {generation + 1}: Population = {population:.2f}")
    return population_list

simulate_population_growth(100, 1.05, 10)
    # for generation in range(generations):
    #     population = population * growth_rate
    #     print(f"Generation {generation + 1}: Population = {population:.2f}")
    # return population

# simulate_population_growth(100, 1.05, 10)