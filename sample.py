"""Sample python file."""
import time


def curr_seconds() -> float:
    """Fetch time in seconds.

    Returns:
        _type_: Float
    """
    curr = time.time()
    print("Current time in seconds since epoch =", curr)
    # print(type(curr))
    return curr


def curr_time(curr: float) -> str:
    """Give time.

    Args:
        curr (_type_): Takes time in seconds

    Returns:
        _type_: string
    """
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
    "apples",
    "bananas",
    "cherries",
]

print(lists)
