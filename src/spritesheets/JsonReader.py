import json


def treatment(data):
    frames = data.get('frames')
    mapping = list()
    for key in frames.keys():
        metadata = frames.get(key).get('frame')
        sub_map = list()
        sub_map.append(int(metadata.get('x')))
        sub_map.append(int(metadata.get('y')))
        sub_map.append(int(metadata.get('h')) + int(metadata.get('x')))
        sub_map.append(int(metadata.get('w')) + int(metadata.get('y')))
        mapping.append((int(str(key)), sub_map))
    return mapping


def get_sprites(path_to_json):
    with open(path_to_json, 'r') as json_data:
        try:
            data = json.load(json_data)
        except ValueError:
            raise SystemError
        return treatment(data)


def get_my_rectangle(mapping, frame=10000):
    output = None
    for key_values in mapping:
        if key_values[0] == frame:
            output = key_values[1]
    return output
