# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.


def binary_search(array, number) -> int:
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == number:
            return mid
        elif array[mid] < number:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main ():
    arr = [1, 2, 4, 6, 10, 12]
    number = int(input("Введите искомый элемент: "))
    result = binary_search(arr, number)
    print(f"Исходный массив: {arr}")

    if result == -1:
        print("Элемента нет в массиве")
    else:
        print(f"Элемент: {number} найден по индексу: {result}")
        
main()