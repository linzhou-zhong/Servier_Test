import os
import sys
from SparseArrays import *


def main():
    try:
        # Uncomment this part if you test without Docker
#         if os.environ.get("STRINGS_INPUT") is None:
#             os.environ["STRINGS_INPUT"] = "ab,abc,ab"

        # If Environment Variable 'STRINGS_INPUT' doesn't exist
        if os.environ.get("STRINGS_INPUT") is None:
            raise KeyError

        # If Standard Input missed some positional arguments
        if len(sys.argv) != 2:
            raise TypeError

        # Split strings and queries by comma and remove space
        _strings = os.environ.get("STRINGS_INPUT").strip().split(',')
        _queries = sys.argv[1].split(',')

    except Exception as e:
        # Cannot find correct Environment Variable
        if type(e) is KeyError:
            sys.stdout.write("Environment variable '{}' doesn't exist".format("STRINGS_INPUT"))
        # Standard Input with a bad number of positional arguments
        if type(e) is TypeError:
            sys.stdout.write("Main class takes only 1 positional argument divided by comma but {} was given".format(
                len(sys.argv) - 1))
        # Print out other types of Exception
        else:
            sys.stdout.write(str(e))
        exit()  # Exit programme

    # Initial SpareArrays class, passing strings and queries as two parameters to it's constructor
    sa = SparseArrays(strings=_strings, queries=_queries)
    res = str(sa.count_frequency_brute_force())
    sys.stdout.write(res)


if __name__ == '__main__':
    main()
