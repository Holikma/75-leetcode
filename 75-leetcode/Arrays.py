def twoSum(nums, target):
    m = {}
    for i in range(len(nums)):
        remainder = target - nums[i]
        if remainder in m:
            return [m[remainder],i]
        m[nums[i]] = i

def main():
    print(twoSum([3,2,4], 6)) 
    return 0

if __name__ == "__main__":
    main()
