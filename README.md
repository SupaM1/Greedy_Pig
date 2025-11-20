![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![GitHub release](https://img.shields.io/github/v/release/SupaM1/Greedy_Pig)
# 🐷 Greedy Pig Dice Game

A Python implementation of the classic probability dice game that tests your greed against your wisdom!

## 📖 About the Game

Greedy Pig is a jeopardy-style dice game where players must balance risk and reward. Roll the dice to accumulate points, but beware – roll your "dead number" and you lose everything! The question is: will you sit and bank your score, or stay greedy and risk it all for more points?

This game is commonly used to teach probability and strategic decision-making in mathematics education, but it's also just plain fun!

## 🎮 How to Play

1. **Set up your game:**
   - Choose how many sides you want on your dice (e.g., 6 for a standard die, 20 for more excitement)
   - Choose your "dead number" – the number that will end your game if rolled

2. **Play rounds:**
   - Each round, the dice rolls automatically
   - If you roll your dead number, it's **GAME OVER** – you lose all your accumulated points
   - If you roll any other number, it's added to your total score
   - After each safe roll, you must decide:
     - **Sit (1):** Bank your current score and end the game
     - **Stay (2):** Risk it all and keep rolling for more points

3. **Beat the high score:**
   - Your high score is automatically saved and tracked between games
   - Try to beat your personal best without getting too greedy!

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- No external libraries required (uses only standard library modules)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/SupaM1/Greedy_Pig.git
cd Greedy_Pig
```

2. Run the game:
```bash
python Greedy_Pig.py
```

## 📊 Features

- ✅ Customisable dice sides
- ✅ Configurable "dead number"
- ✅ Persistent high score tracking (saved to `highscore.json`)
- ✅ Simple text-based interface
- ✅ Perfect for learning Python and probability concepts

## 🎲 Strategy Tips

- The more rolls you take, the higher your score *can* be, but the probability of hitting your dead number increases
- Common strategies include:
  - **Conservative:** Sit after reaching a modest target (e.g., 15-20 points)
  - **Balanced:** Aim for a medium score (e.g., 25-30 points)
  - **Greedy Pig:** Go big or go home! (But expect lots of zeros...)
- With a standard 6-sided die and dead number of 1, your probability of disaster is 1/6 (≈16.7%) per roll

## 🐛 Known Issues

None at the moment – but feel free to open an issue if you find any bugs!

## 📝 Licence

Feel free to use, modify, and share this code for educational purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 

## 👏 Credits

Based on the classic Greedy Pig / Pig dice game, a staple of probability education and family game nights worldwide.

---

**Remember:** Pigs get fed, but hogs get slaughtered. Know when to sit! 🐷✨
