
import cv2
import numpy as np
import sqlite3
import os

# Load mask
mask = cv2.imread("dataset/Y/1 (2).png")

if mask is None:
    print("Mask not found!")
    exit()

# Detect teal regions
lower = np.array([130, 130, 0])
upper = np.array([155, 155, 20])

room_mask = cv2.inRange(mask, lower, upper)

# Find connected regions
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
    room_mask, 8
)

# Create database folder
os.makedirs("database", exist_ok=True)

# Connect to SQLite
conn = sqlite3.connect("database/floorplan.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS rooms (
    room_id INTEGER PRIMARY KEY,
    plan_id TEXT,
    area INTEGER,
    x INTEGER,
    y INTEGER,
    width INTEGER,
    height INTEGER
)
""")

# Remove previous records
cursor.execute("DELETE FROM rooms WHERE plan_id = ?", ("Plan 1",))

room_id = 0

# Insert room information
for i in range(1, num_labels):

    area = int(stats[i, cv2.CC_STAT_AREA])

    if area > 5000:

        room_id += 1

        x = int(stats[i, cv2.CC_STAT_LEFT])
        y = int(stats[i, cv2.CC_STAT_TOP])
        w = int(stats[i, cv2.CC_STAT_WIDTH])
        h = int(stats[i, cv2.CC_STAT_HEIGHT])

        cursor.execute("""
        INSERT INTO rooms
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (room_id, "Plan 1", area, x, y, w, h))

conn.commit()

print("===== DATABASE RESULTS =====")

cursor.execute("SELECT * FROM rooms")

for row in cursor.fetchall():
    print(row)

print("\nTotal regions stored:", room_id)
print("Database created successfully!")

conn.close()
