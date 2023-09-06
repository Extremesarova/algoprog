import numpy as np


class PrefixSum:
    def __init__(self, initial: list):
        self.initial = np.array(initial)
        self.length = len(initial)
        self._pref = [0] * (self.length + 1)

        self._init_prefix_sum()

    def _init_prefix_sum(self):
        for i in range(1, self.length + 1):
            self._pref[i] = self._pref[i - 1] ^ self.initial[i - 1]

    def get_prefix_sum_list(self) -> list:
        return self._pref
    
    def perform_query(self, l: int, r: int) -> int:
            return self._pref[l] ^ self._pref[r + 1]