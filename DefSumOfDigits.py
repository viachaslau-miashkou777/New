import csv

def sum_of_digits(number):
    if type(number) == int and 1 <= len(str(number)) <= 10:
        return sum(int(d) for d in str(number))
    else:
        return "Input error!"

with open('test_numbers.csv', 'r') as f:
    reader = csv.reader(f)
    for string in reader:
        num = int(string[0])
        sum = sum_of_digits(num)
        print(f"Input number: {num}, Sum of digits: {sum}")
