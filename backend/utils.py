# backend/utils.py

import subprocess
import os
import uuid

BLENDER_PATH = r"C:\Program Files\Blender Foundation\Blender 4.4\blender.exe"

def convert_floorplan_to_3d(input_image_path):
    output_name = f"{uuid.uuid4()}.blend"
    output_path = os.path.join("outputs", output_name)

    # Correct path resolution
    blender_script = os.path.join(os.path.dirname(__file__), "blender_script.py")

    cmd = [
        BLENDER_PATH,
        "--background",
        "--python", blender_script,
        "--", input_image_path, output_path
    ]

    try:
        subprocess.run(cmd, check=True)
        return output_path
    except subprocess.CalledProcessError as e:
        print("Blender subprocess error:", e)
        return None
