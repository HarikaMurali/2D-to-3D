import gradio as gr
import os
from utils import convert_floorplan_to_3d

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_image(image):
    image_path = os.path.join(UPLOAD_DIR, "input.png")
    image.save(image_path)

    output_model_path = convert_floorplan_to_3d(image_path)
    if output_model_path and os.path.exists(output_model_path):
        return output_model_path
    else:
        raise gr.Error("Error in generating 3D model.")

demo = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="pil", label="Upload Floorplan"),
    outputs=gr.File(label="Download 3D Model (.blend)"),
    title="2D Floorplan to 3D Model",
    description="Upload a 2D floor plan image to generate a 3D model using Blender."
)

if __name__ == "__main__":
    demo.launch()
