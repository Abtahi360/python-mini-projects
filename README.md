# 🐍 Python Mini Projects - Advanced Portfolio Edition

This repository contains 10 beginner-friendly Python projects, covering various fundamental programming concepts such as loops, conditionals, functions, and file handling. Each project is designed to help improve problem-solving skills and reinforce Python basics.

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

## 📞 Support

For questions or issues, please open a GitHub issue or contact the maintainer.

---

## 🎉 Thank You!

Thank you for using these Python mini projects. Happy coding! 🚀

**Last Updated:** April 2024
**Python Version:** 3.8+
**License:** Open Source
