import json

from src.spritesheets.SpriteSheet import SpriteSheet


class MovementManager(object):
    def __init__(self, path_img, path_json):
        self._path_img = path_img
        self._path_json = path_json
        self._get_sprite(path_json)
        self._sheet = SpriteSheet(path_img)

    def _get_sprite(self, path_json):
        with open(path_json, 'r') as json_data:
            try:
                data = json.load(json_data)
            except ValueError:
                print "\nCould not open :", self._path_json, "\n"
                raise SystemError
            frames = data.get('frames')
            mapping = dict()
            for key in frames.keys():
                metadata = frames.get(key).get('frame')
                sub_map = list()
                sub_map.append(int(metadata.get('x')))
                sub_map.append(int(metadata.get('y')))
                sub_map.append(int(metadata.get('w')))
                sub_map.append(int(metadata.get('h')))
                mapping[key] = sub_map
            self.map = mapping
            self.current_key = min(self.map.keys())
            self.highest_key = max(self.map.keys())

    def get_next_image(self):
        if self.highest_key == self.current_key:
            self.current_key = min(self.map.keys())
        else:
            print self.current_key
            # self.current_key = self.map.
        return self._sheet.image_at(self.map[self.highest_key])

    def get_resting_image(self):
        self.current_key = min(self.map.keys())
        return self._sheet.image_at(self.map[self.current_key])
