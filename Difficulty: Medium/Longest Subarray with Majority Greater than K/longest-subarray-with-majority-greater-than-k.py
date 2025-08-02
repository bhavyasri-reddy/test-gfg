class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)

        # Step 1: Transform array to +1 / -1
        transformed = [1 if num > k else -1 for num in arr]

        prefix_sum = 0
        max_len = 0
        prefix_map = {}  # prefix_sum -> first index

        for i in range(n):
            prefix_sum += transformed[i]

            # Case 1: If total sum so far is positive, then whole subarray [0...i] is valid
            if prefix_sum > 0:
                max_len = i + 1
            else:
                # Case 2: Check if (prefix_sum - 1) has occurred before
                if (prefix_sum - 1) in prefix_map:
                    max_len = max(max_len, i - prefix_map[prefix_sum - 1])

            # Store the first occurrence of prefix_sum
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i

        return max_len

        