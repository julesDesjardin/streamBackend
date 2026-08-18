from FlaskServer import post_payload, with_dependency


def mainPageRoutes(app, obs):
    """Register mainPage routes on the Flask app."""

    @app.route("/setCamSource", methods=["POST"])
    @post_payload
    @with_dependency(obs=obs)
    def setCamSource(payload, obs):
        print("Received setCamSource")
        cam = payload.get("cam")
        source = payload.get("source")
        if cam is None:
            return {"error": "Missing 'cam' parameter"}
        if cam not in ["1", "2"]:
            return {"error": "Invalid 'cam' parameter. Must be 1 or 2"}
        if source is None:
            return {"error": "Missing 'source' parameter"}
        if source not in ["overhead", "ptz"]:
            return {"error": "Invalid 'source' parameter. Must be 'overhead' or 'ptz'"}

        print(f"Setting camera {cam} source to {source}")

        obs.setSourceVisibility(f"Source_Cam{cam}", f"Source_Overhead{cam}", source == "overhead")
        obs.setSourceVisibility(f"Source_Cam{cam}", f"Source_PTZ{cam}", source == "ptz")
        obs.setSourceVisibility("Preview_Cams", f"Preview_Cam{cam}_PTZ", source == "ptz")
        obs.setSourceVisibility("Preview_Cams", f"Preview_Cam{cam}_Overhead", source == "overhead")

        return {"cam": cam, "source": source}

    @app.route("/setScene", methods=["POST"])
    @post_payload
    @with_dependency(obs=obs)
    def setScene(payload, obs):
        scene = payload.get("scene")
        print("Received setScene")
        if scene is None:
            return {"error": "Missing 'scene' parameter"}
        if scene not in ["Cam1", "Cam2", "Bothcams"]:
            return {"error": "Invalid 'scene' parameter. Must be one of: 'Cam1', 'Cam2', 'Bothcams'"}

        print(f"Setting scene to {scene}")

        if scene == "Cam1":
            obs.setSourceVisibility("Preview_Cams", "Preview_Cam1_active", True)
            obs.setSourceVisibility("Preview_Cams", "Preview_Cam1_inactive", False)
            obs.setSourceVisibility("Preview_Cams", "Preview_Cam2_active", False)
            obs.setSourceVisibility("Preview_Cams", "Preview_Cam2_inactive", True)
        elif scene == "Cam2":
            obs.setSourceVisibility("Preview_Cams", "Preview_Cam1_active", False)
            obs.setSourceVisibility("Preview_Cams", "Preview_Cam1_inactive", True)
            obs.setSourceVisibility("Preview_Cams", "Preview_Cam2_active", True)
            obs.setSourceVisibility("Preview_Cams", "Preview_Cam2_inactive", False)
        else:
            obs.setSourceVisibility("Preview_Cams", "Preview_Cam1_active", True)
            obs.setSourceVisibility("Preview_Cams", "Preview_Cam1_inactive", False)
            obs.setSourceVisibility("Preview_Cams", "Preview_Cam2_active", True)
            obs.setSourceVisibility("Preview_Cams", "Preview_Cam2_inactive", False)

        obs.obsApi.set_current_program_scene(f"Scene_{scene}")

        return {"scene": scene}
