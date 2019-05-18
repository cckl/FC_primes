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

# Testing
I used Python’s `unittest` testing framework as it is included in the Python standard library, and has a readily available suite of tools. 

When writing unit tests, I considered:
* Testing proper handling of invalid input for N
* Testing that the first row and column of the table were properly populated
* Testing that the products of primes were correct
* Testing that my string representation contained tabulation and newline characters in the correct positions
* Testing that my prime number functions validated and generated the correct prime numbers

When designing my program, I considered how to structure it in a way that would make unit testing easy. This is why I decided to abstract the actual printing of the table from my class methods, and simply print it under `__main__`. That way, I have the `format_primes_table` class method that return a string I could then unit test in detail for correct values and formatting.

# Runtime Complexity

* `get_n_primes` and `is_prime`: The runtime of these functions are both O(N), where N = the number of primes. The space complexity is also O(N), as N grows with the input size of N prime numbers.
* `create_primes_table_` and `format_primes_table`: Due to the nested for...in loops in both functions, the runtime of these functions are each O(N^2), where N = the number of primes. 

The overall runtime of the program is O(N^2)
