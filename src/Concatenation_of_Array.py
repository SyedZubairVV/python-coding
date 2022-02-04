from sys import builtin_module_names


def getConcatenation(nums):
    bums = nums
    for i in range(0, len(nums)):
        bums.append(nums[i])
    print(bums)
