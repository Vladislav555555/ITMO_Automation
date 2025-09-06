def count_positive(numbers: list[float]) -> int:

    count = 0
    for num in numbers:
        if num > 0:
            count += 1
    return count
nums = []
for i in range(5):
    n = float(input(f"Введите число {i+1}: "))
    nums.append(n)
positive_count = count_positive(nums)
print(f"Количество положительных чисел: {positive_count}")