def sum(values):
    global sum_
    if isinstance(values, int):
        sum_ += values
    elif isinstance(values, str):
        sum_ += len(values)
    elif isinstance(values, dict):
        for a, b in values.items():
            sum_ += len(a)
            sum_ += b


def calculate_structure_sum(*args):
    global sum_
    for i in args:
        sum(i)
        if isinstance(i, list) or isinstance(i, set) or isinstance(i, tuple):
            for j in i:
                sum(j)
                if isinstance(j, tuple):
                    calculate_structure_sum(*j)
                if isinstance(j, list):
                    calculate_structure_sum(*j)

    return sum_

sum_ = 0

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(*data_structure)
print(result)