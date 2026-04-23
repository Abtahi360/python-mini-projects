"""
Advanced Password Generator
Generates strong, customizable passwords with strength checking
and security recommendations.
"""
import random
import string


class PasswordGenerator:
    \"\"\"Handles password generation and validation.\"\"\"
    
    def __init__(self):
        \"\"\"Initialize character sets.\"\"\"
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.special = string.punctuation
    
    def generate_password(self,
                         length: int,
                         use_lowercase: bool = True,
                         use_uppercase: bool = True,
                         use_digits: bool = True,
                         use_special: bool = False) -> str:
        \"\"\"
        Generate a random password with specified criteria.
        
        Args:
            length: Password length
            use_lowercase: Include lowercase letters
            use_uppercase: Include uppercase letters
            use_digits: Include digits
            use_special: Include special characters
            
        Returns:
            str: Generated password
        \"\"\"
        if length < 4:
            raise ValueError(\"Password length must be at least 4 characters!\")
        
        # Build character pool
        char_pool = \"\"
        
        if use_lowercase:
            char_pool += self.lowercase
        if use_uppercase:
            char_pool += self.uppercase
        if use_digits:
            char_pool += self.digits
        if use_special:
            char_pool += self.special
        
        if not char_pool:
            raise ValueError(\"At least one character type must be selected!\")
        
        # Generate password
        password = ''.join(random.choice(char_pool) for _ in range(length))
        return password
    
    def generate_strong_password(self, length: int = 16) -> str:
        \"\"\"Generate a strong password with all character types.\"\"\"
        return self.generate_password(
            length,
            use_lowercase=True,
            use_uppercase=True,
            use_digits=True,
            use_special=True
        )
    
    def check_password_strength(self, password: str) -> dict:
        \"\"\"
        Evaluate password strength.
        
        Args:
            password: Password to evaluate
            
        Returns:
            dict: Strength analysis
        \"\"\"
        analysis = {
            \"length\": len(password),
            \"has_lowercase\": any(c.islower() for c in password),
            \"has_uppercase\": any(c.isupper() for c in password),
            \"has_digits\": any(c.isdigit() for c in password),
            \"has_special\": any(c in self.special for c in password),
        }
        
        # Calculate strength score
        score = 0
        if analysis[\"length\"] >= 8:
            score += 1
        if analysis[\"length\"] >= 12:
            score += 1
        if analysis[\"has_lowercase\"]:
            score += 1
        if analysis[\"has_uppercase\"]:
            score += 1
        if analysis[\"has_digits\"]:
            score += 1
        if analysis[\"has_special\"]:
            score += 2
        
        # Determine strength level
        if score <= 2:
            strength = \"❌ WEAK\"
        elif score <= 4:
            strength = \"⚠️  FAIR\"
        elif score <= 6:
            strength = \"✅ GOOD\"
        else:
            strength = \"🔒 STRONG\"
        
        analysis[\"score\"] = score
        analysis[\"strength\"] = strength
        
        return analysis
    
    def display_strength_analysis(self, password: str) -> None:
        \"\"\"Display detailed password strength analysis.\"\"\"
        analysis = self.check_password_strength(password)
        
        print(f\"\\n{'='*60}\")
        print(\"PASSWORD STRENGTH ANALYSIS\")
        print(f\"{'='*60}\")
        print(f\"Password: {'*' * len(password)}\")
        print(f\"Length: {analysis['length']} characters\")
        print(f\"Strength: {analysis['strength']}\")
        print(f\"Score: {analysis['score']}/8\")
        print()
        print(\"Contains:\")\n        print(f\"  {'✓' if analysis['has_lowercase'] else '✗'} Lowercase letters (a-z)\")\n        print(f\"  {'✓' if analysis['has_uppercase'] else '✗'} Uppercase letters (A-Z)\")\n        print(f\"  {'✓' if analysis['has_digits'] else '✗'} Digits (0-9)\")\n        print(f\"  {'✓' if analysis['has_special'] else '✗'} Special characters (!@#$...)\")\n        print(f\"{'='*60}\\n\")\n\"\"
        # Provide recommendations\n        if analysis[\"strength\"] in [\"❌ WEAK\", \"⚠️  FAIR\"]:\n            print(\"💡 RECOMMENDATIONS TO IMPROVE:\")\n            if analysis[\"length\"] < 12:\n                print(\"  • Increase password length to at least 12 characters\")\n            if not analysis[\"has_uppercase\"]:\n                print(\"  • Add uppercase letters (A-Z)\")\n            if not analysis[\"has_digits\"]:\n                print(\"  • Add numbers (0-9)\")\n            if not analysis[\"has_special\"]:\n                print(\"  • Add special characters (!@#$...)\")\n            print()\n\"\"
    
    def display_menu(self) -> None:\n        \"\"\"Display main menu and handle user interactions.\"\"\"\n        while True:\n            print(f\"\\n{'='*60}\")\n            print(\"🔐 ADVANCED PASSWORD GENERATOR\")\n            print(f\"{'='*60}\")\n            print(\"1. Generate Custom Password\")\n            print(\"2. Generate Strong Password (16 chars)\")\n            print(\"3. Check Password Strength\")\n            print(\"4. Generate Batch Passwords\")\n            print(\"5. Exit\")\n            print(f\"{'='*60}\")\n            
            choice = input(\"Enter your choice (1-5): \").strip()
            
            if choice == \"1\":\n                self.option_custom_password()\n            elif choice == \"2\":\n                self.option_strong_password()\n            elif choice == \"3\":\n                self.option_check_strength()\n            elif choice == \"4\":\n                self.option_batch_passwords()\n            elif choice == \"5\":\n                print(\"\\n👋 Thanks for using Password Generator! Goodbye!\\n\")\n                break\n            else:\n                print(\"❌ Invalid choice! Please try again.\\n\")\n\"\"
    
    def option_custom_password(self) -> None:\n        \"\"\"Option: Generate a custom password.\"\"\"\n        print(f\"\\n{'='*60}\")\n        print(\"CUSTOM PASSWORD GENERATOR\")\n        print(f\"{'='*60}\")\n        
        try:\n            length = int(input(\"Enter desired password length (4-128): \"))\n            if not 4 <= length <= 128:\n                print(\"❌ Length must be between 4 and 128!\\n\")\n                return\n            
            print(\"\\nSelect character types to include:\")\n            use_lower = input(\"Include lowercase letters? (yes/no): \").lower() == \"yes\"\n            use_upper = input(\"Include uppercase letters? (yes/no): \").lower() == \"yes\"\n            use_digits = input(\"Include digits? (yes/no): \").lower() == \"yes\"\n            use_special = input(\"Include special characters? (yes/no): \").lower() == \"yes\"\n            
            if not any([use_lower, use_upper, use_digits, use_special]):\n                print(\"❌ Select at least one character type!\\n\")\n                return\n            
            password = self.generate_password(\n                length,\n                use_lowercase=use_lower,\n                use_uppercase=use_upper,\n                use_digits=use_digits,\n                use_special=use_special\n            )\n            
            print(f\"\\n{'='*60}\")\n            print(f\"Generated Password: {password}\")\n            print(f\"{'='*60}\\n\")\n            
            # Optionally check strength\n            if input(\"Check password strength? (yes/no): \").lower() == \"yes\":\n                self.display_strength_analysis(password)\n        
        except ValueError:\n            print(\"❌ Invalid input! Please try again.\\n\")\n\"\"
    
    def option_strong_password(self) -> None:\n        \"\"\"Option: Generate a strong preset password.\"\"\"\n        print(f\"\\n{'='*60}\")\n        print(\"STRONG PASSWORD GENERATOR\")\n        print(f\"{'='*60}\")\n        
        try:\n            length = int(input(\"Enter desired password length (8-128) [default: 16]: \") or \"16\")\n            if not 8 <= length <= 128:\n                print(\"❌ Length must be between 8 and 128!\\n\")\n                return\n            
            password = self.generate_strong_password(length)\n            \n            print(f\"\\n{'='*60}\")\n            print(f\"Generated Strong Password: {password}\")\n            print(f\"{'='*60}\\n\")\n            
            self.display_strength_analysis(password)\n        
        except ValueError:\n            print(\"❌ Invalid input! Please try again.\\n\")\n\"\"
    
    def option_check_strength(self) -> None:\n        \"\"\"Option: Check password strength.\"\"\"\n        print(f\"\\n{'='*60}\")\n        print(\"PASSWORD STRENGTH CHECKER\")\n        print(f\"{'='*60}\")\n        
        password = input(\"Enter password to check: \").strip()\n        if not password:\n            print(\"❌ Password cannot be empty!\\n\")\n            return\n        
        self.display_strength_analysis(password)\n\"\"
    
    def option_batch_passwords(self) -> None:\n        \"\"\"Option: Generate multiple passwords.\"\"\"\n        print(f\"\\n{'='*60}\")\n        print(\"BATCH PASSWORD GENERATOR\")\n        print(f\"{'='*60}\")\n        
        try:\n            count = int(input(\"How many passwords? (1-10): \"))\n            if not 1 <= count <= 10:\n                print(\"❌ Generate between 1 and 10 passwords!\\n\")\n                return\n            
            length = int(input(\"Password length (8-32) [default: 16]: \") or \"16\")\n            if not 8 <= length <= 32:\n                print(\"❌ Length must be between 8 and 32!\\n\")\n                return\n            
            print(f\"\\n{'='*60}\")\n            print(f\"Generated {count} Strong Passwords:\")\n            print(f\"{'='*60}\")\n            
            for i in range(1, count + 1):\n                password = self.generate_strong_password(length)\n                print(f\"{i:2d}. {password}\")\n            
            print(f\"{'='*60}\\n\")\n        
        except ValueError:\n            print(\"❌ Invalid input! Please try again.\\n\")\n\"\"


def main():\n    \"\"\"Entry point of the application.\"\"\"\n    generator = PasswordGenerator()\n    generator.display_menu()\n\n\nif __name__ == \"__main__\":\n    main()
    
