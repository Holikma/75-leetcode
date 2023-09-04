def containsDuplicate(nums: list[int]) -> bool:
    if len(nums) == len(set(nums)):
        return False
    return True

nums = [1,1,1,3,3,4,3,2,4,2]

containsDuplicate(nums)
