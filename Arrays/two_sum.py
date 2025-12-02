from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    LeetCode Problem: Two Sum (Easy)
    
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.
    
    Approach:
    - Use a hash map (dictionary) to store numbers and their indices.
    - For each number, check if target - number exists in the map.
    - If yes, return the pair of indices.
    
    Time Complexity: O(n)  (single pass through the array)
    Space Complexity: O(n) (hash map storage)
    
    Example:
    >>> two_sum([2,7,11,15], 9)
    [0, 1]
    """
    num_map = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

