


test = {
    'i':5,
    'a':2,
    'c':1,
    'h':12
}


print(test)

sorted_dict = dict(sorted(test.items(), key=lambda kv: kv[1]))

print(sorted_dict)