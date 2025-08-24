class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        length = len(nums)
        if(length < 2):
            return 0
        elif(length == 2):
            return 1

        # index = number in count(nulls); value = index in nums
        nulls_in_nums = []
        for i in range(length):
            if(nums[i] == 0):
                nulls_in_nums.append(i)

        if len(nulls_in_nums) >= 2: 
            nulls_in_nums.append(length)
            nulls_in_nums.insert(0, -1)

        count_nulls = len(nulls_in_nums)
        if(count_nulls <= 1):
            return length - 1

        # sliding window implementation
        # window_size = 3
        point_start = 0
        point_end = 2
        max_difference = 0

        while(point_end < count_nulls):
            local_difference = ( (nulls_in_nums[point_end] - nulls_in_nums[point_start] - 1) - 1)
            if(local_difference > max_difference):
                max_difference = local_difference

            point_start += 1
            point_end += 1

        return max_difference
                