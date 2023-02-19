my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

[key for key in my_dict]  # ['a', 'b', 'c', 'd']
[my_dict[key] for key in my_dict]  # [1, 2, 3, 4]


[item for item in my_dict.items()]  # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]


[key for key, value in my_dict.items()] # ['a', 'b', 'c', 'd']

[value for key, value in my_dict.items()]  # [1, 2, 3, 4]
