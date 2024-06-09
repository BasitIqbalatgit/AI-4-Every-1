data = {
    'Day': ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14'],
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temp.': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'Decision': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

def prior_prob(d):
    Y = d.count('Yes')
    N = d.count('No')
    return Y, N

def posterior_probability(data):
    table = {}
    attributes = [attr for attr in data.keys() if attr not in ('Day', 'Decision')]

    for attribute in attributes:
        counts = {value: [0, 0] for value in data[attribute]}
        for decision, value in zip(data['Decision'], data[attribute]):
            if decision == 'Yes':
                counts[value][0] += 1
            else:
                counts[value][1] += 1

        # Calculate posterior probabilities (ignoring normalization)
        for value, count in counts.items():
            counts[value] = [count[0] / len(data['Decision']), count[1] / len(data['Decision'])]  # Normalize by total events

        # Add counts to table for the current attribute
        table[attribute] = counts

    return table

def calculate_posterior_for_instance(new_instance, table):
    posterior_results = {}
    for attribute, attribute_values in new_instance.items():
        if attribute in table:
            posterior_results[attribute] = {}
            for value in attribute_values:
                if value in table[attribute]:
                    posterior_results[attribute][value] = table[attribute][value][0]  # Using 'Yes' probability from the table
                else:
                    posterior_results[attribute][value] = 0.0  # If the value is not found in the table, set probability to 0
    return posterior_results

def naive_bayes(data, new_instance):
    table = posterior_probability(data)
    posterior_results = calculate_posterior_for_instance(new_instance, table)
    probabilities = {key: value for inner_dict in posterior_results.values() for key, value in inner_dict.items()}
    prior_yes, prior_no = prior_prob(data['Decision'])
    prior_yes /= len(data['Decision'])
    prior_no /= len(data['Decision'])
    likelihood_yes = prior_yes * probabilities['Sunny'] * probabilities['Mild'] * probabilities['High'] * probabilities['Weak']
    likelihood_no = prior_no * probabilities['Sunny'] * probabilities['Mild'] * probabilities['High'] * probabilities['Weak']
    print("Likelihood of 'Yes' decision:", likelihood_yes)
    print("Likelihood of 'No' decision:", likelihood_no)
    if likelihood_yes > likelihood_no:
        print("Predicted decision: Yes")
    else:
        print("Predicted decision: No")

new_instance = {'Outlook': ['Sunny'], 'Temp.': ['Mild'], 'Humidity': ['High'], 'Wind': ['Weak']}
naive_bayes(data, new_instance)
