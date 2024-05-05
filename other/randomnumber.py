import random
def generate_random_value():
    # Generate random values for each part of the format
    num1 = random.randint(1, 4)
    num2 = random.randint(1, 10000)
    num3 = random.randint(1, 10000)
    # Format the numbers as per the given format
    random_value = f"{num1}, {num2}, {num3}"
    return random_value

def main():
    # Generate and store three random values
    random_values = [generate_random_value() for _ in range(10000)]
    
    # Write the generated values to a text file
    with open("random_values.txt", "w") as file:
        for value in random_values:
            file.write(value + "\n")
    
    print("Random values have been stored in 'random_values.txt'.")

if __name__ == "__main__":
    main()
