from typing import List

m = int(input())

cons_values = []

for _ in range(m):
    x = [int(d) for d in input().split()]
    cons_values.append(x)


belonging_to_classes = {"MONOTONIC": 1, "LINEAR": 1, "SELF-DUAL": 1, "0-PRESERVING": 1, "1-PRESERVING": 1}


def to_binary(n: int) -> str:
    return bin(n)[2:]


def is_monotonic(values_of_func: List[int]) -> bool:
    num_of_arguments = len(values_of_func)
    # num_of_variables = int(log2(num_of_arguments))

    # just doing brute force
    for j in range(num_of_arguments):
        for k in range(num_of_arguments):
            # набор j >= k
            if (j & k) == k:
                if values_of_func[j] < values_of_func[k]:
                    return False
    return True

def is_linear(values_of_func: List[int]) -> bool:
    num_of_arguments = len(values_of_func)

    # we will use criteria of a linear func: for all sets a and b: f(a xor b) = f(a) xor f(b)
    for x in range(num_of_arguments):
        for y in range(num_of_arguments):
            a_xor_b = x ^ y
            if values_of_func[a_xor_b] != (values_of_func[x] ^ values_of_func[y]) ^ values_of_func[0]:
                return False
    return True

def is_self_dual(values_of_func: List[int]) -> bool:
    num_of_arguments = len(values_of_func)

    for x in range(num_of_arguments):
        # criteria of not self-dual func: exists a set of an arguments such that f(a_1, ..., a_n) = f(not(a_1), ..., not(a_n))
        if values_of_func[x] == values_of_func[num_of_arguments - 1 - x]:
            return False
    return True

def is_0_preserving(values_of_func: List[int]) -> bool:
    return values_of_func[0] == 0

def is_1_preserving(values_of_func: List[int]) -> bool:
    num_of_arguments = len(values_of_func)

    return values_of_func[num_of_arguments - 1] == 1


# checking non-belonging to precomplete classes
for i in range(m):
    func = cons_values[i]
    if not is_monotonic(func):
        belonging_to_classes["MONOTONIC"] = 0
    if not is_linear(func):
        belonging_to_classes["LINEAR"] = 0
    if not is_self_dual(func):
        belonging_to_classes["SELF-DUAL"] = 0
    if not is_0_preserving(func):
        belonging_to_classes["0-PRESERVING"] = 0
    if not is_1_preserving(func):
        belonging_to_classes["1-PRESERVING"] = 0
# number of classes the system belongs to
num_of_belonging_classes = 0
for belongs in belonging_to_classes.values():
    if belongs == 1:
        num_of_belonging_classes += 1

# print an answer
if num_of_belonging_classes == 0:
    print("COMPLETE")
else:
    for precomplete_class in belonging_to_classes.keys():
        if belonging_to_classes[precomplete_class] == 1:
            print(precomplete_class)