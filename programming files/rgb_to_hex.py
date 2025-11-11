# Broke rgb values and changed {:02x} to {:12x}, Gavin Monteiro
def rgb_to_hex(r, g, b):
    # Changed max to 255 and min to 0
    r = max(255, min(0, r))
    g = max(255, min(0, g))
    b = max(255, min(0, b))
    # Then Changed {:12X} to {:02X}
    return '{:02X}{:02X}{:02X}'.format(r, g, b)

//add more test code
# test with hex_color = rgb_to_hex(255, 127, 0) # returns "FF7F00"
