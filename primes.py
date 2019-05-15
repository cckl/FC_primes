
class MultiplicationTable():

    def __init__(self):
        """Instantiates an empty multiplication table."""
        self.table = []

    def get_n_input(self):
        """Gets the specified input of n prime numbers from the user."""
        n = input("How many prime numbers would you like in the multiplication table? ")
        try:
            n = int(n)
            return n
        except:
            print('Sorry, that\'s not a valid integer. Please restart the program.')

    def create_primes_table(self, n_primes):
        """Generates a 2D array of n primes and their products."""

        # n = self.get_n_input()
        n_primes = get_n_primes(10)

        table = []
        table.append(n_primes)

        for i in range(1, len(n_primes)):
            row = []
            row.append(n_primes[i])
            for j in range(1, len(n_primes)):
                row.append(str(int(n_primes[i]) * int(n_primes[j])))
            table.append(row)

        return table

    def print_primes_table(self, n_primes):
        """Prints the mulitplication table of n prime numbers to stdout."""

        primes_table = self.create_primes_table(n_primes)

        for row in primes_table:
            print('\t'.join(row))



def is_prime(num):
    """Returns a boolean of whether the given number is prime."""

    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_n_primes(n):
    """Returns a list of the first n prime numbers."""

    primes = [' ']
    num = 2

    while len(primes) < n + 1:
        if is_prime(num):
            primes.append(str(num))
        num += 1

    return primes


if __name__ == '__main__':
    print("* * * * * * * * * *")
    print("\nFunding Circle Coding Challenge")
    print("\nThis program prints out a multiplication table of the first 10 prime numbers. Try it with your own input as well!")
    print("\n\n* * * * * * * * * *")
    table = MultiplicationTable()
    table.print_primes_table(10)
    # custom_table = MultiplicationTable()
    # custom_table.print_primes_table()
