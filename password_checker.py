import re
import math
import string

def check_length(password):
    length = len(password)
    if length >= 16:
        return 3, "Excellent length (16+ chars)"
    elif length >= 12:
        return 2, "Good length (12-15 chars)"
    elif length >= 8:
        return 1, "Minimum length (8-11 chars)"
    else:
        return 0, "Too short (less than 8 chars)"

def check_uppercase(password):
    if re.search(r'[A-Z]', password):
        return 1, "Has uppercase letters"
    return 0, "Missing uppercase letters"

def check_lowercase(password):
    if re.search(r'[a-z]', password):
        return 1, "Has lowercase letters"
    return 0, "Missing lowercase letters"

def check_digits(password):
    count = sum(1 for c in password if c.isdigit())
    if count >= 2:
        return 2, f"Has {count} digits (great)"
    elif count == 1:
        return 1, "Has 1 digit (add more)"
    return 0, "No digits found"

def check_special_chars(password):
    special = re.findall(r'[!@#$%^&*()_+\-=\[\]{};\'":,.<>?/\\|`~]', password)
    if len(special) >= 2:
        return 2, f"Has {len(special)} special characters (great)"
    elif len(special) == 1:
        return 1, "Has 1 special character (add more)"
    return 0, "No special characters"

def check_common_patterns(password):
    common_passwords = [
        "password", "123456", "password123", "admin", "letmein",
        "qwerty", "abc123", "monkey", "1234567890", "iloveyou",
        "welcome", "login", "passw0rd", "master", "hello"
    ]
    if password.lower() in common_passwords:
        return -2, "Very common password — easily guessed!"

    if re.search(r'(.)\1{2,}', password):
        return -1, "Repeated characters detected (e.g. aaa, 111)"

    if re.search(r'(012|123|234|345|456|567|678|789|890|abc|bcd|cde|def)', password.lower()):
        return -1, "Sequential characters detected (e.g. 123, abc)"

    return 0, "No common patterns detected"

def calculate_entropy(password):
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'[0-9]', password): charset += 10
    if re.search(r'[^a-zA-Z0-9]', password): charset += 32

    if charset == 0:
        return 0
    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

def get_strength_label(score):
    if score <= 2:
        return "VERY WEAK", "🔴"
    elif score <= 4:
        return "WEAK", "🟠"
    elif score <= 6:
        return "MODERATE", "🟡"
    elif score <= 8:
        return "STRONG", "🟢"
    else:
        return "VERY STRONG", "✅"

def check_password(password):
    print("\n" + "="*55)
    print("         PASSWORD STRENGTH CHECKER")
    print("="*55)
    print(f"  Password: {'*' * len(password)}  (length: {len(password)})")
    print("-"*55)

    total_score = 0
    suggestions = []

    # Run all checks
    checks = [
        check_length(password),
        check_uppercase(password),
        check_lowercase(password),
        check_digits(password),
        check_special_chars(password),
        check_common_patterns(password),
    ]

    print("\n  ANALYSIS:")
    for score, message in checks:
        total_score += score
        icon = "✔" if score > 0 else ("⚠" if score == 0 else "✘")
        print(f"   {icon}  {message}")
        if score <= 0 and "Missing" in message:
            suggestions.append(f"Add {message.replace('Missing ', '').lower()}")
        if score < 0:
            suggestions.append("Avoid common/sequential patterns")

    # Entropy
    entropy = calculate_entropy(password)
    print(f"\n  Entropy Score: {entropy} bits")
    if entropy < 40:
        print("   ⚠  Low entropy — password is predictable")
        suggestions.append("Use a longer, more random password")
    elif entropy < 60:
        print("   ✔  Moderate entropy")
    else:
        print("   ✔  High entropy — hard to crack")

    # Final score
    label, emoji = get_strength_label(total_score)
    print(f"\n  TOTAL SCORE : {total_score}/10")
    print(f"  STRENGTH    : {emoji}  {label}")

    if suggestions:
        print("\n  SUGGESTIONS TO IMPROVE:")
        for i, s in enumerate(set(suggestions), 1):
            print(f"   {i}. {s}")

    print("="*55 + "\n")
    return label

def main():
    print("\n  ╔══════════════════════════════════════════╗")
    print("  ║      PASSWORD STRENGTH CHECKER           ║")
    print("  ║      by Kartik | Cybersecurity Tool      ║")
    print("  ╚══════════════════════════════════════════╝")

    while True:
        print("\n  Options:")
        print("   1. Check a password")
        print("   2. Exit")

        choice = input("\n  Enter choice (1/2): ").strip()

        if choice == "1":
            password = input("  Enter password to check: ")
            if not password:
                print("  ⚠  Please enter a password.")
                continue
            check_password(password)

        elif choice == "2":
            print("\n  Goodbye! Stay secure. 🔐\n")
            break
        else:
            print("  Invalid choice. Enter 1 or 2.")

if __name__ == "__main__":
    main()
