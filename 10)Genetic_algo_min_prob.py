import matplotlib.pyplot as plt


# Encoding function
def encoding(individual):
    return int(individual, 2)


# Decoding function
def decoding(value):
    minR1, maxR1 = 0, 31
    minR2, maxR2 = 0, 2
    return minR2 + (maxR2 - minR2) * (value - minR1) / (maxR1 - minR1)


# Fitness function
def fitness(x):
    return x ** (1 / 6) + (1 / 3 * x)


# Crossover function
def crossover(parent1, parent2):
    child1 = parent1[0] + parent2[1:4] + parent1[4]
    child2 = parent2[0] + parent1[1:4] + parent2[4]
    return child1, child2


# Probability calculation
def probability(value):
    total = sum(value)
    probabilities = [i / total for i in value]
    return probabilities


# Main Function
if __name__ == "__main__":
    # Initial Population
    population = ['10010', '10111', '11110', '01101', '10100', '10101']
    max_generation = 2
    random_numbers = [0.15, 0.30, 0.50, 0.60, 0.75,0.90]
    min_fitness_values = []

    for generation in range(max_generation):
        print(f"\nGeneration {generation + 1} Individuals:")
        decoded_values = []
        fitness_values = []
        cumulative_probabilities = []

        # Evaluate fitness scores for each individual
        for i, individual in enumerate(population):
            encoded_value = encoding(individual)
            decoded_value = decoding(encoded_value)
            fitness_score = fitness(decoded_value)

            print(
                f"Individual {i + 1}: Binary: {individual}, Encoded: {encoded_value}, Decoded: {decoded_value:.2f}, Fitness: {fitness_score:.2f}")

            decoded_values.append(decoded_value)
            fitness_values.append(fitness_score)

        min_fitness_values.append(min(fitness_values))
        probabilities = probability(fitness_values)

        print("\nIndividual Probabilities and Cumulative Probabilities:")
        cumulative_prob = 0
        for i, p in enumerate(probabilities):
            cumulative_prob += p
            cumulative_probabilities.append(cumulative_prob)
            if i == 0:
                interval_start = 0
            else:
                interval_start = cumulative_probabilities[i - 1] + 0.01
            interval_end = cumulative_prob
            print(
                f"Individual {i + 1} : Probability : {p:.2f} , Cummulative_Prob : {cumulative_prob:.2f} , Interval : [{interval_start:.2f}, {interval_end:.2f}]")

        # Sort population based on random numbers and intervals
        sorted_population = []
        for rand_num in random_numbers:
            for i, interval_end in enumerate(cumulative_probabilities):
                if i == 0:
                   interval_start =0
                else:
                    interval_start = cumulative_probabilities[i - 1] + 0.01

                if rand_num <= interval_end and rand_num >= interval_start:
                    sorted_population.append(population[i])
                    break

        # Update population with sorted individuals
        population = sorted_population
        print("\nRandom Value Table :")
        for idx, (individual,rand_no) in enumerate(zip(population, random_numbers)):
            print(f"Random No: {rand_no} , Individual {idx + 1}: {individual}")


        # Create next generation using crossover
        next_generation = []
        for i in range(0, len(population) - 1, 2):
            child1, child2 = crossover(population[i], population[i + 1])
            next_generation.extend([child1, child2])

        # Add the last individual if population size is odd
        if len(population) % 2 != 0:
            next_generation.append(population[-1])

        population = next_generation
        print("\n-----------------------------------------------------------------------\n")

    # Print minimum fitness values across generations
    print("\nMinimum Fitness Value Across Generations:")
    for gen, min_fitness in enumerate(min_fitness_values):
        print(f"Generation {gen + 1}: {min_fitness:.2f}")

    # Plotting the Minimum fitness values across generations
    plt.plot(range(1, max_generation + 1), min_fitness_values, marker='o')
    plt.xlabel('Generation')
    plt.ylabel('Minimum Fitness')
    plt.title('Minimum Fitness for Each Generation')
    plt.grid(True)
    plt.xticks(range(1, max_generation + 1))
    plt.ylim(min(min_fitness_values) - 0.05, max(min_fitness_values) + 0.05)
    plt.show()
