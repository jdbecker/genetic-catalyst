FIB_NUMS = [0, 1]


def fibonacci(index: int) -> int:
    while len(FIB_NUMS) < index + 1:
        FIB_NUMS.append(FIB_NUMS[-1] + FIB_NUMS[-2])
    return FIB_NUMS[index]


def fibonacci_shift(index: int) -> int:
    return fibonacci(index + 1)
