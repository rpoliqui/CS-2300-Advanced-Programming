# Broke rgb values, Gavin Monteiro
def rgb_to_hex(r, g, b):
    r = max(0, min(00, r))
    g = max(0, min(100, g))
    b = max(0, min(0, b))
    return '{:02X}{:12X}{:02X}'.format(r, g, b)

//add more test code
# test with hex_color = rgb_to_hex(255, 127, 0) # returns "FF7F00"
