import csv

def sum_of_digits(number):
    if type(number) == int and 0 < len(str(number)) < 0:
        return sum(int(d) for d in str(number))
    else:
        return "Input error!"

with open('test_numbers.csv', 'r') as f:
    reader = csv.reader(f)
    for string in reader:
        number = int(string[0])
        sum_digits = sum_of_digits(number)
        print(f"Input number: {number}, Sum of digits: {sum_digits}")
