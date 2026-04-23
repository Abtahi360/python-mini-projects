"""
Advanced Fibonacci Sequence Generator
Generates Fibonacci sequences using iterative, recursive, and memoization methods.
Includes performance comparison and visualization.
"""
import time
from functools import lru_cache


class FibonacciGenerator:
    \"\"\"Generates Fibonacci sequences using different methods.\"\"\"
    
    @staticmethod
    def iterative_fibonacci(count: int) -> list:
        \"\"\"
        Generate Fibonacci sequence using iterative approach.
        
        Args:
            count: Number of Fibonacci numbers to generate
            
        Returns:
            list: Fibonacci sequence
        \"\"\"
        if count <= 0:
            return []
        elif count == 1:
            return [0]
        
        sequence = [0, 1]
        for i in range(2, count):
            next_num = sequence[i - 1] + sequence[i - 2]
            sequence.append(next_num)
        
        return sequence[:count]
    
    @staticmethod
    @lru_cache(maxsize=None)
    def recursive_fibonacci_memoized(n: int) -> int:
        \"\"\"
        Calculate nth Fibonacci number using recursion with memoization.
        
        Args:
            n: Position in Fibonacci sequence (0-indexed)
            
        Returns:
            int: nth Fibonacci number
        \"\"\"
        if n <= 1:
            return n
        return FibonacciGenerator.recursive_fibonacci_memoized(n - 1) + \
               FibonacciGenerator.recursive_fibonacci_memoized(n - 2)
    
    @staticmethod
    def recursive_fibonacci_pure(n: int) -> int:
        \"\"\"
        Calculate nth Fibonacci number using pure recursion (slower).
        
        Args:
            n: Position in Fibonacci sequence (0-indexed)
            
        Returns:
            int: nth Fibonacci number
        \"\"\"
        if n <= 1:
            return n
        return FibonacciGenerator.recursive_fibonacci_pure(n - 1) + \
               FibonacciGenerator.recursive_fibonacci_pure(n - 2)
    
    @staticmethod
    def generate_by_range(start: int, end: int) -> list:
        \"\"\"
        Generate Fibonacci sequence from index start to end.
        
        Args:
            start: Starting index (0-indexed)
            end: Ending index (inclusive)
            
        Returns:
            list: Fibonacci numbers in range
        \"\"\"
        if start < 0 or end < start:
            return []
        
        sequence = []
        for i in range(start, end + 1):
            sequence.append(FibonacciGenerator.recursive_fibonacci_memoized(i))
        
        return sequence
    
    @staticmethod
    def get_nth_fibonacci(n: int) -> int:
        \"\"\"Get the nth Fibonacci number efficiently.\"\"\"
        return FibonacciGenerator.recursive_fibonacci_memoized(n)
    
    @staticmethod
    def performance_comparison(count: int) -> None:
        \"\"\"
        Compare performance of different Fibonacci methods.
        
        Args:
            count: Number of Fibonacci numbers to generate
        \"\"\"
        print(f\"\\n{'='*70}\")
        print(\"⏱️  PERFORMANCE COMPARISON\")
        print(f\"{'='*70}\")
        print(f\"Generating first {count} Fibonacci numbers...\\n\")
        
        # Iterative method
        start = time.time()
        iterative_result = FibonacciGenerator.iterative_fibonacci(count)
        iterative_time = time.time() - start
        
        # Memoized recursive method
        start = time.time()
        memoized_result = [FibonacciGenerator.recursive_fibonacci_memoized(i) 
                          for i in range(count)]
        memoized_time = time.time() - start
        
        print(f\"Iterative Method: {iterative_time:.6f} seconds\")
        print(f\"Memoized Recursive: {memoized_time:.6f} seconds\")
        
        if iterative_time < memoized_time:
            ratio = memoized_time / iterative_time
            print(f\"✅ Iterative is {ratio:.2f}x faster!\")
        else:
            ratio = iterative_time / memoized_time
            print(f\"✅ Memoized is {ratio:.2f}x faster!\")
        
        print(f\"{'='*70}\\n\")
    
    @staticmethod
    def display_menu() -> None:
        \"\"\"Display menu and handle user interactions.\"\"\"
        while True:
            print(f\"{'='*60}\")
            print(\"📊 FIBONACCI SEQUENCE GENERATOR\")
            print(f\"{'='*60}\")
            print(\"1. Generate First N Numbers (Iterative)\")
            print(\"2. Get Nth Fibonacci Number (Memoized)\")
            print(\"3. Generate Range of Numbers\")
            print(\"4. Performance Comparison\")
            print(\"5. Clear Memoization Cache\")
            print(\"6. Exit\")
            print(f\"{'='*60}\")
            
            choice = input(\"Enter your choice (1-6): \").strip()
            
            if choice == \"1\":
                FibonacciGenerator.option_generate_first_n()
            elif choice == \"2\":
                FibonacciGenerator.option_get_nth()
            elif choice == \"3\":
                FibonacciGenerator.option_generate_range()
            elif choice == \"4\":
                FibonacciGenerator.option_performance()
            elif choice == \"5\":
                FibonacciGenerator.recursive_fibonacci_memoized.cache_clear()
                print(\"✅ Cache cleared!\\n\")
            elif choice == \"6\":
                print(\"\\n👋 Thanks for using Fibonacci Generator! Goodbye!\\n\")
                break
            else:
                print(\"❌ Invalid choice! Please try again.\\n\")
    
    @staticmethod
    def option_generate_first_n() -> None:
        \"\"\"Option: Generate first N Fibonacci numbers.\"\"\"
        print(f\"\\n{'='*60}\")
        print(\"GENERATE FIRST N FIBONACCI NUMBERS\")
        print(f\"{'='*60}\")
        
        try:
            count = int(input(\"How many Fibonacci numbers? \"))
            if count < 0:
                print(\"❌ Please enter a positive number!\\n\")
                return
            
            if count == 0:
                print(\"❌ Please enter at least 1!\\n\")
                return
            
            sequence = FibonacciGenerator.iterative_fibonacci(count)
            
            print(f\"\\nFirst {count} Fibonacci Numbers:\")
            print(f\"{'='*60}\")
            
            # Display in formatted rows
            for i in range(0, len(sequence), 10):
                row = sequence[i:i+10]
                print(\" \".join(f\"{num:>10}\" for num in row))
            
            print(f\"{'='*60}\\n\")
        
        except ValueError:
            print(\"❌ Invalid input! Please enter a number.\\n\")
    
    @staticmethod
    def option_get_nth() -> None:
        \"\"\"Option: Get the Nth Fibonacci number.\"\"\"
        print(f\"\\n{'='*60}\")
        print(\"GET NTH FIBONACCI NUMBER\")
        print(f\"{'='*60}\")
        
        try:
            n = int(input(\"Enter position (0-indexed): \"))
            if n < 0:
                print(\"❌ Position must be non-negative!\\n\")
                return
            
            start = time.time()
            result = FibonacciGenerator.get_nth_fibonacci(n)
            elapsed = time.time() - start
            
            print(f\"\\nFibonacci({n}) = {result}\")
            print(f\"Computed in: {elapsed:.6f} seconds\\n\")
        
        except ValueError:
            print(\"❌ Invalid input! Please enter a number.\\n\")
    
    @staticmethod
    def option_generate_range() -> None:
        \"\"\"Option: Generate range of Fibonacci numbers.\"\"\"
        print(f\"\\n{'='*60}\")
        print(\"GENERATE RANGE OF FIBONACCI NUMBERS\")
        print(f\"{'='*60}\")
        
        try:
            start = int(input(\"Enter start position (0-indexed): \"))
            end = int(input(\"Enter end position (0-indexed, inclusive): \"))
            
            if start < 0 or end < 0:
                print(\"❌ Positions must be non-negative!\\n\")
                return
            
            if start > end:
                print(\"❌ Start position must be <= end position!\\n\")
                return
            
            sequence = FibonacciGenerator.generate_by_range(start, end)
            
            print(f\"\\nFibonacci numbers from position {start} to {end}:\")
            print(f\"{'='*60}\")
            for i, num in enumerate(sequence, start):
                print(f\"F({i}) = {num}\")
            print(f\"{'='*60}\\n\")
        
        except ValueError:
            print(\"❌ Invalid input! Please enter numbers.\\n\")
    
    @staticmethod
    def option_performance() -> None:
        \"\"\"Option: Show performance comparison.\"\"\"
        try:
            count = int(input(\"\\nHow many numbers for comparison? (1-30): \"))
            if count < 1 or count > 30:
                print(\"❌ Please enter between 1 and 30!\\n\")
                return
            
            FibonacciGenerator.performance_comparison(count)
        
        except ValueError:
            print(\"❌ Invalid input! Please enter a number.\\n\")


def main():
    \"\"\"Entry point of the application.\"\"\"
    generator = FibonacciGenerator()
    FibonacciGenerator.display_menu()


if __name__ == \"__main__\":
    main()
