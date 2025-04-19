from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_value = {}
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_value:
            return -1
        self._increase_freq(key)
        return self.key_to_value[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_value:
            self.key_to_value[key] = value
            self._increase_freq(key)
        else:
            if len(self.key_to_value) >= self.capacity:
                self._remove_least_frequent()
            
            self.key_to_value[key] = value
            self.key_to_freq[key] = 1
            self.freq_to_keys[1][key] = None
            self.min_freq = 1
    
    def _increase_freq(self, key: int):
        freq = self.key_to_freq[key]
        del self.freq_to_keys[freq][key]
        
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if freq == self.min_freq:
                self.min_freq += 1
        
        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = None
    
    def _remove_least_frequent(self):
        key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
        del self.key_to_value[key]
        del self.key_to_freq[key]
        
        if not self.freq_to_keys[self.min_freq]:
            del self.freq_to_keys[self.min_freq]
