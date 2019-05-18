# Funding Circle Coding Challenge
This program prints out a multiplication table of the first N prime numbers. The first row and column of the table have N primes, with each cell containing the product of the primes for the corresponding row and column. The program is set up to run with N = 10, although you may change N to any integer value from 0 to much larger numbers.

# Requirements
Python 3 must be installed.

Suggested installation for OSX with Homebrew:
`brew install python3`

# Instructions
Run the program in the terminal to print the multiplication table of the first 10 prime numbers:
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
* `get_n_primes`: creates an array of the first N prime numbers, ensuring it begins with an empty space for the top left corner of the table.
* `is_prime`: a helper function that validates prime numbers.

# Testing
I used Python’s `unittest` testing framework because it is included in the Python standard library, and has a readily available suite of tools. 

When writing unit tests, I considered:
* Testing proper handling of invalid input for N
* Testing that the first row and column of the table were properly populated
* Testing the correct products of primes
* Testing my string representation for tabulation and newline characters in the correct positions
* Testing my prime number functions for validation and generation of the correct prime numbers

When designing my program, I considered how to structure it in a way that would make unit testing easy. This is why I decided to abstract the actual printing of the table from my class methods, and simply print it under `__main__`.  The `format_primes_table` class method returns a string that I can unit test in detail for correct values and formatting.

# Aysymptotic Complexity
## Time
Examples of the actual runtime of the program are as follows:  
N = 10 `0.0004780292510986328s`  
N = 100 `0.0356907844543457s`  
N = 500 `29.098557949066162s`  

* `get_n_primes` and `is_prime`: The runtime of these functions are both O(N), where N = the number of primes; O(N) + O(N).
* `create_primes_table_` and `format_primes_table`: Due to the nested for...in loops in both functions, the runtime of these functions are each O(N^2), where N = the number of primes; O(N^2) + O(N^2).

The overall runtime complexity of the program is 2N + 2(N^2). After ignoring lower order terms and dropping leading constants, the runtime complexity is **O(N^2)**.

## Space
* `get_n_primes`: The space complexity of this function is O(N), where N = the number of primes.
*  `is_prime`: The space complexity is O(1), as it holds no additional data structures.
* `create_primes_table_` and `format_primes_table`: Due to self.table being a 2D array, the space complexity is O(N^2).

After ignoring lower order terms and dropping leading constants, the space complexity is **O(N^2)**.

Overall, as the size of N grows, the program scales in quadratic time and space.
