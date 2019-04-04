import scipy
from scipy import io
import numpy as np
import pdb #  pdb.set_trace()

class Node:
    def __init__(self, depth, points, split_rule=None, left_child=None, right_child=None, label = None):
        # Split on feature 2, with threshold 3
        self.depth = depth
        self.points = points
        self.split_rule = split_rule
        self.left_child = left_child
        self.right_child = right_child
        self.label = label

    def next_node(self, sample):
        # leaf node value
        if self.label is not None:
            return self.label

        # pdb.set_trace()
        sample_feature_value = sample[self.split_rule[0]]
        if sample_feature_value < self.split_rule[1]:
            return self.left_child
        else:
            return self.right_child