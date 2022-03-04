class PrefixSum:
    def __init__(self, initial: list):
        self.initial = initial
        self.length = len(initial)

        self._init_prefix_sum()

    def _init_prefix_sum(self):
        self._prefix_sum = [0] * (self.length + 1)
        for i in range(1, self.length + 1):
            self._prefix_sum[i] = self._prefix_sum[i - 1] + self.initial[i - 1]

    def get_prefix_sum_list(self) -> list:
        return self._prefix_sum

