# 🔐 Password Strength Checker

A command-line cybersecurity tool that analyzes password strength using multiple security criteria including entropy calculation, pattern detection, and common password checks.

## 🛡️ Features

- ✅ Checks password length, uppercase, lowercase, digits, special characters
- ✅ Detects common/weak passwords (password, 123456, admin, etc.)
- ✅ Detects repeated and sequential character patterns
- ✅ Calculates entropy (randomness score in bits)
- ✅ Gives an overall strength rating: Very Weak → Very Strong
- ✅ Provides actionable suggestions to improve your password

## 📸 Example Output

```
=======================================================
         PASSWORD STRENGTH CHECKER
=======================================================
  Password: ************  (length: 12)
-------------------------------------------------------

  ANALYSIS:
   ✔  Good length (12-15 chars)
   ✔  Has uppercase letters
   ✔  Has lowercase letters
   ✔  Has 2 digits (great)
   ✔  Has 2 special characters (great)
   ✔  No common patterns detected

  Entropy Score: 71.45 bits
   ✔  High entropy — hard to crack

  TOTAL SCORE : 9/10
  STRENGTH    : ✅  VERY STRONG
=======================================================
```

## 🚀 How to Run

**Requirements:** Python 3.x (no extra libraries needed)

```bash
# Clone the repo
git clone https://github.com/yourusername/password-strength-checker.git
cd password-strength-checker

# Run the tool
python password_checker.py
```

## 📊 Scoring Criteria

| Check | Max Score |
|---|---|
| Password Length | 3 |
| Uppercase Letters | 1 |
| Lowercase Letters | 1 |
| Digits | 2 |
| Special Characters | 2 |
| Pattern Penalty | -2 |

## 🔑 What Makes a Strong Password?

- At least **12+ characters**
- Mix of **uppercase and lowercase**
- At least **2 digits**
- At least **2 special characters** (!@#$%^&*)
- **No sequential patterns** (123, abc)
- **Not a common password**

## 🧰 Tech Stack

- **Language:** Python 3
- **Libraries:** `re`, `math`, `string` (all built-in — no installs needed)

## 👤 Author

**Kartik** — QA Analyst | Cybersecurity Enthusiast  
📧 palkartik2005@gmail.com

## 📄 License

MIT License — free to use and modify.
