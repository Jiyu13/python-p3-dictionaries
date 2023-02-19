def pour_coffee(size) :
    size_to_ounce_map = {
        "tall": 12,
        "grande": 16,
        "venti": 20
    }
    return size_to_ounce_map[size]

pour_coffee("tall") # 12
pour_coffee("grande") # 16
pour_coffee("jumbo") # KeyError: 'jumbo'


def dict_get_method(size):
    size_to_ounce_map = {
        "tall": 12,
        "grande": 16,
        "venti": 20
    }
    return size_to_ounce_map.get(size)

dict_get_method("jumbo") # None