class SparseArrays:

    def __init__(self, strings, queries):
        self.strings = strings
        self.queries = queries

    # Brute Force, Time Complexity: O(n^2)
    def count_frequency_brute_force(self):
        # Corner Cases
        if self.strings is None or self.queries is None or len(self.strings) == 0 or len(self.queries) == 0:
            return {}

        res = dict({x: 0 for x in self.queries})

        for eachQuery in set(self.queries):  # Remove all duplicated elements. For example: queries = ['abc','abc','ab']
            for eachString in self.strings:
                if eachString == eachQuery:  # If current string is equal to current query
                    res[eachString] += 1
        return res

    # Use Python inner function List.count(), Time Complexity: O(n^2)
    def count_frequency_inner_func(self):
        # Corner Cases
        if self.strings is None or self.queries is None or len(self.strings) == 0 or len(self.queries) == 0:
            return {}

        res = dict()
        for eachQuery in set(self.queries):
            res[eachQuery] = self.strings.count(eachQuery)

        return res

    # Use hash_map in order to reduce Time Complexity from O(n^2) to O(n)
    def count_frequency_optimization(self):
        # Corner Cases
        if self.strings is None or self.queries is None or len(self.strings) == 0 or len(self.queries) == 0:
            return {}

        # Initial a dict for result with queries' keywords
        res = dict({x: 0 for x in self.queries})

        for eachString in self.strings:
            if res.get(eachString) is not None: # If current string is found in queries
                res[eachString] += 1

        return res
