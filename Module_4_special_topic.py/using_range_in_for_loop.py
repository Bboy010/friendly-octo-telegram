initial_population = 100

growth_rate = 1.05  # 5% growth per generation



for generation in range(1, 11):

    population = initial_population * (growth_rate ** generation)

    print(f"Generation {generation}: {population:.2f}")

#function 11