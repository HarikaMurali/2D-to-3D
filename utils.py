import subprocess
import os
from FloorplanToBlenderLib import IO, const, config, floorplan, execution

def run_blender_conversion(image_path, blender_path):
    # Setup paths
    program_path = os.path.dirname(os.path.realpath(__file__))
    blender_script_path = const.BLENDER_SCRIPT_PATH
    target_folder = const.TARGET_PATH
    target_base = target_folder + const.TARGET_NAME
    target_path = (
        IO.get_next_target_base_name(target_base, target_base + const.BASE_FORMAT)
        + const.BASE_FORMAT
    )

    # Clean data folder
    IO.clean_data_folder(const.BASE_PATH)

    # Load config and set image
    config_path = "./Configs/default.ini"
    fp = floorplan.new_floorplan(config_path)
    fp.image_path = image_path

    # Generate data path from config
    data_paths = [execution.simple_single(fp)]

    # Create Blender .blend project
    subprocess.check_output([
        blender_path,
        "-noaudio",
        "--background",
        "--python", blender_script_path,
        program_path,
        target_path,
    ] + data_paths)

    # Export format
    outformat = config.get(
        const.SYSTEM_CONFIG_FILE_NAME, "SYSTEM", const.STR_OUT_FORMAT
    ).replace('"', "")

    final_output = "." + target_path
    if outformat != ".blend":
        final_output = target_base + outformat
        subprocess.check_output([
            blender_path,
            "-noaudio",
            "--background",
            "--python", "./Blender/blender_export_any.py",
            "." + target_path,
            outformat,
            final_output,
        ])

    return final_output
