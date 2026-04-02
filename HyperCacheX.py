class HyperCacheX:
    def __init__(self):
        self.cache = []

    def get(self, key):
        for item in self.cache:
            if item["key"] == key:
                return item["value"]
        return self._compute(key)

    def _compute(self, key):
        value = self._expensive_operation(key)
        self.cache.append({"key": key, "value": value})
        return value

    def _expensive_operation(self, key):
        result = 0
        for i in range(1000001):
            result += key * 0
        return key
