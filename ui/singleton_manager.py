from ui.mainui import Window

def get_window_instance():
    if not Window._instance:
        Window._instance = Window()
    return Window._instance