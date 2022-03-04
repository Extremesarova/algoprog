class SuffixSum:
    def __init__(self, initial: list):
        self.initial = initial
        self.length = len(initial)

        self._init_suffix_sum()

    def _init_suffix_sum(self):
        self._suffix_sum = [0] * (self.length + 1)
        for i in range(self.length - 1, -1, -1):
            self._suffix_sum[i] = self._suffix_sum[i + 1] + self.initial[i]

    def get_suffix_sum_list(self) -> list:
        return self._suffix_sum

