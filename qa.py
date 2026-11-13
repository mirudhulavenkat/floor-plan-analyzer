
import sqlite3
import os

DB_PATH = "database/floorplan.db"


def answer_question(question):

    if not os.path.exists(DB_PATH):
        return "Database not found. Please run database.py first."

    if not question.strip():
        return "Please enter a question."

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    q = question.lower().strip()

    try:

        # 1. Largest room
        if "largest" in q or "biggest" in q:
            cursor.execute("""
                SELECT room_id, area
                FROM rooms
                ORDER BY area DESC
                LIMIT 1
            """)

            result = cursor.fetchone()

            return (
                f"Largest room: Room {result[0]}\n"
                f"Area: {result[1]:,} pixels"
            )

        # 2. Smallest room
        elif "smallest" in q:
            cursor.execute("""
                SELECT room_id, area
                FROM rooms
                ORDER BY area ASC
                LIMIT 1
            """)

            result = cursor.fetchone()

            return (
                f"Smallest room: Room {result[0]}\n"
                f"Area: {result[1]:,} pixels"
            )

        # 3. Total area
        elif "area" in q and any(
            word in q for word in ["total", "calculate", "give"]
        ):
            cursor.execute("SELECT SUM(area) FROM rooms")
            result = cursor.fetchone()[0] or 0

            return f"Total detected area: {result:,} pixels"

        # 4. Show all rooms
        elif any(word in q for word in ["show", "all", "list", "display"]):
            cursor.execute("""
                SELECT room_id, area
                FROM rooms
                ORDER BY room_id
            """)

            results = cursor.fetchall()

            answer = "===== ALL DETECTED ROOMS =====\n\n"

            for room in results:
                answer += (
                    f"Room {room[0]} | "
                    f"Area: {room[1]:,} pixels\n"
                )

            return answer

        # 5. Count rooms
        elif any(word in q for word in ["how many", "count"]):
            cursor.execute("SELECT COUNT(*) FROM rooms")
            result = cursor.fetchone()[0]

            return f"Total detected regions: {result}"

        else:
            return "Sorry, I cannot answer that question."

    finally:
        conn.close()
