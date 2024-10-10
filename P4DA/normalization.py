import numpy as np

class Normalization:
    def __init__(self, values):
        self.values = values
    
    def display_list(self):
        print(f"My list: {self.values}")
    
    def min_max_normalization(self):
        min_val = min(self.values)
        max_val = max(self.values)
        min_max_normalized = [(x - min_val) / (max_val - min_val) for x in self.values]
        return min_max_normalized
    
    def z_score_normalization(self):
        mean_val = np.mean(self.values)
        std_dev = np.std(self.values)
        z_score_normalized = [(x - mean_val) / std_dev for x in self.values]
        return z_score_normalized