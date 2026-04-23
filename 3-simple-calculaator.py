"""
Advanced Calculator
A full-featured calculator with multiple operations, continuous calculation,
and comprehensive error handling.
"""
import math


class AdvancedCalculator:
    """Handles calculator operations and calculations."""
    
    def __init__(self):
        """Initialize calculator with operation history."""
        self.history = []
    
    def add(self, num1: float, num2: float) -> float:
        """Addition operation."""
        return num1 + num2
    
    def subtract(self, num1: float, num2: float) -> float:
        """Subtraction operation."""
        return num1 - num2
    
    def multiply(self, num1: float, num2: float) -> float:
        """Multiplication operation."""
        return num1 * num2
    
    def divide(self, num1: float, num2: float) -> float:
        """Division operation with zero-division handling."""
        if num2 == 0:
            raise ValueError("Cannot divide by zero!")
        return num1 / num2
    
    def modulus(self, num1: float, num2: float) -> float:
        """Modulus operation (remainder)."""
        if num2 == 0:
            raise ValueError("Cannot perform modulus with zero!")
        return num1 % num2
    
    def power(self, num1: float, num2: float) -> float:
        """Exponentiation operation."""
        return num1 ** num2
    
    def square_root(self, num: float) -> float:
        """Calculate square root."""
        if num < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        return math.sqrt(num)
    
    def percentage(self, num1: float, num2: float) -> float:
        """Calculate percentage: what % of num1 is num2."""
        if num1 == 0:
            raise ValueError("Cannot calculate percentage with zero!")
        return (num2 / num1) * 100
    
    def perform_calculation(self, num1: float, operation: str, num2: float = None) -> float:
        """
        Perform a calculation based on operation type.
        
        Args:
            num1: First number
            operation: Operation to perform
            num2: Second number (not needed for square root)
            
        Returns:
            float: Result of calculation
        """
        operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
            "%": self.modulus,
            "**": self.power,
            "√": self.square_root,
            "%of": self.percentage
        }
        
        if operation not in operations:
            raise ValueError(f"Unknown operation: {operation}")
        
        if operation == "√":
            return operations[operation](num1)
        else:
            return operations[operation](num1, num2)
    
    def add_to_history(self, calculation: str, result: float) -> None:
        """Add calculation to history."""
        self.history.append(f"{calculation} = {result}")
    
    def view_history(self) -> None:
        """Display calculation history."""
        if not self.history:
            print("\n📭 No calculation history available!\n")
            return
        
        print("\n" + "=" * 50)
        print("📜 CALCULATION HISTORY")
        print("=" * 50)
        for i, calc in enumerate(self.history, 1):
            print(f"{i}. {calc}")
        print("=" * 50 + "\n")
    
    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history.clear()
        print("✅ History cleared!\n")
    
    def display_menu(self) -> None:
        """Display calculator menu and options."""
        while True:
            print("=" * 50)
            print("🧮 ADVANCED CALCULATOR")
            print("=" * 50)
            print("BASIC OPERATIONS:")
            print("  + (Addition)")
            print("  - (Subtraction)")
            print("  * (Multiplication)")
            print("  / (Division)")
            print("ADVANCED OPERATIONS:")
            print("  % (Modulus/Remainder)")
            print("  ** (Power/Exponentiation)")
            print("  √ (Square Root)")
            print("  %of (Percentage of)")
            print("OTHER:")
            print("  H (View History)")
            print("  C (Clear History)")
            print("  E (Exit)")
            print("=" * 50)
            
            operation = input("Enter operation or command: ").strip().lower()
            
            if operation == "e":
                print("\n👋 Thanks for using the calculator! Goodbye!\n")
                break
            elif operation == "h":
                self.view_history()
                continue
            elif operation == "c":
                self.clear_history()
                continue
            elif operation not in ["+", "-", "*", "/", "%", "**", "√", "%of"]:
                print("❌ Invalid operation! Please try again.\n")
                continue
            
            try:
                # Handle square root (single operand)
                if operation == "√":
                    num1 = float(input("Enter a number: "))
                    result = self.perform_calculation(num1, operation)
                    calculation_str = f"√{num1}"
                else:
                    # Handle two-operand operations
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
                    result = self.perform_calculation(num1, operation, num2)
                    calculation_str = f"{num1} {operation} {num2}"
                
                print(f"\n✅ Result: {result}\n")
                self.add_to_history(calculation_str, result)
                
                # Ask if user wants to continue
                continue_calc = input("Continue calculating? (yes/no): ").lower()
                if continue_calc != "yes":
                    print("\n👋 Thanks for using the calculator! Goodbye!\n")
                    break
                print()
            
            except ValueError as e:
                print(f"❌ Error: {e}\n")
            except Exception as e:
                print(f"❌ Unexpected error: {e}\n")


def main():
    """Entry point of the application."""
    calculator = AdvancedCalculator()
    calculator.display_menu()


if __name__ == "__main__":
    main()
    
    