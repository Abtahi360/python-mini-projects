"""
Advanced Palindrome Checker
Checks if words or sentences are palindromes with detailed analysis
and formatting options.
"""
import re


class PalindromeChecker:
    """Handles palindrome checking logic."""
    
    @staticmethod
    def clean_string(text: str, ignore_spaces_and_punctuation: bool = True) -> str:
        """
        Clean string for palindrome checking.
        
        Args:
            text: Text to clean
            ignore_spaces_and_punctuation: Whether to remove spaces and punctuation
            
        Returns:
            str: Cleaned string
        """
        # Convert to lowercase
        cleaned = text.lower()
        
        if ignore_spaces_and_punctuation:
            # Remove spaces, punctuation, and special characters
            cleaned = re.sub(r'[^a-z0-9]', '', cleaned)
        
        return cleaned
    
    @staticmethod
    def is_palindrome(text: str) -> bool:
        """
        Check if text is a palindrome.
        
        Args:
            text: Text to check
            
        Returns:
            bool: True if palindrome, False otherwise
        """
        cleaned = PalindromeChecker.clean_string(text)
        return cleaned == cleaned[::-1]
    
    @staticmethod
    def reverse_string(text: str) -> str:
        """Reverse a string."""
        return text[::-1]
    
    @staticmethod
    def get_reversed_cleaned(text: str) -> str:
        """Get reversed version of cleaned string."""
        cleaned = PalindromeChecker.clean_string(text)
        return cleaned[::-1]
    
    @staticmethod
    def analyze_palindrome(text: str) -> dict:
        """
        Perform detailed analysis of text for palindrome properties.
        
        Args:
            text: Text to analyze
            
        Returns:
            dict: Analysis results
        """
        cleaned = PalindromeChecker.clean_string(text)
        is_pal = PalindromeChecker.is_palindrome(text)
        
        return {
            "original": text,
            "cleaned": cleaned,
            "reversed": cleaned[::-1],
            "is_palindrome": is_pal,
            "length": len(cleaned),
            "character_count": len(text)
        }
    
    @staticmethod
    def display_menu() -> None:
        """Display menu and handle user interactions."""
        while True:
            print("=" * 60)
            print("🔄 PALINDROME CHECKER")
            print("=" * 60)
            print("1. Check Single Word")
            print("2. Check Sentence/Phrase")
            print("3. Detailed Analysis")
            print("4. Batch Check Multiple Words")
            print("5. Exit")
            print("=" * 60)
            
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == "1":
                PalindromeChecker.check_single_word()
            elif choice == "2":
                PalindromeChecker.check_sentence()
            elif choice == "3":
                PalindromeChecker.detailed_analysis()
            elif choice == "4":
                PalindromeChecker.batch_check()
            elif choice == "5":
                print("\n👋 Thanks for using Palindrome Checker! Goodbye!\n")
                break
            else:
                print("❌ Invalid choice! Please try again.\n")
    
    @staticmethod
    def check_single_word() -> None:
        """Check if a single word is a palindrome."""
        print("\n" + "=" * 60)
        print("CHECK SINGLE WORD")
        print("=" * 60)
        
        word = input("Enter a word: ").strip()
        
        if not word:
            print("❌ Word cannot be empty!\n")
            return
        
        cleaned = PalindromeChecker.clean_string(word)
        reversed_word = cleaned[::-1]
        is_pal = PalindromeChecker.is_palindrome(word)
        
        print(f"\nOriginal: {word}")
        print(f"Cleaned: {cleaned}")
        print(f"Reversed: {reversed_word}")
        
        if is_pal:
            print("✅ YES! This is a PALINDROME! 🎉")
        else:
            print("❌ NO, this is NOT a palindrome.")
        
        print()
    
    @staticmethod
    def check_sentence() -> None:
        """Check if a sentence/phrase is a palindrome."""
        print("\n" + "=" * 60)
        print("CHECK SENTENCE/PHRASE")
        print("=" * 60)
        
        sentence = input("Enter a sentence: ").strip()
        
        if not sentence:
            print("❌ Sentence cannot be empty!\n")
            return
        
        cleaned = PalindromeChecker.clean_string(sentence)
        reversed_sent = cleaned[::-1]
        is_pal = PalindromeChecker.is_palindrome(sentence)
        
        print(f"\nOriginal: {sentence}")
        print(f"Cleaned: {cleaned}")
        print(f"Reversed: {reversed_sent}")
        
        if is_pal:
            print("✅ YES! This is a PALINDROME! 🎉")
        else:
            print("❌ NO, this is NOT a palindrome.")
        
        print()
    
    @staticmethod
    def detailed_analysis() -> None:
        """Perform and display detailed analysis."""
        print("\n" + "=" * 60)
        print("DETAILED ANALYSIS")
        print("=" * 60)
        
        text = input("Enter text to analyze: ").strip()
        
        if not text:
            print("❌ Text cannot be empty!\n")
            return
        
        analysis = PalindromeChecker.analyze_palindrome(text)
        
        print("\n" + "=" * 60)
        print("ANALYSIS RESULTS")
        print("=" * 60)
        print(f"Original Text: {analysis['original']}")
        print(f"Cleaned Text: {analysis['cleaned']}")
        print(f"Reversed Text: {analysis['reversed']}")
        print(f"Length (cleaned): {analysis['length']} characters")
        print(f"Length (original): {analysis['character_count']} characters")
        print(f"Is Palindrome: {'✅ YES' if analysis['is_palindrome'] else '❌ NO'}")
        print("=" * 60 + "\n")
    
    @staticmethod
    def batch_check() -> None:
        """Check multiple words in batch mode."""
        print("\n" + "=" * 60)
        print("BATCH CHECK")
        print("=" * 60)
        print("Enter words separated by commas (e.g., racecar, hello, level)")
        
        words_input = input("Enter words: ").strip()
        
        if not words_input:
            print("❌ No words provided!\n")
            return
        
        words = [word.strip() for word in words_input.split(",")]
        
        print("\n" + "=" * 60)
        print(f"{'Word':<20} {'Cleaned':<20} {'Result':<15}")
        print("=" * 60)
        
        for word in words:
            if word:
                cleaned = PalindromeChecker.clean_string(word)
                is_pal = PalindromeChecker.is_palindrome(word)
                result = "✅ PALINDROME" if is_pal else "❌ NOT"
                print(f"{word:<20} {cleaned:<20} {result:<15}")
        
        print("=" * 60 + "\n")


def main():
    """Entry point of the application."""
    PalindromeChecker.display_menu()


if __name__ == "__main__":
    main()
