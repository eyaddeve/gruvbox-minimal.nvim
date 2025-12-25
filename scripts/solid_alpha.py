INPUT_FILE = "colors.txt"

BACKGROUND_COLOR = "#221f1d"
VISUAL_ALPHA = 0.15


def blend_colors(fg_hex, bg_hex, alpha):
    def hex_to_rgb(h):
        h = h.strip().lstrip("#")
        return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))

    fg_r, fg_g, fg_b = hex_to_rgb(fg_hex)
    bg_r, bg_g, bg_b = hex_to_rgb(bg_hex)

    new_r = (fg_r * alpha) + (bg_r * (1.0 - alpha))
    new_g = (fg_g * alpha) + (bg_g * (1.0 - alpha))
    new_b = (fg_b * alpha) + (bg_b * (1.0 - alpha))

    return "#{:02x}{:02x}{:02x}".format(int(new_r), int(new_g), int(new_b))


try:
    with open(INPUT_FILE, "r") as f:
        for line in f:
            if line.strip():
                original = line.strip()
                if len(original.strip().lstrip("#")) != 6:
                    print(f"Skipping invalid: {original}")
                    continue

                processed = blend_colors(original, BACKGROUND_COLOR, VISUAL_ALPHA)
                print(f"{original} -> {processed}")

except FileNotFoundError:
    print(f"Error: Could not find '{INPUT_FILE}'.")
