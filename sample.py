import time


def curr_seconds():
    curr = time.time()
    print("Current time in seconds since epoch =", curr)
    # print(type(curr))
    return curr


def curr_time(curr):
    current_date_time = time.ctime(curr)
    print("Current time:", current_date_time)

    return current_date_time


print(curr_time(curr_seconds()))

lists = [
    "apple",
    "banana",
    "cherry",
    "apple",
    "banana",
    "cherry",
    "apple",
    "banana",
    "cherry",
    "apple",
    "banana",
    "cherry",
]
print(lists)
