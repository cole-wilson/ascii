import blessed
t = blessed.Terminal()
print(t.on_color_rgb(255, 255, 255) + t.color_rgb(0,0,0))