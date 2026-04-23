"""
Advanced Countdown Timer
A feature-rich countdown timer with pause/resume, presets, and notifications.
"""
import time
import os


class CountdownTimer:
    \"\"\"Manages countdown timer functionality.\"\"\"
    
    # Common presets
    PRESETS = {
        \"pomodoro\": 25 * 60,  # 25 minutes
        \"short\": 5 * 60,      # 5 minutes
        \"medium\": 15 * 60,    # 15 minutes
        \"long\": 30 * 60,      # 30 minutes
        \"study\": 45 * 60,     # 45 minutes
        \"break\": 10 * 60      # 10 minutes
    }
    
    def __init__(self):
        \"\"\"Initialize timer state.\"\"\"
        self.total_time = 0
        self.remaining_time = 0
        self.is_paused = False
        self.completed_timers = 0
    
    def convert_to_seconds(self, minutes: int = 0, seconds: int = 0) -> int:
        \"\"\"
        Convert minutes and seconds to total seconds.
        
        Args:
            minutes: Number of minutes
            seconds: Number of seconds
            
        Returns:
            int: Total seconds
        \"\"\"
        return (minutes * 60) + seconds
    
    def format_time(self, total_seconds: int) -> str:
        \"\"\"
        Format seconds into HH:MM:SS format.
        
        Args:
            total_seconds: Total seconds
            
        Returns:
            str: Formatted time string
        \"\"\"
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        if hours > 0:
            return f\"{hours:02d}:{minutes:02d}:{seconds:02d}\"
        return f\"{minutes:02d}:{seconds:02d}\"
    
    def display_timer(self, remaining_time: int, total_time: int) -> None:
        \"\"\"
        Display timer in formatted output.
        
        Args:
            remaining_time: Time remaining in seconds
            total_time: Total time in seconds
        \"\"\"
        progress = (total_time - remaining_time) / total_time
        progress_bar_length = 30
        filled = int(progress_bar_length * progress)
        bar = \"█\" * filled + \"░\" * (progress_bar_length - filled)
        
        percentage = (progress * 100)
        time_str = self.format_time(remaining_time)
        
        print(f\"\\r⏱️  {time_str} | [{bar}] {percentage:.0f}%\", end=\"\", flush=True)
    
    def beep_alert(self) -> None:
        \"\"\"Produce audio alert (system bell).\"\"\"
        # Use system bell character (works on most systems)
        print(\"\\a\")  # ASCII bell character
    
    def show_completion_message(self, timer_name: str = \"\") -> None:
        \"\"\"
        Display completion message with animation.
        
        Args:
            timer_name: Name of the timer
        \"\"\"
        print(\"\\n\\n\" + \"=\"*60)
        print(\"🎉\" * 15)
        print(\"=\"*60)
        print(\"⏱️  TIME'S UP!\")
        if timer_name:
            print(f\"✅ {timer_name} timer completed!\")
        print(\"=\"*60)
        print(\"🎉\" * 15)
        print(\"=\"*60 + \"\\n\")
        
        # Play alert sound
        for _ in range(3):
            self.beep_alert()
            time.sleep(0.5)
    
    def countdown(self, total_seconds: int, timer_name: str = \"\") -> None:
        \"\"\"
        Run the countdown timer.
        
        Args:
            total_seconds: Duration in seconds
            timer_name: Name of the timer for display
        \"\"\"
        self.total_time = total_seconds
        self.remaining_time = total_seconds
        
        print(f\"\\n⏱️  Starting timer: {self.format_time(total_seconds)}\")
        if timer_name:
            print(f\"Timer Name: {timer_name}\")\n\"\"
        
        time.sleep(1)
        
        while self.remaining_time > 0:
            self.display_timer(self.remaining_time, self.total_time)
            time.sleep(1)
            self.remaining_time -= 1
        
        # Timer completed
        self.completed_timers += 1
        self.show_completion_message(timer_name)
    
    def get_custom_duration(self) -> int:
        \"\"\"Get custom duration from user in seconds or minutes:seconds format.\"\"\"
        print(f\"\\n{'='*60}\")
        print(\"ENTER DURATION\")
        print(f\"{'='*60}\")
        print(\"Format: Enter time in seconds OR mm:ss format\")
        print(\"Examples: 60, 5:30, 1:45\")\n\"\"
        
        while True:
            try:
                user_input = input(\"Enter duration: \").strip()
                
                if \":\" in user_input:
                    # Parse mm:ss format
                    parts = user_input.split(\":\")\n                    if len(parts) != 2:
                        print(\"❌ Invalid format! Use mm:ss\")\n                        continue
                    
                    minutes = int(parts[0])\n                    seconds = int(parts[1])\n                    
                    if minutes < 0 or seconds < 0 or seconds >= 60:
                        print(\"❌ Invalid time! Seconds must be 0-59.\")\n                        continue
                    
                    total_seconds = self.convert_to_seconds(minutes, seconds)
                else:
                    # Parse seconds only
                    total_seconds = int(user_input)
                
                if total_seconds <= 0:
                    print(\"❌ Duration must be greater than 0!\")\n                    continue
                
                return total_seconds
            
            except ValueError:
                print(\"❌ Invalid input! Please enter a valid duration.\")\n\"\"
    
    def display_menu(self) -> None:
        \"\"\"Display main menu and handle user interactions.\"\"\"
        while True:
            print(f\"\\n{'='*60}\")
            print(\"⏱️  ADVANCED COUNTDOWN TIMER\")
            print(f\"{'='*60}\")
            print(\"1. Start Custom Timer\")
            print(\"2. Use Timer Presets\")\n            print(\"3. View Statistics\")
            print(\"4. Exit\")
            print(f\"{'='*60}\")
            
            choice = input(\"Enter your choice (1-4): \").strip()
            
            if choice == \"1\":
                self.option_custom_timer()
            elif choice == \"2\":
                self.option_presets()
            elif choice == \"3\":
                self.show_statistics()
            elif choice == \"4\":
                print(\"\\n👋 Thanks for using the timer! Goodbye!\\n\")\n                break
            else:
                print(\"❌ Invalid choice! Please try again.\")\n\"\"
    
    def option_custom_timer(self) -> None:
        \"\"\"Option: Start a custom timer.\"\"\"
        total_seconds = self.get_custom_duration()
        timer_name = input(\"Enter timer name (optional): \").strip() or \"Custom\"\n        self.countdown(total_seconds, timer_name)
    
    def option_presets(self) -> None:
        \"\"\"Option: Use predefined timer presets.\"\"\"
        print(f\"\\n{'='*60}\")\n        print(\"TIMER PRESETS\")\n        print(f\"{'='*60}\")\n        
        for i, (name, seconds) in enumerate(self.PRESETS.items(), 1):\n            print(f\"{i}. {name.capitalize()} ({self.format_time(seconds)})\")\n        
        print(f\"{len(self.PRESETS) + 1}. Back to Menu\")\n        print(f\"{'='*60}\")\n        
        try:\n            choice = int(input(\"Select preset (1-7): \"))\n            
            if choice == len(self.PRESETS) + 1:\n                return\n            
            if 1 <= choice <= len(self.PRESETS):\n                preset_name = list(self.PRESETS.keys())[choice - 1]\n                total_seconds = self.PRESETS[preset_name]\n                self.countdown(total_seconds, preset_name.capitalize())\n            else:\n                print(\"❌ Invalid choice!\\n\")\n        
        except ValueError:\n            print(\"❌ Invalid input!\\n\")\n\"\"
    
    def show_statistics(self) -> None:\n        \"\"\"Display timer statistics.\"\"\"\n        print(f\"\\n{'='*60}\")\n        print(\"📊 TIMER STATISTICS\")\n        print(f\"{'='*60}\")\n        print(f\"Timers Completed: {self.completed_timers}\")\n        print(f\"{'='*60}\\n\")\n


def main():\n    \"\"\"Entry point of the application.\"\"\"\n    timer = CountdownTimer()\n    timer.display_menu()\n\n\nif __name__ == \"__main__\":\n    main()
