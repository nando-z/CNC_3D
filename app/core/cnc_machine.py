import logging

logging.basicConfig(level=logging.INFO)

class CNCMachine:
    def __init__(self):
        self.status = "IDLE"

    def send_gcode(self, gcode_lines):
        try:
            self.status = "RUNNING"
            if not all(isinstance(line, str) for line in gcode_lines):
                raise ValueError("All G-code lines must be strings.")
            
            logging.info("Sending G-code to CNC machine...")
            logging.info("\n".join(gcode_lines))
            
            self.status = "FINISHED"
        except Exception as e:
            self.status = "ERROR"
            logging.error(f"Error while sending G-code: {e}")
        finally:
            logging.info(f"CNC Machine status: {self.status}")