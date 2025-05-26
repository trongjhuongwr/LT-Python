# Dict
# Write python program:
#  1. Convert two lists into a dictionary
#  2. Merge two Python dictionaries into one
#  3. Print the value of key ‘history’ from the below dict
#  4. Initialize dictionary with default values
#  5. Create a dictionary by extracting the keys from a given dictionary
#  6. Delete a list of keys from a dictionary
#  7. Check if a value exists in a dictionary
#  8. Rename key of a dictionary
#  9. Get the key of a minimum value from the following dictionary
# 10. Change value of a key in a nested dictionary
# 11. Counts the number of times characters appear in a text paragraph.
# 12. Using a dictionary containing keys starting from 1 and values containing prime numbers less than a value N.

# 1. Convert two lists into a dictionary
def ex1():
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    return dict(zip(keys, values))

# 2. Merge two Python dictionaries into one
def ex2():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    return {**dict1, **dict2}  # Hoặc dict1.update(dict2)

# 3. Print the value of key ‘history’
def ex3():
    sample_dict = {
        'class': {
            'student': {
                'name': 'Mike',
                'marks': {
                    'physics': 70,
                    'history': 80
                }
            }
        }
    }
    return sample_dict['class']['student']['marks']['history']

# 4. Initialize dictionary with default values
def ex4():
    keys = ['a', 'b', 'c']
    default = 0
    return dict.fromkeys(keys, default)

# 5. Create a dictionary by extracting keys from a given dict
def ex5():
    original_dict = {'a': 1, 'b': 2, 'c': 3}
    keys = ['a', 'c']
    return {k: original_dict[k] for k in keys}

# 6. Delete a list of keys from a dictionary
def ex6():
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    keys_to_remove = ['a', 'c']
    return {k: v for k, v in sample_dict.items() if k not in keys_to_remove}

# 7. Check if a value exists in a dictionary
def ex7():
    sample_dict = {'a': 1, 'b': 2, 'c': 3}
    return 2 in sample_dict.values()

# 8. Rename key of a dictionary
def ex8():
    sample_dict = {'old_key': 'value'}
    sample_dict['new_key'] = sample_dict.pop('old_key')
    return sample_dict

# 9. Get the key of a minimum value
def ex9():
    sample_dict = {'a': 5, 'b': 2, 'c': 8}
    return min(sample_dict, key=lambda k: sample_dict[k])

# 10. Change value in a nested dictionary
def ex10():
    sample_dict = {
        'emp1': {'name': 'John', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000}
    }
    sample_dict['emp2']['salary'] = 8500
    return sample_dict

# 11. Count character frequencies
def ex11():
    text = "Hello world"
    freq = {}
    for char in text.lower():
        freq[char] = freq.get(char, 0) + 1
    return freq

# 12. Generate prime numbers dictionary
def ex12():
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0: return False
        return True

    N = 20
    primes = [i for i in range(2, N) if is_prime(i)]
    return {i+1: primes[i] for i in range(len(primes))}