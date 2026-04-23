"""
Number Guessing Game with Difficulty Levels
A fun guessing game with hints, scoring, and multiple difficulty modes.
"""
import random


class NumberGuessingGame:
    """Manages the number guessing game logic and scoring."""
    
    def __init__(self):
        """Initialize game statistics."""
        self.total_score = 0
        self.games_won = 0
        self.games_played = 0
        self.difficulty_levels = {
            "easy": {"range": (1, 50), "attempts": 10, "points": 10},
            "medium": {"range": (1, 100), "attempts": 7, "points": 25},
            "hard": {"range": (1, 500), "attempts": 5, "points": 50}
        }
    
    def select_difficulty(self) -> dict:
        """
        Display difficulty menu and return selected difficulty settings.
        
        Returns:
            dict: Difficulty settings (range, attempts, points)
        """
        print("\n" + "=" * 50)
        print("SELECT DIFFICULTY LEVEL")
        print("=" * 50)
        print("1. Easy   (1-50, 10 attempts, 10 points)")
        print("2. Medium (1-100, 7 attempts, 25 points)")
        print("3. Hard   (1-500, 5 attempts, 50 points)")
        print("=" * 50)
        
        while True:
            choice = input("Enter your choice (1-3): ").strip()
            if choice == "1":
                return self.difficulty_levels["easy"], "Easy"
            elif choice == "2":
                return self.difficulty_levels["medium"], "Medium"
            elif choice == "3":
                return self.difficulty_levels["hard"], "Hard"
            else:
                print("❌ Invalid choice! Please enter 1, 2, or 3.")
    
    def get_hint(self, secret_number: int, guess: int) -> str:
        """
        Generate a helpful hint based on the guess.
        
        Args:
            secret_number: The number to be guessed
            guess: The player's guess
            
        Returns:
            str: A helpful hint message
        """
        if guess < secret_number:
            return "💡 Hint: Your guess is TOO LOW. Try a higher number!"
        else:
            return "💡 Hint: Your guess is TOO HIGH. Try a lower number!"
    
    def play_round(self):
        """Execute a single game round."""
        settings, difficulty_name = self.select_difficulty()
        number_range = settings["range"]
        max_attempts = settings["attempts"]
        points = settings["points"]
        
        secret_number = random.randint(number_range[0], number_range[1])
        attempts_remaining = max_attempts
        self.games_played += 1
        
        print(f"\n🎮 Starting {difficulty_name} Game!")
        print(f"I'm thinking of a number between {number_range[0]} and {number_range[1]}")
        print(f"You have {max_attempts} attempts. Good luck!\n")
        
        while attempts_remaining > 0:
            try:
                guess = int(input(f"Enter your guess (Attempts left: {attempts_remaining}): "))
                
                # Validate input range
                if guess < number_range[0] or guess > number_range[1]:
                    print(f"❌ Please enter a number between {number_range[0]} and {number_range[1]}!")
                    continue
                
                if guess == secret_number:
                    self.games_won += 1
                    self.total_score += points
                    print(f"\n🎉 CONGRATULATIONS! You guessed it correctly!")
                    print(f"The number was {secret_number}")
                    print(f"✅ You earned {points} points!")
                    print(f"📊 Total Score: {self.total_score}\n")
                    return
                else:
                    # Provide a hint
                    hint = self.get_hint(secret_number, guess)
                    print(hint)
                    attempts_remaining -= 1
                    
                    if attempts_remaining > 0:
                        print(f"Try again! You have {attempts_remaining} attempt(s) left.\n")
                    
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.\n")
                continue
        
        # Game over - out of attempts
        print(f"\n💀 GAME OVER! You ran out of attempts.")
        print(f"The correct number was {secret_number}")
        print(f"Better luck next time!\n")
    
    def display_stats(self):
        """Display player statistics."""
        if self.games_played == 0:
            print("\nNo games played yet!")
            return
        
        win_rate = (self.games_won / self.games_played) * 100
        print("\n" + "=" * 50)
        print("📊 GAME STATISTICS")
        print("=" * 50)
        print(f"Games Played: {self.games_played}")
        print(f"Games Won: {self.games_won}")
        print(f"Win Rate: {win_rate:.1f}%")
        print(f"Total Score: {self.total_score}")
        print("=" * 50 + "\n")
    
    def main_menu(self):
        """Display main menu and handle user choices."""
        while True:
            print("=" * 50)
            print("🎯 NUMBER GUESSING GAME")
            print("=" * 50)
            print("1. Play Game")
            print("2. View Statistics")
            print("3. Exit")
            print("=" * 50)
            
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == "1":
                self.play_round()
            elif choice == "2":
                self.display_stats()
            elif choice == "3":
                print("Thanks for playing! Goodbye! 👋\n")
                break
            else:
                print("❌ Invalid choice! Please try again.\n")


def main():
    """Entry point of the application."""
    game = NumberGuessingGame()
    game.main_menu()


if __name__ == "__main__":
    main()
