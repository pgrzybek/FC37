from dearpygui import dearpygui as dpg

tasks = []

def add_task(sender, app_data, user_data):
    task = dpg.get_value("task_input").strip()
    if task:
        row_id = f"task_{len(tasks)}"
        tasks.append(row_id)

        with dpg.group(horizontal=True, parent="task_list", tag=row_id):
            dpg.add_text(task, wrap=300)
            dpg.add_button(label="Usun", callback=delete_task, user_data=row_id)

        dpg.set_value("task_input", "")

def delete_task(sender, app_data, row_id):
    if dpg.does_item_exist(row_id):
        dpg.delete_item(row_id)
        tasks.remove(row_id)

# --- UI ---
dpg.create_context()

# Rejestracja fontu z pełnym Unicode i ustawienie jako domyślny
with dpg.font_registry():
    font = dpg.add_font("NotoSans-Regular.ttf", 50)
    #font = dpg.add_font("NotoSans-Regular.ttf", 50)
dpg.bind_font(font)
# Linux: "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    # Mac: "/System/Library/Fonts/Supplemental/Arial.ttf"
#dpg.bind_font(font)
with dpg.window(label="Backlog z polskimi znakami ń ", width=400, height=400):
    dpg.add_input_text(tag="task_input", hint="Wpisz zadanie...", width=300)
    dpg.add_button(label="Dodaj zadanie", callback=add_task)
    dpg.add_separator()
    dpg.add_group(tag="task_list")

dpg.create_viewport(title="Backlog - DearPyGui Unicode", width=420, height=450)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
