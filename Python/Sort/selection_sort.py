
def selection_sort(num_list):
    count = len(num_list)
    for i in range(count):
        min_idx = i
        for j in range(i + 1, count):
            if num_list[min_idx] > num_list[j]:
                min_idx = j
        num_list[min_idx], num_list[i] = num_list[i], num_list[min_idx]

if __name__ == "__main__":
    nums = [38, 65, 97, 76, 13, 27, 49]
    print("before sort: ")
    print(nums)
    print("after sort: ")
    selection_sort(nums)
    print(nums)