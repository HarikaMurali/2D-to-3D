import sys
import os
import main  # <-- changed from `from backend import main`

def run():
    if len(sys.argv) < 3:
        print("Usage: blender_script.py <input_image> <output_path>")
        sys.exit(1)

    input_image = sys.argv[-2]
    output_path = sys.argv[-1]

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    generated_path = main.create_blender_project([input_image])

    if os.path.exists(generated_path):
        os.rename(generated_path, output_path)
    else:
        raise FileNotFoundError("Blender output file not found")

if __name__ == "__main__":
    run()
