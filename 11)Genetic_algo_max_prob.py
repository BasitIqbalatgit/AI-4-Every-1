# Assalam u alikum sir !!
# sir i have written this code in pycharm  and not in Ananconda ..........Thank You..


import matplotlib.pyplot as plt

# Encoding function to convert binary string to integer
def encoding(individual):
    return int(individual, 2)

# Decoding function to scale integer value to a specified range
def decoding(value):
    minR1, maxR1 = 0, 31
    minR2, maxR2 = 0, 2
    return minR2 + (maxR2 - minR2) * (value - minR1) / (maxR1 - minR1)

# Fitness function
def fitnessFunc(x):
    return -(x**2) + (2*x)

# Crossover function to generate two children from two parents
def crossOverFunc(parent1, parent2):
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
    population = ['11010', '00111', '10110', '00101']
    max_generation = 2
    random_numbers =  [0.4, 0.15, 0.7, 0.9]
    max_fitness_values = []

    for generation in range(max_generation):
        print(f"\nGeneration {generation + 1} Individuals:")
        decoded_values = []
        fitness_values = []
        cumulative_probabilities = []

        # Evaluate fitness scores for each individual
        for i, individual in enumerate(population):
            encoded_value = encoding(individual)
            decoded_value = decoding(encoded_value)
            fitness_score = fitnessFunc(decoded_value)

            print(
                f"Individual {i + 1}: Binary: {individual}, Encoded: {encoded_value}, Decoded: {decoded_value:.2f}, Fitness: {fitness_score:.2f}")

            decoded_values.append(decoded_value)
            fitness_values.append(fitness_score)

        max_fitness_values.append(max(fitness_values))
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
            child1, child2 = crossOverFunc(population[i], population[i + 1])
            next_generation.extend([child1, child2])

        # Add the last individual if population size is odd
        if len(population) % 2 != 0:
            next_generation.append(population[-1])

        population = next_generation
        print("\n-----------------------------------------------------------------------\n")

    # Print maximum fitness values across generations
    print("\nMaximum Fitness Value Across Generations:")
    for gen, max_fitness in enumerate(max_fitness_values):
        print(f"Generation {gen + 1}: {max_fitness:.2f}")

    # Plotting the Maximum fitness values across generations
    plt.plot(range(1, max_generation + 1), max_fitness_values, marker='o')
    plt.xlabel('Generation')
    plt.ylabel('Maximum Fitness')
    plt.title('Maximum Fitness for Each Generation')
    plt.grid(True)
    plt.xticks(range(1, max_generation + 1))
    plt.ylim(min(max_fitness_values) - 0.05, max(max_fitness_values) + 0.05)
    plt.show()
