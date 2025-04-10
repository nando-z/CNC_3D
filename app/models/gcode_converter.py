from app.models.model3d import Model3D
from pycam.Geometry import Toolpath
from pycam.Toolpath import LinearToolpath

class GCodeConverter:
    def __init__(self, model: Model3D, toolpath: Toolpath):
        self.model = model
        self.toolpath = toolpath

    def convert_to_gcode(self) -> str:
        # Convert the toolpath to G-code format
        gcode_lines = []
        for segment in self.toolpath.segments:
            if isinstance(segment, LinearToolpath):
                gcode_lines.append(f"G1 X{segment.end.x} Y{segment.end.y} Z{segment.end.z}")
            # Add more segment types as needed

        # Combine the G-code lines into a single string
        return "\n".join(gcode_lines)