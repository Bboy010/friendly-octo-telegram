# This function simulates population growth over a number of generations

def simulate_population_growth(initial_population, growth_rate, generations):
    population = initial_population
    for generation in range(generations):
        population = population * growth_rate
        print(f"Generation {generation + 1}: Population = {population:.2f}")
    return population

simulate_population_growth(100, 1.05, 10)