class DP:
    @staticmethod
    def drop_two_eggs(n):
        """Finds optimal worst numbers of trials for dropping 2 eggs to test floor n
        """

        mem_list = [0] * (n+1)
        mem_list[0] = 0
        mem_list[1] = 1

        for k in range(2, n+1):
            trials_list = []
            for i in range(1, k+1):
                # test on ith floor
                success_worst_trials = mem_list[k - i]
                fail_worst_trials = i - 1
                trials_list.append(1 + max(success_worst_trials, fail_worst_trials))
            mem_list[k] = min(trials_list)


        return mem_list

    @staticmethod
    def rod_profit_max(n, prices):
        """Gest maximum profits in cutting rod.

        Parameters
        ----------
            n: int
                length of the rod
            prices: list
                ith item is the price of length i
        """
        if n != len(prices) + 1:
            raise ValueError('n must be len(prices)+1')

        profits_list = [0] * (n+1)
        profits_list[0] = 0

        for k in range(1, n+1):
            profits_trials = []
            profits_trials.append(prices[k])
            for cut in range(1, k):
                profits_trials.append(prices[k - cut] + prices[cut])
            profits_list[k] = max(profits_trials)

        return profits_list

class FibMem:
    """ Fibonacci using memoization """
    def __init__(self, n):
        self.mem = [-1] * n
        self.capacity = n


    def get_value(self, k):
        if k > self.capacity:
            raise ValueError(f'Exceeding capacity {self.capacity}')

        idx = k - 1
        if idx <= 1:
            self.mem[idx] = 1
            return self.mem[idx]

        if self.mem[idx] == -1:
            self.mem[idx] = self.get_value(k-1) + self.get_value(k-2)

        return self.mem[idx]
