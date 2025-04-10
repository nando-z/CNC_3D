import trimesh

class Model3D:
    def __init__(self, file_path):
        self.file_path = file_path
        self.mesh = None

    def load(self):
        try:
            self.mesh = trimesh.load(self.file_path)
            return self.mesh.is_watertight
        except Exception as e:
            print(f"Error loading model: {e}")
            return False