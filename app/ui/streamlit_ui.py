import streamlit as st
from app.models.model3d import Model3D
from app.models.gcode_converter import GCodeConverter
from app.core.cnc_machine import CNCMachine
import os
import tempfile

def run_ui():
    st.title("CNC G-code Generator 🚀")
    st.write("Upload a 3D model file to generate G-code for your CNC machine.")

    uploaded_file = st.file_uploader("Upload a 3D model (.stl, .obj)", type=["stl", "obj"])

    if uploaded_file:
        temp_file_path = os.path.join(tempfile.gettempdir(), uploaded_file.name)
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.read())

        model = Model3D(temp_file_path)
        if model.load():
            st.success("3D Model Loaded Successfully ✅")
            converter = GCodeConverter(model)
            gcode = converter.convert()

            if st.button("Generate G-code"):
                cnc = CNCMachine()
                cnc.send_gcode(gcode)
                st.code("\n".join(gcode), language="text")

                st.download_button(
                    label="Download G-code",
                    data="\n".join(gcode),
                    file_name="generated_gcode.nc",
                    mime="text/plain"
                )
        else:
            st.error("Failed to load the 3D model. Please check the file format.")