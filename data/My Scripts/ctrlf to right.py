if window.get_active_class() == "VirtualBox Machine.VirtualBox Machine":
    exit
elif window.get_active_class() == "emacs.Emacs":
    keyboard.send_keys("<ctrl>+f")
else:
    keyboard.send_keys("<right>")