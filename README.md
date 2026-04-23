# 🐍 Python Mini Projects - Advanced Portfolio Edition

A comprehensive collection of **10 advanced Python mini-projects** designed for educational purposes and portfolio building. Each project has been significantly enhanced with modern best practices, clean code architecture, error handling, and advanced features.

---

## 📋 Table of Contents

- [Projects Overview](#projects-overview)
- [Project Details](#project-details)
- [Technologies & Features](#technologies--features)
- [Installation & Setup](#installation--setup)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [Learning Outcomes](#learning-outcomes)
- [GUI Enhancement Suggestions](#gui-enhancement-suggestions)

---

## 🎯 Projects Overview

| # | Project | Description | Advanced Features |
|---|---------|-------------|------------------|
| 1 | **Number Guessing Game** | Interactive number guessing with AI hints | Difficulty levels, Score system, Statistics |
| 2 | **To-Do List** | Task management with persistence | File storage (JSON), Priority levels, Statistics |
| 3 | **Calculator** | Advanced mathematical operations | Multiple operations, History, Continuous mode |
| 4 | **Palindrome Checker** | String palindrome detection | Batch processing, Regex validation |
| 5 | **Fibonacci Generator** | Fibonacci sequence with optimizations | Memoization, Performance comparison |
| 6 | **Countdown Timer** | Customizable countdown with alerts | Presets, Progress bars, Sound notifications |
| 7 | **Password Generator** | Secure password generation | Strength checker, Customization, Batch mode |
| 8 | **Email Slicer** | Email validation and analysis | Regex validation, Provider detection, Statistics |
| 9 | **Rock Paper Scissors** | Game with AI and scoring | Difficulty levels, Match tracking, Statistics |
| 10 | **Quiz Game** | Multi-category interactive quiz | Shuffled questions, Scoring, Multiple difficulties |

---

## 📚 Project Details

### 1️⃣ **Number Guessing Game** (`1-Number_Guessing_Game.py`)

A classic guessing game with modern enhancements.

**Features:**
- 🎮 **3 Difficulty Levels**: Easy (1-50), Medium (1-100), Hard (1-500)
- 💡 **Smart Hints**: "Higher" or "Lower" guidance
- 📊 **Score System**: Points vary by difficulty
- 📈 **Statistics Tracking**: Win rate, total score, games played
- 🎯 **Menu-Driven Interface**

**How to Play:**
```bash
python 1-Number_Guessing_Game.py
```

**Key Functions:**
- `select_difficulty()` - Choose game difficulty
- `get_hint()` - Provide helpful hints
- `play_round()` - Execute single game
- `display_stats()` - Show player statistics

---

### 2️⃣ **To-Do List** (`2-To-do-List.py`)

Advanced task management system with persistent storage.

**Features:**
- 💾 **JSON File Storage**: Automatically saves tasks
- ✅ **Task Status Tracking**: Mark tasks complete/pending
- 🏷️ **Priority Levels**: low, medium, high
- 📊 **Statistics**: Completion rate, task count
- ✏️ **Full CRUD Operations**: Create, Read, Update, Delete

**How to Run:**
```bash
python 2-To-do-List.py
```

**Menu Options:**
1. Add Task (with priority)
2. View All Tasks
3. View Pending Tasks Only
4. Mark Task Complete
5. Update Task
6. Delete Task
7. View Statistics

---

### 3️⃣ **Calculator** (`3-simple-calculaator.py`)

Full-featured calculator with advanced operations.

**Supported Operations:**
- ➕ Addition (+)
- ➖ Subtraction (-)
- ✖️ Multiplication (*)
- ➗ Division (/)
- 📊 Modulus (%)
- 🔢 Power (**)
- √ Square Root
- % Percentage calculations

**Features:**
- 📜 **Calculation History**: View all previous calculations
- 🔄 **Continuous Mode**: Multiple calculations without restarting
- ❌ **Error Handling**: Division by zero, invalid inputs
- 🎯 **Clean Output**: Formatted results

---

### 4️⃣ **Palindrome Checker** (`4-Palindrome-Checker.py`)

Advanced palindrome detection with multiple modes.

**Features:**
- 🔤 **Case-Insensitive Checking**: "Racecar" = "racecar"
- ➡️ **Ignore Spaces & Punctuation**: "A man, a plan, a canal: Panama"
- 📝 **Batch Processing**: Check multiple words at once
- 📊 **Detailed Analysis**: Character counts, reversed strings
- 🏷️ **Multiple Modes**: Single word, sentence, batch

---

### 5️⃣ **Fibonacci Sequence** (`5-Fibonacci-Sequence.py`)

Optimized Fibonacci generation with multiple algorithms.

**Methods:**
- 🔄 **Iterative Approach**: Fast, memory-efficient
- 🔁 **Recursive with Memoization**: Balanced performance
- 📊 **Pure Recursive**: Educational (slower)

**Features:**
- ⚡ **Performance Comparison**: Compare algorithm speeds
- 🎯 **Range Generation**: Get Fibonacci numbers in a range
- 💾 **Memoization Cache**: Optimized recursion
- 📈 **Large Number Support**: Generate high-index Fibonacci

---

### 6️⃣ **Countdown Timer** (`6-CountDown-Timer.py`)

Feature-rich countdown timer with presets.

**Features:**
- ⏱️ **Custom Duration**: Any time in seconds or mm:ss format
- 🎯 **Preset Timers**: Pomodoro (25m), Short (5m), Study (45m)
- 📊 **Progress Bar**: Visual countdown display
- 🔔 **Audio Alerts**: System bell when complete
- 📈 **Timer Statistics**: Track completed timers

**Presets:**
- Pomodoro: 25 minutes
- Short Break: 5 minutes
- Medium Break: 15 minutes
- Long Break: 30 minutes

---

### 7️⃣ **Password Generator** (`7-Password-Generator.py`)

Advanced password generation with security analysis.

**Features:**
- 🔐 **Customizable Options**:
  - Length (4-128 characters)
  - Character types (uppercase, lowercase, digits, special)
- 📊 **Strength Checker**: Analyzes password security
- 🎯 **Presets**: Quick strong password generation
- 📦 **Batch Mode**: Generate multiple passwords
- 💡 **Recommendations**: Security improvement tips

**Strength Levels:**
- ❌ WEAK (0-2 points)
- ⚠️ FAIR (3-4 points)
- ✅ GOOD (5-6 points)
- 🔒 STRONG (7+ points)

---

### 8️⃣ **Email Slicer** (`8-Email-Slicer.py`)

Comprehensive email validation and analysis.

**Features:**
- ✅ **Regex Validation**: RFC 5322 compliant
- 🔍 **Component Extraction**: Username, domain, extension
- 🏢 **Provider Detection**: Gmail, Outlook, Yahoo, etc.
- 📊 **Quality Metrics**: Email analysis
- 📋 **Batch Validation**: Check multiple emails
- 📈 **Statistics**: Validity rate tracking

**Extracted Information:**
- Full email
- Username
- Domain
- Domain name
- Extension

---

### 9️⃣ **Rock Paper Scissors** (`9-Rock-paper_scissser.py`)

Advanced game with AI and comprehensive tracking.

**Features:**
- 🎮 **3 Difficulty Levels**:
  - Easy: Random moves
  - Medium: 30% strategic
  - Hard: 60% strategic
- 📊 **Score Tracking**: Wins, losses, ties, win rate
- 📜 **Game History**: Review all previous rounds
- 📈 **Statistics**: Move distribution, performance analysis
- 🎯 **Best of N**: Play multiple-round matches

---

### 🔟 **Quiz Game** (`10-quiz-game.py`)

Interactive quiz with multiple categories and difficulties.

**Features:**
- 🎓 **3 Categories**:
  - General Knowledge
  - Science
  - Technology
- 📚 **3 Difficulty Levels**: Easy, Medium, Hard
- 🔀 **Question Shuffling**: Randomized order
- 📊 **Scoring System**: Points vary by difficulty
- 📈 **Statistics**: Accuracy, total points, category performance
- 🎯 **Progress Tracking**: Current score display

**Difficulty Points:**
- Easy: 10 points
- Medium: 25 points
- Hard: 50 points

---

## 🛠️ Technologies & Features

### **Core Technologies**
- **Python 3.8+** - Modern Python features
- **Standard Library**: json, random, string, time, math, re, functools
- **No External Dependencies** - Pure Python implementations

### **Design Patterns Used**
- 🏗️ **Object-Oriented Programming**: Class-based architecture
- 📦 **Modular Design**: Separated concerns
- 🔄 **DRY Principle**: Don't Repeat Yourself
- 🎯 **Single Responsibility**: Each function does one thing well

### **Advanced Features**
- ✅ **Comprehensive Error Handling**: Try-except blocks
- 📝 **Detailed Docstrings**: Every function documented
- 🔤 **PEP 8 Compliance**: Clean, readable code
- 💾 **Data Persistence**: JSON file storage
- 📊 **Statistics & Analytics**: Track metrics
- 🎨 **User-Friendly UI**: Clear formatted menus

---

## 📥 Installation & Setup

### **Requirements**
- Python 3.8 or higher
- Windows, macOS, or Linux

### **Step 1: Clone Repository**
```bash
git clone <repository-url>
cd python-mini-projects
```

### **Step 2: Verify Python Installation**
```bash
python --version
# or
python3 --version
```

### **Step 3: No Dependencies Installation Needed!**
All projects use only the Python standard library.

---

## 🚀 How to Run

### **Run Individual Projects**
```bash
# Number Guessing Game
python 1-Number_Guessing_Game.py

# To-Do List
python 2-To-do-List.py

# Calculator
python 3-simple-calculaator.py

# Palindrome Checker
python 4-Palindrome-Checker.py

# Fibonacci Generator
python 5-Fibonacci-Sequence.py

# Countdown Timer
python 6-CountDown-Timer.py

# Password Generator
python 7-Password-Generator.py

# Email Slicer
python 8-Email-Slicer.py

# Rock Paper Scissors
python 9-Rock-paper_scissser.py

# Quiz Game
python .10-quiz-game.py
```

### **Run All Projects (Demo Mode)**
Create `run_all.py`:
```python
import os
import subprocess

projects = [
    "1-Number_Guessing_Game.py",
    "2-To-do-List.py",
    "3-simple-calculaator.py",
    # ... add others as needed
]

for project in projects:
    print(f"\\nRunning {project}...")
    subprocess.run(["python", project])
```

---

## 📁 Project Structure

```
python-mini-projects/
├── 1-Number_Guessing_Game.py    # Difficulty levels, hints, scoring
├── 2-To-do-List.py              # File storage, priority tracking
├── 3-simple-calculaator.py      # Advanced operations, history
├── 4-Palindrome-Checker.py      # Regex, batch processing
├── 5-Fibonacci-Sequence.py      # Algorithms, memoization, performance
├── 6-CountDown-Timer.py         # Presets, progress bar, alerts
├── 7-Password-Generator.py      # Strength checker, customization
├── 8-Email-Slicer.py            # Validation, provider detection
├── 9-Rock-paper_scissser.py     # AI levels, statistics
├── .10-quiz-game.py             # Categories, shuffling, scoring
├── tasks.json                   # To-Do List data (auto-generated)
└── README.md                    # This file
```

---

## 📖 Learning Outcomes

By studying and using these projects, you'll learn:

### **Python Fundamentals**
- ✅ Variables, data types, operators
- ✅ Control flow (if/elif/else, loops)
- ✅ Functions and parameters
- ✅ Object-Oriented Programming (OOP)

### **Advanced Concepts**
- ✅ File I/O and JSON handling
- ✅ Exception handling and error management
- ✅ Regular expressions (regex)
- ✅ Data structures (lists, dictionaries, tuples)
- ✅ Algorithms and performance optimization
- ✅ Memoization and caching

### **Best Practices**
- ✅ Clean code principles
- ✅ Code documentation
- ✅ User input validation
- ✅ Menu-driven interfaces
- ✅ Statistics and logging
- ✅ PEP 8 style guidelines

### **Soft Skills**
- ✅ Project organization
- ✅ User experience design
- ✅ Problem-solving approaches
- ✅ Debugging techniques

---

## 🎨 GUI Enhancement Suggestions

Each project can be converted to a GUI application using **Tkinter**. Here are suggestions:

### **1. Number Guessing Game (Tkinter)**
```python
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")

# Add buttons for difficulty selection, text entry for guess, label for hints
# Use messagebox for results
```

### **2. To-Do List (Tkinter)**
```python
import tkinter as tk
from tkinter import ttk

# Treeview widget for task display
# Entry widgets for task input
# Buttons for CRUD operations
# Progressbar for completion rate
```

### **3. Calculator (Tkinter)**
```python
import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

# Grid layout with number buttons (0-9)
# Operation buttons (+, -, *, /, etc.)
# Display label for results
# History text widget
```

### **4. Password Generator (PySimpleGUI)**
```python
import PySimpleGUI as sg

layout = [
    [sg.Text("Password Length:"), sg.Slider(range=(4, 128), size=(20, 15))],
    [sg.Checkbox("Uppercase"), sg.Checkbox("Lowercase")],
    [sg.Checkbox("Digits"), sg.Checkbox("Special Chars")],
    [sg.Button("Generate"), sg.Button("Exit")],
    [sg.Text("", key="-OUTPUT-")]
]
```

### **5. Quiz Game (Tkinter)**
```python
import tkinter as tk
from tkinter import ttk

# Radio buttons for answer selection
# Label for question display
# Progress bar for quiz progress
# Results window with score breakdown
```

### **GUI Framework Options:**
- **Tkinter**: Built-in, lightweight, perfect for beginners
- **PySimpleGUI**: Easy event-driven programming
- **PyQt5/PySide**: Professional, feature-rich
- **Kivy**: Mobile-friendly, cross-platform

---

## 🎓 Usage Examples

### **Example 1: Using Number Guessing Game**
```
🎯 NUMBER GUESSING GAME
============================================================
SELECT DIFFICULTY LEVEL
============================================================
1. Easy   (1-50, 10 attempts, 10 points)
2. Medium (1-100, 7 attempts, 25 points)
3. Hard   (1-500, 5 attempts, 50 points)
============================================================
Enter your choice (1-3): 2

🎮 Starting Medium Game!
I'm thinking of a number between 1 and 100
You have 7 attempts. Good luck!

Enter your guess (Attempts left: 7): 50
💡 Hint: Your guess is TOO LOW. Try a higher number!
Try again! You have 6 attempt(s) left.
```

### **Example 2: Using To-Do List**
```
The task will be saved to tasks.json automatically:
{
    "id": 1,
    "title": "Buy groceries",
    "priority": "high",
    "completed": false,
    "created_at": "2024-04-24 10:30:45"
}
```

### **Example 3: Using Email Validator**
```
Email Analysis Results:
- Full Email: john.doe@example.com
- Status: ✅ VALID
- Username: john.doe
- Domain: example.com
- Provider: Custom Domain
- Email Quality: High (contains dots, numbers, proper format)
```

---

## 🐛 Troubleshooting

### **Issue: "Module not found" error**
✅ Solution: All projects use only standard library. Ensure Python 3.8+ is installed.

### **Issue: Tasks not saving in To-Do List**
✅ Solution: Check write permissions in the directory. `tasks.json` is created automatically.

### **Issue: Email validation always fails**
✅ Solution: Ensure email format is valid. Example: `user@domain.com`

### **Issue: Timer not showing countdown**
✅ Solution: Use Python 3.6+. Some older versions have terminal issues.

---

## 📝 License

This project collection is open source and available for educational purposes.

---

## 💡 Contributing

To contribute improvements:
1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

---

## 🌟 Portfolio Usage

These projects are perfect for your portfolio because they demonstrate:
- ✅ Clean, professional code
- ✅ Advanced Python concepts
- ✅ Problem-solving abilities
- ✅ User experience design
- ✅ Error handling
- ✅ Documentation skills
- ✅ Best practices

Include this README in your GitHub portfolio to showcase your work!

---

## 📞 Support

For questions or issues, please open a GitHub issue or contact the maintainer.

---

## 🎉 Thank You!

Thank you for using these Python mini projects. Happy coding! 🚀

**Last Updated:** April 2024
**Python Version:** 3.8+
**License:** Open Source