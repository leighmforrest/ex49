import copy

class Map(object):
    def __init__(self, scenes, adjacent_scenes):
        if isinstance(scenes, dict) and isinstance(adjacent_scenes, dict):
            self._scenes = copy.deepcopy(scenes)
            self._adjacent_scenes = copy.deepcopy(adjacent_scenes)
        else:
            raise ValueError("Arguments must be dictionaries.")
    
    @property
    def scenes(self):
        return self._scenes
    
    @scenes.setter
    def scenes(self, value):
        if isinstance(value, dict):
            self._scenes = value
        else:
            raise ValueError("Scenes must be a dictionary.")
    
    @property
    def adjacent_scenes(self):
        return self._adjacent_scenes
    
    @adjacent_scenes.setter
    def adjacent_scenes(self, value):
        if isinstance(value, dict):
            self._adjacent_scenes = value
        else:
            raise ValueError("Adjacent scenes must be a dictionary.")
    
    def get_next_scenes(self, current_scene):
        return self._adjacent_scenes.get(current_scene)
    
    def get_scene(self, scene_string):
        return self._scenes.get(scene_string)
