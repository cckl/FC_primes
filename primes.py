class MultiplicationTable:
    """A multiplication table class."""

    def __init__(self):
        """Instantiate an empty multiplication table."""

        self.table = []

    def create_primes_table(self, n):
        """Create a 2D array of n primes and their products."""

        if n == 0:
            print('You\'ve selected 0 primes. Here is a nonexistent table.')
            return '0 primes'
        if not isinstance(n, int) or n < 0:
            raise ValueError('Sorry, that\'s not a valid number of primes. Please try again with an integer greater than 0.')

        n_primes = get_n_primes(n)
        self.table.append(n_primes)

        for i in range(1, len(n_primes)):
            row = []
            row.append(n_primes[i])
            for j in range(1, len(n_primes)):
                row.append(n_primes[i] * n_primes[j])
            self.table.append(row)

    def format_primes_table(self, n):
        """Create a formatted string representation of the primes table."""

        self.create_primes_table(n)
        primes_table_string = ''

        for row in self.table:
            for i in range(len(row)):
                primes_table_string = f"{primes_table_string}{str(row[i])}\t"
            primes_table_string += '\n'
        return primes_table_string


def is_prime(num):
    """Return a boolean of whether num is prime."""

    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_n_primes(n):
    """Return a list of the first n prime numbers."""

    primes = [' ']
    num = 2
    while len(primes) < n + 1:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


if __name__ == '__main__':
    print('* * * * * * * * * *\n')
    print('Funding Circle Coding Challenge\n')
    print('This program prints out a multiplication table of the first 10 prime numbers.')
    print('Try it with another value of n as well.\n')
    print('* * * * * * * * * *\n')

    n = 10
    table = MultiplicationTable()
    result = table.format_primes_table(n)
    print(result)
