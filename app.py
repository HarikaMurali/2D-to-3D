import gradio as gr
import os
import shutil
from utils import run_blender_conversion

OUTPUT_DIR = "./Target"
BLENDER_PATH = "C:\\Program Files\\Blender Foundation\\Blender 4.4\\blender.exe"

def process_floorplan(image):
    # Save the uploaded image temporarily
    input_path = os.path.join("temp", "input.png")
    os.makedirs("temp", exist_ok=True)
    image.save(input_path)

    # Run blender processing
    output_path = run_blender_conversion(image_path=input_path, blender_path=BLENDER_PATH)

    # Return downloadable file
    return output_path

with gr.Blocks() as demo:
    gr.Markdown("## 🏠 Floorplan to 3D Model Generator")
    with gr.Row():
        with gr.Column():
            input_img = gr.Image(label="Upload 2D Floorplan", type="pil")
            btn = gr.Button("Generate 3D Model")
        with gr.Column():
            output_file = gr.File(label="Download 3D Model")

    btn.click(process_floorplan, inputs=input_img, outputs=output_file)

if __name__ == "__main__":
    demo.launch(share=True)
