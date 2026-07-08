#!/usr/bin/env python3
"""
LinHex - Professional Terminal Hex Color Palette Generator.
Built for designers, developers, and terminal enthusiasts.
"""

import argparse
import colorsys
import random
import sys

# --- Constants & ANSI ---
C_BOLD = "\033[1m"
C_RESET = "\033[0m"

def get_bg_color(hex_code):
    """Return ANSI escape sequence for 24-bit background color."""
    hex_code = hex_code.lstrip('#')
    r, g, b = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
    return f"\033[48;2;{r};{g};{b}m"

def get_fg_color(hex_code):
    """Return white or black escape sequence based on luminance."""
    hex_code = hex_code.lstrip('#')
    r, g, b = tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
    # Standard formula for relative luminance
    luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    return "\033[38;5;232m" if luminance > 0.5 else "\033[38;5;255m"

def hex_to_hls(hex_code):
    hex_code = hex_code.lstrip('#')
    r, g, b = [int(hex_code[i:i+2], 16) / 255.0 for i in (0, 2, 4)]
    return colorsys.rgb_to_hls(r, g, b)

def hls_to_hex(h, l, s):
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return "#{:02x}{:02x}{:02x}".format(int(r*255), int(g*255), int(b*255))

def generate_palette(mode="random", seed=None):
    palette = []
    if seed:
        h, l, s = hex_to_hls(seed)
    else:
        h, l, s = random.random(), 0.5, 0.7

    if mode == "monochromatic":
        for i in range(5):
            palette.append(hls_to_hex(h, max(0.1, min(0.9, l + (i-2)*0.15)), s))
    elif mode == "analogous":
        for i in range(5):
            palette.append(hls_to_hex((h + (i-2)*0.05) % 1.0, l, s))
    elif mode == "complementary":
        palette.append(hls_to_hex(h, l, s))
        palette.append(hls_to_hex(h, l - 0.2, s - 0.1))
        palette.append(hls_to_hex((h + 0.5) % 1.0, l, s))
        palette.append(hls_to_hex((h + 0.5) % 1.0, l - 0.1, s))
        palette.append(hls_to_hex(h, l + 0.2, s))
    elif mode == "triadic":
        palette.append(hls_to_hex(h, l, s))
        palette.append(hls_to_hex((h + 0.33) % 1.0, l, s))
        palette.append(hls_to_hex((h + 0.66) % 1.0, l, s))
        palette.append(hls_to_hex(h, l - 0.2, s))
        palette.append(hls_to_hex((h + 0.33) % 1.0, l - 0.2, s))
    else: # random
        for _ in range(5):
            palette.append(hls_to_hex(random.random(), 0.4 + random.random()*0.2, 0.6 + random.random()*0.3))
    
    return palette

def display_palette(palette):
    print("\n  " + C_BOLD + "LINHEX | Terminal Palette" + C_RESET)
    print("  " + "─" * 40 + "\n")
    
    # Draw top half of blocks
    sys.stdout.write("  ")
    for color in palette:
        sys.stdout.write(get_bg_color(color) + "          " + C_RESET + " ")
    sys.stdout.write("\n  ")
    
    # Draw middle half with hex text
    for color in palette:
        fg = get_fg_color(color)
        bg = get_bg_color(color)
        sys.stdout.write(bg + fg + f" {color.upper()}  " + C_RESET + " ")
    sys.stdout.write("\n  ")

    # Draw bottom half
    for color in palette:
        sys.stdout.write(get_bg_color(color) + "          " + C_RESET + " ")
    print("\n")

def main():
    parser = argparse.ArgumentParser(description="LinHex - Terminal Color Palette Generator")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Gen command
    gen_p = subparsers.add_parser("gen", help="Generate a random palette")
    gen_p.add_argument("-m", "--mode", choices=["random", "monochromatic", "analogous", "complementary", "triadic"], default="random")
    gen_p.add_argument("-s", "--seed", help="Seed hex color (e.g. #6366f1)")

    # View command
    view_p = subparsers.add_parser("view", help="View specific hex colors")
    view_p.add_argument("colors", nargs="+", help="Hex codes to preview")

    args = parser.parse_args()

    if args.command == "gen":
        palette = generate_palette(args.mode, args.seed)
        display_palette(palette)
    elif args.command == "view":
        display_palette(args.colors)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
