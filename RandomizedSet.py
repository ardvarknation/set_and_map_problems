# Solution for LeetCode problem "Insert, Delete, GetRandom in O(1)".
# Description:
#    Implement the RandomizedSet class with following:
#    - RandomizedSet() initializes the RandomizedSet object
#    - bool insert(int val) inserts an item, val, into the set if not present.
#      Returns True if the item was not present, False otherwise.
#    - bool remove(int val) removes an item, val, from the set if present.
#      Returns True if the item was present, False if not.
#    - int getRandom() returns a random element from the current set of 
#      elements. Each element must have the same probability of being returned.
#    The functions of the class must be implemented such that each function works
#    in average O(1) complexity.

import random

class RandomizedSet:

  def __init__(self):
    """
    Initialize a new RandomizedSet object.
    """
    self.values = []      # list to store elements
    self.index_map = {}    # Value -> index mapping in values list

  def insert(self, val: int) -> bool:
    """
    Inserts value into RandomizedSet, returns True if not present, False otherwise.
    """
    if val in self.index_map:
      return False

    self.index_map[val] = len(self.values)
    self.values.append(val)
    return True

  def remove(self, val: int) -> bool:
    """
    Remove item from RandomizedSet, return True if present, False otherwise.
    """
    if val not in self.index_map:
      return False

    # Index of element to remove
    idx = self.index_map[val]

    # Last element in the list
    last_val = self.values[-1]

    # Swap val with last element
    self.values[idx] = last_val
    self.index_map[last_val] = idx

    # Remove last element
    self.values.pop()
    del self.index_map[val]

    return True

  def getRandom(self) -> int:
    """
    Return a random element from RandomizedSet.
    """
    return random.choice(self.values)
