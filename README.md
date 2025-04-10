
# PyCNC-Slicer

## ✨ Project Goal:
A Python-based open-source tool that converts 3D models (like STL) into ready-to-run G-code for CNC machines or 3D printers, using a simple Streamlit-based UI.

---

## 🏡 High-Level Architecture:

### Layers:

#### 1. 🧯 Core Layer (Domain Logic)
- STL file parsing
- Model slicing into layers
- Toolpath generation
- G-code generation

#### 2. 📙 Application Layer (Use Cases)
- Acts as the brain between the UI and core logic
- Handles inputs from UI and manages operations flow

#### 3. 📝 Presentation Layer (UI)
- Built using Streamlit
- Handles file upload, slicing settings, and G-code generation

#### 4. 🔌 Infrastructure Layer
- Blender add-on (future feature)
- G-code file saving/export
- Hardware communication support (future scope)

---

## 🔧 Technologies:

| Component     | Tech Stack         |
|---------------|--------------------|
| UI            | Streamlit          |
| STL Handling  | trimesh, numpy-stl |
| Logic         | Python + NumPy     |
| File I/O      | Python stdlib      |
| Versioning    | Git / GitHub       |
| Testing       | pytest             |

---

## 🧱 Directory Structure (Initial):

```
pycnc_slicer/
├── core/
│   ├── stl_parser.py
│   ├── slicer.py
│   ├── toolpath_generator.py
│   ├── gcode_generator.py
│   └── __init__.py
├── app/
│   └── streamlit_ui.py
├── services/
│   └── slicer_service.py
├── utils/
│   ├── file_handler.py
│   └── logger.py
├── tests/
│   └── test_slicer.py
└── main.py
```

---

## 📣 Design Principles (SOLID):

| Principle | Application |
|-----------|-------------|
| S - SRP   | Each module has one clear job |
| O - OCP   | Can add new machine types with minimal changes |
| L - LSP   | Substituting slicers won’t break anything |
| I - ISP   | Each part depends only on what it needs |
| D - DIP   | UI depends on interfaces, not low-level logic |

---

## 📤 Testing Plan:

- Unit tests for STL reading and layer slicing
- G-code validity tests
- Basic UI input/output flow validation

---

## 🏁 Future Scope:

- Blender Add-on integration
- Exporting to physical printers/machines
- Live simulation preview
- Cloud save & share option

---

Made with love & CNC vibes by Ahmed Khalid ✨
