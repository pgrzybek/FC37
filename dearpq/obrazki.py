from dearpygui import dearpygui as dpg

dpg.create_context()

with dpg.texture_registry():
    width, height, channels, data = dpg.load_image("przycisk.jpg")
    texture_id = dpg.add_static_texture(width, height, data)

with dpg.window(label="Obraz w DearPyGui"):
    dpg.add_image(texture_id)

dpg.create_viewport(title="Test Obrazu", width=400, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
