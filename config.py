def update_image_in_config(config_path, new_image_path):
    from . import floorplan
    fp = floorplan.new_floorplan(config_path)
    fp.image_path = new_image_path
    return fp
