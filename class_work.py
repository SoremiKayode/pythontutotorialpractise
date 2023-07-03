name = {
    "age" : [23, 45, 67, 89, 100],
    "score" : [80, 75, 65, 45, 95]
}

# a = name["age"]
# b = name["score"]
# name["age"] = [20, 30, 40, 50, 60]

# print(name["age"])
# print(name.keys())
# print(name.values())
# print(name.items())

# def jer():
#     print(2 + 2)


# jer()

def mean(a, b):
    m1 = sum(a) / len(a)
    m2 = sum(b) / len(b)

    return m1, m2

print(mean(name["age"], name["score"]))

def highest(a, b):
    return max(a), max(b)

print(highest(name["age"], name["score"]))

def median(a, b):
    c = a[int(len(a) / 2)]
    d = b[int(len(b) / 2)]

    return c, d

print(median(name["age"], name["score"]))




