# { "key": "value"}

a = {1: "hi", "a": "aaa"}

print(a)
print(a[1])
print(a['a'])

# {1: 'hi', 'a': 'aaa'}
# hi
# aaa

a["b"] = "bbb"

print(a)    # {1: 'hi', 'a': 'aaa', 'b': 'bbb'}

del a["b"]
print(a)    # {1: 'hi', 'a': 'aaa'}

b = {1: "a", 1: "b"}
print(b[1]) # b

print(a.keys()) # dict_keys([1, 'a'])
for k in a.keys():
    print(k)    # 1 a
    
print(a.values())   # dict_values(['hi', 'aaa'])    get a list of values
print(a.items())    # dict_items([('a', 'aaa'), (1, 'hi')]) get as tuple

print(a.get("notExistKey")) # None
print(a.get("notExistKey", "DefaultKey")) # DefaultKey

# Confirm that a certain key is exist in this dictionary.
print('name' in a)  # false
print(1 in a)  # true
