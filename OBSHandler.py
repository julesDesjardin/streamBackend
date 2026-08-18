from obsws_python import ReqClient


class OBSHandler:
    def __init__(self):
        self.obsApi = ReqClient(
            host="localhost",
            port=4455,
            password=""
        )

    def setSourceVisibility(self, scene_name, source_name, visible):
        self.obsApi.set_scene_item_enabled(
            scene_name=scene_name,
            item_id=self.obsApi.get_scene_item_id(scene_name, source_name).scene_item_id,
            enabled=visible
        )

    def setSourceVisibilityPrefix(self, scene_name, source_prefix, visible):
        items = self.obsApi.get_scene_item_list(scene_name).scene_items
        for item in items:
            name = item["sourceName"]
            if name.startswith(source_prefix):
                self.obsApi.set_scene_item_enabled(
                    scene_name=scene_name,
                    item_id=item["sceneItemId"],
                    enabled=visible
                )
