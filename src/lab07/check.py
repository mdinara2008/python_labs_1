import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
 
def check_sorting(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"
    return trials


def check_search(trials=100):
  check = 0
  for _ in range(trials):
    n = random.randint(0, 50)
    nums = [random.randint(-50, 50) for _ in range(n)]
    x = random.randint(-60, 60)

    #линейный поиск
    res_l = linear_search(nums, x)
    try:
      expected = nums.index(x)
    except ValueError:
      expected = -1
    assert res_l == expected, f"linear_search ошиблась на {nums}, x={x}"
    check += 1

    #бинарный поиск
    sort_nums = sorted(nums)
    targets = [x, -999, 999]
    if sort_nums:
      targets.extend([sort_nums[0], sort_nums[-1]])

    for t in targets:
      res_b = binary_search(sort_nums, t)
      if t in sort_nums:
        assert 0<=res_b<len(sort_nums) and sort_nums[res_b]==t, f"binary_search ошиблась на {sort_nums}, x={t}, вернула {res_b}"
      else:
        assert res_b == -1, f"binary_search не вернула -1 на {sort_nums}, x={t}, вернула {res_b}"
      check += 1

  return check


def check_two_sum(trials=100):
  for _ in range(trials):
    n = random.randint(0, 40)
    nums = [random.randint(-50, 50) for _ in range(n)]
    if n >= 2 and random.random() < 0.5:
      i1, i2 = random.sample(range(n), 2)
      target = nums[i1] + nums[i2]
    else:
      target = random.randint(-100, 100)

    res_brute = two_sum_brute(nums, target)
    res_fast = two_sum_fast(nums, target)

    if res_brute is None:
      assert res_fast is None, f"two_sum разошлись (ожидался None) на {nums}, target={target}"
    else:
      assert res_fast is not None, f"two_sum_fast вернула None на {nums}, target={target}"
      i, j = res_fast
      assert 0<=i<j<len(nums) and nums[i]+nums[j]==target, f"two_sum_fast вернула неверную пару {res_fast} на {nums}, target={target}"
  return trials


if __name__ == "__main__":
  random.seed(42)
  total = 0
  for fn in (bubble_sort, insertion_sort, selection_sort):
    total += check_sorting(fn)
  total += check_search()
  total += check_two_sum()
  print(f"OK: {total} проверок")
  