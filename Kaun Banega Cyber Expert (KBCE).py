# 🛡️ Kaun Banega Cyber Expert - Python Quiz Game
# CBSE Class 12 (2025–26) Compliant Project

# --- Welcome Message ---
print("\U0001F6E1\ufe0f Welcome to 'Kaun Banega Cyber Expert' \U0001F6E1\ufe0f")
print("Answer each question by typing A, B, C or D.")
print("Correct Answer: +10 points | Wrong Answer: -5 points")
print("\nLet's begin the quiz! Good luck!\n")

# --- Question Bank (List of Dictionaries) ---
questions = [
    {"question": "What does 'HTTPS' stand for?", "options": ["A. HyperText Transfer Protocol Secure", "B. High Transfer Protocol Secure", "C. HyperTerminal Transfer Secure", "D. HighText Protocol Secure"], "answer": "A"},
    {"question": "Which language is used to write the Python interpreter?", "options": ["A. C", "B. Java", "C. Python", "D. C++"], "answer": "A"},
    {"question": "What is the purpose of a firewall in cybersecurity?", "options": ["A. To block unauthorized access", "B. To speed up internet connection", "C. To store passwords securely", "D. To encrypt data"], "answer": "A"},
    {"question": "Which of these is a strong password?", "options": ["A. password123", "B. 123456", "C. P@ssw0rd!", "D. admin"], "answer": "C"},
    {"question": "What does an 'if' statement do in Python?", "options": ["A. Loops through code", "B. Defines a function", "C. Checks a condition", "D. Imports a module"], "answer": "C"},
    {"question": "What is the output of print(2 + 3 * 4)?", "options": ["A. 20", "B. 14", "C. 24", "D. 10"], "answer": "B"},
    {"question": "Which Python data structure is ordered and mutable?", "options": ["A. Tuple", "B. List", "C. Set", "D. Dictionary"], "answer": "B"},
    {"question": "What is phishing?", "options": ["A. A type of malware", "B. Stealing info by pretending to be trustworthy", "C. Encrypting data", "D. A firewall technique"], "answer": "B"},
    {"question": "Which of these is not a programming language?", "options": ["A. Python", "B. Java", "C. HTML", "D. C++"], "answer": "C"},
    {"question": "What does 'else' do in Python?", "options": ["A. Defines a function", "B. Executes if 'if' is false", "C. Loops through code", "D. Imports a module"], "answer": "B"},
    {"question": "What is the output of print('Hello' + 'World')?", "options": ["A. Hello World", "B. HelloWorld", "C. Hello+World", "D. Error"], "answer": "B"},
    {"question": "Which Python data type is mutable?", "options": ["A. String", "B. Tuple", "C. List", "D. Integer"], "answer": "C"},
    {"question": "What is a Trojan in cybersecurity?", "options": ["A. A secure protocol", "B. Malicious software disguised as legitimate", "C. A type of encryption", "D. A network tool"], "answer": "B"},
    {"question": "Which loop repeats a fixed number of times?", "options": ["A. while", "B. for", "C. if", "D. else"], "answer": "B"},
    {"question": "What does VPN stand for?", "options": ["A. Virtual Private Network", "B. Very Public Network", "C. Virtual Public Node", "D. Verified Private Node"], "answer": "A"},
    {"question": "What is the purpose of a variable in Python?", "options": ["A. To store data", "B. To print output", "C. To loop code", "D. To define functions"], "answer": "A"},
    {"question": "Which is a common cyber attack?", "options": ["A. SQL Injection", "B. Faster Internet", "C. Data Sorting", "D. File Compression"], "answer": "A"},
    {"question": "What is the output of len('Python')?", "options": ["A. 5", "B. 6", "C. 7", "D. 8"], "answer": "B"},
    {"question": "Which key in a dictionary is unique?", "options": ["A. Value", "B. Key", "C. Index", "D. Element"], "answer": "B"},
    {"question": "What does a hacker exploit?", "options": ["A. System vulnerabilities", "B. Fast networks", "C. Secure passwords", "D. Encrypted files"], "answer": "A"}
]

# --- Initialize Score and Counters ---
score = 0
correct_count = 0
incorrect_count = 0

# --- Question Loop ---
for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer: ").strip().upper()

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 10
        correct_count += 1
    else:
        print("❌ Incorrect!")
        score -= 5
        incorrect_count += 1
    print("Current Score:", score)

# --- Final Summary ---
print("\n🎉 Quiz Over! Your Final Score is:", score)
print(f"Correct Answers: {correct_count}")
print(f"Incorrect Answers: {incorrect_count}")

# --- Level-Based Feedback ---
if score == 200:
    print("🌟 Perfect score! You're a true Cyber Expert!")
elif score >= 150:
    print("🏆 Congratulations! You've reached the Expert level!")
elif score >= 100:
    print("🎯 Well done! You've reached the Intermediate level.")
else:
    print("👍 Keep practicing! You're at the Beginner level.")

# --- Motivational Message ---
if score >= 150:
    print("Excellent job! You have a strong grasp of cybersecurity and computer science.")
elif score >= 100:
    print("Good work! You have a solid understanding of the basics.")
else:
    print("Keep learning and try again to improve your score!")
