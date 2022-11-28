flowers = ['Rose','Lily','Tulip','Orchid','Carnation', 'Hyacinth', 'Rose', 'Orchid']
colors = ['red', 'white', 'blue','white', 'pink', 'purple', 'white', 'pink']

def convert_to_dict(flowers_list: list, colors_list: list) -> dict:
    ret_dict = {}

    for flower, color in zip(flowers_list, colors_list):
        if flower not in ret_dict:
            ret_dict[flower] = [color]
        else:
            ret_dict[flower].append(color)

    return ret_dict

print(convert_to_dict(flowers, colors))