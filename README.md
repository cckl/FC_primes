# Funding Circle Coding Challenge
This program prints out a multiplication table of the first N prime numbers. The first row and column of the table have N primes, with each cell containing the product of the primes for the corresponding row and column. The program is set up to run with N = 10, although you may change N to any integer value from 0 to much larger numbers.

# Requirements
Python 3 must be installed.

Suggested installation for OSX with Homebrew:
`brew install python3`

# Instructions
Run the program in the terminal and see the multiplication table of the first 10 prime numbers printed to stdout:
`python3 primes.py`

Run the test file:
`python3 tests.py`

To run the program with a custom N input, open the `primes.py` file in your text editor of choice. On line 71, under `if __name__ == '__main__':`, you may change the N value here.

# Process
I first considered the format of my output table and the data structures needed. A 2D array, or matrix, was the obvious choice in creating a representation of a table. I would then use string formatting and tab spacing for ease of readability when printing the table to stdout. 

I took an object-oriented approach to writing the program. `primes.py` consists of a MultiplicationTable class with three class methods:
* `__init__`: instantiates an empty array for the primes table.
* `create_primes_table`: calls external functions to generate prime numbers and populates the 2D array with their products.
* `format_primes_table`: creates a string representation of the 2D array with proper tab and newline spacing so the printed output is easily readable.

The class methods of MultiplicationTable utilize two standalone functions:
* `get_n_primes`: creates an array of the first N primes numbers, ensuring it begins with an empty space ' '.
* `is_prime`: a helper function that validates prime numbers.
