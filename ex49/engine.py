class Engine(object):

    def __init__(self, player, scene_map, starting_scene_name):
        self.player = player
        self.scene_map = scene_map
        self.starting_scene_name = starting_scene_name

    def play(self):
        current_scene_name = self.starting_scene_name
        current_scene = self.scene_map.get_scene(current_scene_name)
        last_scene = self.scene_map.get_scene("finished")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter(self.player)

            if next_scene_name in self.scene_map.get_next_scenes(current_scene_name):
                current_scene = self.scene_map.get_scene(next_scene_name)
                current_scene_name = next_scene_name
            else:
                raise ValueError("Next scene is not adjacent to current scene.")

        current_scene.enter(self.player)
