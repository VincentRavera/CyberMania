import json


def treatment(data):
    frames = data.get('frames')
    mapping = list()
    for key in frames.keys():
        metadata = frames.get(key).get('frame')
        sub_map = list()
        for data in metadata:
            sub_map.append(metadata.get(data))
        mapping.append((int(str(key)), sub_map))
    return  mapping





def get_Sprites(path_to_json):
    with open(path_to_json, 'r') as json_data:
        try:
            data = json.load(json_data)
        except ValueError:
            raise SystemError
        return treatment(data)
