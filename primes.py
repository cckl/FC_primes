class MultiplicationTable:
    """A multiplication table class."""

    def __init__(self):
        """Instantiate an empty multiplication table."""

        self.table = []

    def create_primes_table(self, n):
        """Create a 2D array of n primes and their products."""

        # validate n
        if n == 0:
            print('You\'ve selected 0 primes. Here is a nonexistent table.')
        if not isinstance(n, int) or n < 0:
            print('Sorry, that\'s not a valid number of primes.')
            print('Please try again with an integer greater than 0.')
        else:
            # generate first row of table of n primes
            n_primes = get_n_primes(n)
            self.table.append(n_primes)

            for i in range(1, len(n_primes)):
                row = []
                row.append(n_primes[i])
                for j in range(1, len(n_primes)):
                    product = int(n_primes[i]) * int(n_primes[j])
                    row.append(str(product))
                self.table.append(row)

    def print_primes_table(self, n):
        """Print the multiplication table to stdout."""

        primes_table = self.create_primes_table(n)
        for row in self.table:
            print('\t'.join(row))


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
            primes.append(str(num))
        num += 1
    return primes


if __name__ == '__main__':
    print('* * * * * * * * * *\n')
    print('Funding Circle Coding Challenge\n')
    print('This program prints out a multiplication table of the first 10 prime numbers.')
    print('Try it with another value of n as well.\n')
    print('* * * * * * * * * *\n')

    n = 8
    table = MultiplicationTable()
    table.print_primes_table(n)
