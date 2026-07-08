# 🎨 LinHex

**A professional, 24-bit TrueColor palette generator for your terminal.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Terminal: 24bit](https://img.shields.io/badge/Terminal-24bit_TrueColor-black?style=for-the-badge)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

LinHex is a minimalist terminal utility designed to generate harmonious color palettes instantly. Whether you're a designer looking for inspiration or a developer styling a new HUD, LinHex provides beautiful hex codes directly in your workflow.

## ✨ Features

- **🌈 Harmony Modes**: Generate palettes using **Monochromatic**, **Analogous**, **Complementary**, or **Triadic** rules.
- **🌱 Seeded Growth**: Provide a single hex color and LinHex will build a harmonious family around it.
- **🖼️ Instant Preview**: Large 24-bit color blocks with smart foreground contrast for readability.
- **⚡ Zero Dependencies**: Built with pure Python standard library.
- **🛠️ Command Driven**: Simple CLI interface for `gen` and `view` actions.

## 🛠️ Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/chambtai-sys/LinHex.git
   cd LinHex
   ```

2. **Generate a Random Palette**:
   ```bash
   ./linhex.py gen
   ```

3. **Generate from a Seed (Analogous)**:
   ```bash
   ./linhex.py gen --mode analogous --seed #6366f1
   ```

4. **Preview Specific Colors**:
   ```bash
   ./linhex.py view #ff0055 #00d2ff #10b981
   ```

## 🚀 Commands

| Command | Description |
|---|---|
| `gen` | Generate a new palette. |
| `view` | Display specific hex codes as color blocks. |
| `-m, --mode` | Set harmony mode (random, triadic, etc). |
| `-s, --seed` | Set a starting base color. |

## 📜 Requirements

- **Python 3.6+**
- **TrueColor Terminal** (Most modern terminals like iTerm2, Alacritty, Kitty, Windows Terminal, GNOME Terminal support this).

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
