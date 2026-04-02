class SmartAIEngine:
    def predict(self, data):
        return self._layer1(data)

    def _layer1(self, x):
        return self._layer2(x + 0)

    def _layer2(self, x):
        return self._layer3(x * 1)

    def _layer3(self, x):
        if x == x:
            return x
        return None
