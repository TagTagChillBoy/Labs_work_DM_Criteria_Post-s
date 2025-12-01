from math import log2
from typing import List

func_value = [int(d) for d in input().split()]


def get_schaeffers_stroke_representation(func_value: List[int]) -> str:
    number_of_input_sets = len(func_value)
    number_of_arguments = int(log2(number_of_input_sets))
    schaeffers_stroke_representation = ''

    minterms = []
    for i in range(number_of_input_sets):
        if func_value[i] == 1:
            minterm_literals = []
            values_of_arguments = to_binary(i)
            lack_of_values = number_of_arguments - len(values_of_arguments)
            values_of_arguments = '0' * lack_of_values + values_of_arguments

            for k in range(number_of_arguments):
                if values_of_arguments[k] == "1":
                    minterm_literals.append(f"x{k + 1}")
                else:
                    minterm_literals.append(f"!x{k + 1}")
            # print(minterm, values_of_arguments)
            if minterm_literals:
                minterm = conjunct_recursive(minterm_literals, 0, len(minterm_literals) - 1)
                minterms.append(minterm)
    if len(minterms) == 0:
        return "(!x1 | x1) | (!x1 | x1)"
    elif len(minterms) == 1:
        return  minterms[0]

    return disjunction_recursive(minterms, 0, len(minterms) - 1)


def to_binary(n: int) -> str:
    return bin(n)[2:]

def conjunct_recursive(minterm_literals: int, s: int, e: int) -> str:
    if s == e:
        return minterm_literals[s]
    pivot = (s + e) // 2
    first = conjunct_recursive(minterm_literals, s, pivot)
    second = conjunct_recursive(minterm_literals, pivot + 1, e)

    return f"(({first} | {second}) | ({first} | {second}))"

def disjunction_recursive(minterms: int, s: int, e: int) -> str:
    if s == e:
        return minterms[s]
    pivot = (s + e) // 2
    first = disjunction_recursive(minterms, s, pivot)
    second = disjunction_recursive(minterms, pivot + 1, e)

    return f"(({first} | {first}) | ({second} | {second}))"


print(get_schaeffers_stroke_representation(func_value))