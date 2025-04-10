class GCodeConverter:
    def __init__(self, model):
        self.model = model

    def convert(self):
        # Example G-code generation logic
        return [
            "G21 ; Set units to millimeters",
            "G90 ; Absolute positioning",
            "G1 X10 Y10 Z-1 F100 ; Move to point",
            "G1 X20 Y20 Z-1 F100 ; Move to another point"
        ]