import re
import math
from collections import Counter

def calculate_entropy(password):
    """Calculate the entropy of a password."""
    length = len(password)
    if length == 0:
        return 0
    freq = Counter(password)
    entropy = 0
    for count in freq.values():
        prob = count / length
        entropy -= prob * math.log2(prob)
    return entropy * length

def check_length(password):
    """Check if the password meets the length requirement."""
    min_length = 8
    if len(password) < min_length:
        return False, f"Password should be at least {min_length} characters long."
    return True, None

def check_complexity(password):
    """Check the complexity of the password."""
    checks = {
        "lowercase": re.compile(r'[a-z]'),
        "uppercase": re.compile(r'[A-Z]'),
        "digits": re.compile(r'\d'),
        "special_chars": re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    }
    
    missing = [key for key, regex in checks.items() if not regex.search(password)]
    
    if missing:
        return False, f"Password should include: {', '.join(missing)}."
    return True, None

def check_uniqueness(password):
    """Check if the password is unique."""
    common_passwords = {"password", "123456", "123456789", "qwerty", "abc123", "password1", "12345678", "12345", "1234567", "admin"}
    if password.lower() in common_passwords:
        return False, "Password is too common. \n- Please choose a different password."
    return True, None

def assess_password_strength(password):
    """Assess the strength of a given password."""
    results = []
    
    # Check length
    length_ok, length_msg = check_length(password)
    if not length_ok:
        results.append(length_msg)
    
    # Check complexity
    complexity_ok, complexity_msg = check_complexity(password)
    if not complexity_ok:
        results.append(complexity_msg)
    
    # Check uniqueness
    uniqueness_ok, uniqueness_msg = check_uniqueness(password)
    if not uniqueness_ok:
        results.append(uniqueness_msg)
    
    # Check entropy
    entropy = calculate_entropy(password)
    if entropy < 40:
        results.append("Password entropy is low. \n- Consider using a more complex password.")
    
    # Provide feedback
    if not results:
        results.append("Password is strong.")
    return results

def main():
    print("Welcome  To PSC\n")
    password = input("Enter a password to assess: ")
    feedback = assess_password_strength(password)
    print("\nPassword Strength Assessment:")
    for line in feedback:
        print(f"- {line}")

if __name__ == "__main__":
    main()
