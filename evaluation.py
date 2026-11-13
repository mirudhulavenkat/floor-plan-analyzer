
import sqlite3
import os
import csv

# Database connection
DB_PATH = "database/floorplan.db"

if not os.path.exists(DB_PATH):
    print("Database not found!")
    exit()

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# 20 evaluation questions
questions = [
    ("How many rooms are detected?", "count"),
    ("How many regions are there?", "count"),
    ("Count rooms", "count"),
    ("Count detected regions", "count"),

    ("Which is the largest room?", "largest"),
    ("Show the largest room", "largest"),
    ("Tell me the largest region", "largest"),
    ("What is the largest area?", "largest"),

    ("Which is the smallest room?", "smallest"),
    ("Show the smallest room", "smallest"),
    ("Tell me the smallest region", "smallest"),
    ("What is the smallest area?", "smallest"),

    ("What is the total area?", "total"),
    ("Calculate total area", "total"),
    ("Show total area", "total"),
    ("Give total area", "total"),

    ("Show all rooms", "all"),
    ("Show all regions", "all"),
    ("List all rooms", "all"),
    ("Display all detected regions", "all")
]

# Function to generate answers
def get_answer(question_type):

    if question_type == "count":
        cursor.execute("SELECT COUNT(*) FROM rooms")
        return cursor.fetchone()[0]

    elif question_type == "largest":
        cursor.execute("""
            SELECT room_id, area
            FROM rooms
            ORDER BY area DESC
            LIMIT 1
        """)
        return cursor.fetchone()

    elif question_type == "smallest":
        cursor.execute("""
            SELECT room_id, area
            FROM rooms
            ORDER BY area ASC
            LIMIT 1
        """)
        return cursor.fetchone()

    elif question_type == "total":
        cursor.execute("SELECT SUM(area) FROM rooms")
        return cursor.fetchone()[0]

    elif question_type == "all":
        cursor.execute("SELECT room_id, area FROM rooms")
        return cursor.fetchall()


# Expected results
expected = {
    "count": 12,
    "largest": (12, 218818),
    "smallest": (9, 10139),
    "total": 862306,
    "all": 12
}

# Run evaluation
results = []

print("\n===== 20 QUESTION EVALUATION =====\n")

passed = 0
failed = 0

for number, (question, question_type) in enumerate(questions, 1):

    actual = get_answer(question_type)

    if question_type == "all":
        actual_value = len(actual)
    else:
        actual_value = actual

    expected_value = expected[question_type]

    status = "PASS" if actual_value == expected_value else "FAIL"

    if status == "PASS":
        passed += 1
    else:
        failed += 1

    print(f"Question {number}: {question}")
    print("Expected:", expected_value)
    print("Actual:", actual_value)
    print("Status:", status)
    print("----------------------------")

    results.append([
        number,
        question,
        str(expected_value),
        str(actual_value),
        status
    ])

# Save evaluation report
os.makedirs("output", exist_ok=True)

with open("output/evaluation_results.csv",
          "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Question Number",
        "Question",
        "Expected Answer",
        "Actual Answer",
        "Status"
    ])

    writer.writerows(results)

# Final summary
print("\n===== EVALUATION SUMMARY =====")
print("Total Questions:", len(questions))
print("Passed:", passed)
print("Failed:", failed)

accuracy = (passed / len(questions)) * 100

print(f"Evaluation Accuracy: {accuracy:.2f}%")
print("\nReport saved in output/evaluation_results.csv")

conn.close()
