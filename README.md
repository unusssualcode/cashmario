# 🍄 CASHMARIO 🍄

```
    _____ _____ _____ _   _ ___  ___  ___  ______ _____ _____ 
   /  __ \  __ |  ___| | | ||  \/  | / _ \ | ___ \_   _|  _  |
   | /  \/ /  \| |__ | |_| || .  . |/ /_\ \| |_/ / | | | | | |
   | |   | |  ||  __||  _  || |\/| ||  _  ||    /  | | | | | |
   | \__/\ \__/\ |___| | | || |  | || | | || |\ \ _| |_\ \_/ /
    \____/\____/\____\_| |_/\_|  |_/\_| |_/\_| \_|\___/ \___/ 
```

### 🎮 Classic Mario-Style Arcade Game built with Python + Pygame

---

## 📖 Description

**CASHMARIO** is a dynamic 2D platformer game inspired by the classic Mario. Run, jump, shoot and dodge enemy mushrooms! How long can you survive?

---

## ✨ Features

- 🏃 **Smooth character control** with walking animation
- 🦘 **Dynamic jumping** with realistic physics
- 🍄 **Random enemy spawning** for unpredictable gameplay
- 💥 **Shooting system** with limited bullets
- 🎨 **Parallax background scrolling**
- ♻️ **One-click game restart** system
- 🎯 **Collision detection** between player, enemies and bullets

---

## 🎯 Controls

| Key | Action |
|---------|----------|
| `←` | Move left |
| `→` | Move right |
| `SPACE` | Jump |
| `B` | Shoot (5 bullets) |
| `MOUSE` | Restart game (on game over) |

---

## 🚀 Quick Start

### Requirements

- Python 3.7+
- Pygame

### Installation

```bash
# Clone the repository
git clone <your-repo-url>

# Navigate to project directory
cd PyGame_courseProj

# Install dependencies
pip install pygame
```

### Launch Game

```bash
python main.py
```

or using Bun:

```bash
bun run python main.py
```

---

## 📁 Project Structure

```
PyGame_courseProj/
│
├── main.py              # Application entry point
├── game.py              # Main game loop and logic
├── player.py            # Player class
├── enemy.py             # Enemy class
├── bullet.py            # Bullet class
├── assets.py            # Resource loading
├── config.py            # Constants and settings
│
├── images/              # Graphics resources
│   ├── player_right/    # Right movement animation
│   ├── player_left/     # Left movement animation
│   ├── enemy/           # Enemy sprites
│   ├── bg.png           # Background image
│   ├── bullet.png       # Bullet sprite
│   └── icon.png         # Game icon
│
└── fonts/               # Fonts
    └── Mont-Bold.ttf    # Main game font
```

---

## 🎨 Architecture

The project is built with a modular approach for easy maintenance and extension:

- **config.py** - Centralized settings (speeds, sizes, positions)
- **assets.py** - Management of all game resources
- **player.py** - Encapsulation of player logic (movement, jumps, animation)
- **enemy.py** - Enemy logic
- **bullet.py** - Bullet logic
- **game.py** - Main game loop, event handling and rendering
- **main.py** - Minimalist entry point

---

## ⚙️ Game Configuration

All game parameters are easily configurable in `config.py`:

```python
SCREEN_WIDTH = 800          # Window width
SCREEN_HEIGHT = 600         # Window height
PLAYER_SPEED = 5            # Player speed
BULLET_SPEED = 14           # Bullet speed
ENEMY_SPEED = 10            # Enemy speed
FPS = 10                    # Frames per second
```

---

## 🎮 Game Mechanics

### Life System
- One collision with a mushroom = Game Over
- Can restart after losing

### Combat System
- Limited to 5 bullets per game
- Bullets destroy mushrooms on hit
- Shoot wisely! 🎯

### Enemies
- Mushrooms spawn randomly
- Move from right to left
- Increasing difficulty over time

---

## 🛠️ Technologies

- **Python** - Main programming language
- **Pygame** - Game engine
- **OOP** - Object-oriented approach

---

## 📝 TODO

- [ ] Add score system
- [ ] Add sound effects
- [ ] Add background music
- [ ] Add level system
- [ ] Add bonuses and power-ups
- [ ] Add more enemy types
- [ ] Add high score leaderboard

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📄 License

This project was created for educational purposes.

---

<div align="center">

### 🍄 Made with ❤️ and Pygame 🍄

**Play, have fun and defeat the mushrooms!** 🎮

```
    ⭐ If you enjoyed the game, give it a star! ⭐
```

</div>

