import csv
import timeit
import random
import os
from src.lab04.io_txt_csv import write_csv
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
 
def get_numbers(n):
    path = f"data/samples/lab07/numbers_{n}.csv"
    if os.path.exists(path):
      with open(path, encoding="utf-8") as f:
        return [int(row["value"]) for row in csv.DictReader(f)]
    return [random.randint(-100_000, 100_000) for _ in range(n)]
 
def bench_sort(n):
    data = get_numbers(n)
    rows = []
    t = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("sort", n, "sorted", t))

    if n==10**5:
      rows.append(("sort", n, "bubble_sort", "> 60 c"))
      rows.append(("sort", n, "insertion_sort", "> 60 c"))
      rows.append(("sort", n, "selection_sort", "> 60 c"))

    else:
      t = timeit.timeit(lambda: bubble_sort(data), number=1)
      rows.append(("sort", n, "bubble_sort", t))

      t = timeit.timeit(lambda: insertion_sort(data), number=1)
      rows.append(("sort", n, "insertion_sort", t))

      t = timeit.timeit(lambda: selection_sort(data), number=1)
      rows.append(("sort", n, "selection_sort", t))

    return rows

def bench_search():
  n = 100_000
  data = get_numbers(n)
  sorted_data = sorted(data)
  queries = [random.randint(-100_000, 100_000) for _ in range(10_000)]
  rows = []

  def linear():
     for q in queries:
        linear_search(data, q)
  time_lin = timeit.timeit(linear, number=1)
  rows.append(("search", n, "linear_search", time_lin))

  def binary():
       for q in queries:
          binary_search(sorted_data, q)
  time_bin = timeit.timeit(binary, number=1)
  rows.append(("search", n, "binary_search", time_bin))

  def sort_binary():
       s = sorted(data)
       for q in queries:
          binary_search(s, q)
  time_sb = timeit.timeit(sort_binary, number=1)
  rows.append(("search", n, "sort + binary", time_sb))

  return rows

def bench_two_sum():
  rows = []
  for n in (1_000, 10_000):
    data = get_numbers(n)
    target = data[-2] + data[-1]

    t_brute = timeit.timeit(lambda: two_sum_brute(data, target), number=1)
    rows.append(("two_sum", n, "two_sum_brute", round(t_brute, 6)))

    t_fast = timeit.timeit(lambda: two_sum_fast(data, target), number=1)
    rows.append(("two_sum", n, "two_sum_fast", round(t_fast, 6)))

  return rows


if __name__ == "__main__":
  random.seed(42)
  all_rows = []

  all_rows.extend(bench_sort(1_000))
  all_rows.extend(bench_sort(10_000))
  all_rows.extend(bench_sort(100_000))
  all_rows.extend(bench_search())
  all_rows.extend(bench_two_sum())

  print(f"{'task':<10} | {'n':<8} | {'impl':<16} | {'seconds':<10}")
  print("-"*52)
  for task, n, impl, seconds in all_rows:
    if isinstance(seconds, (int, float)):
      seconds = f"{seconds:.6f}"
    print(f"{task:<10} | {n:<8} | {impl:<16} | {seconds:<10}")

  os.makedirs("data/lab07", exist_ok=True)
  write_csv(all_rows, "data/lab07/bench.csv", header=["task", "n", "impl", "seconds"])