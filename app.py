
import streamlit as st
import sqlite3
import os
import pandas as pd

from qa import answer_question


# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="Floor Plan Analyzer",
    page_icon="🏠",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title("🏠 Floor Plan Analyzer")

st.write(
    "Floor Plan Analysis and Room Detection System"
)

st.divider()


# ==========================================
# DATABASE CONNECTION
# ==========================================

db_path = "database/floorplan.db"

if not os.path.exists(db_path):
    st.error("Database not found. Run database.py first.")
    st.stop()

conn = sqlite3.connect(db_path)
cursor = conn.cursor()


# ==========================================
# ANALYSIS SUMMARY
# ==========================================

cursor.execute("SELECT COUNT(*) FROM rooms")
room_count = cursor.fetchone()[0]

cursor.execute("SELECT SUM(area) FROM rooms")
total_area = cursor.fetchone()[0] or 0

cursor.execute("""
    SELECT room_id, area
    FROM rooms
    ORDER BY area DESC
    LIMIT 1
""")

largest = cursor.fetchone()

st.header("Analysis Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Detected Regions",
    room_count
)

col2.metric(
    "Total Area",
    f"{total_area:,} pixels"
)

col3.metric(
    "Largest Region",
    f"Room {largest[0]}" if largest else "N/A"
)

st.divider()


# ==========================================
# FLOOR PLAN IMAGES
# ==========================================

st.header("Floor Plan Images")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Original Floor Plan")

    image_path = "dataset/X/1.png"

    if os.path.exists(image_path):
        st.image(
            image_path,
            use_container_width=True
        )
    else:
        st.warning("Original image not found.")


with col2:

    st.subheader("Segmentation Mask")

    mask_path = "dataset/Y/1 (2).png"

    if os.path.exists(mask_path):
        st.image(
            mask_path,
            use_container_width=True
        )
    else:
        st.warning("Segmentation mask not found.")


# ==========================================
# ROOM DETECTION
# ==========================================

st.header("Room Detection")

candidate_path = "output/room_candidates.png"

if os.path.exists(candidate_path):

    st.image(
        candidate_path,
        caption="Detected candidate room regions",
        use_container_width=True
    )

else:
    st.warning("Room detection image not found.")


st.divider()


# ==========================================
# FLOOR PLAN OVERLAYS
# ==========================================

st.header("Floor Plan Overlays")

cols = st.columns(3)

for i in range(1, 4):

    with cols[i - 1]:

        st.subheader(f"Overlay {i}")

        path = f"output/overlay_{i}.png"

        if os.path.exists(path):

            st.image(
                path,
                use_container_width=True
            )

        else:
            st.warning(f"Overlay {i} not found.")


st.divider()


# ==========================================
# ROOM INFORMATION TABLE
# ==========================================

st.header("Room Information")

cursor.execute("""
    SELECT room_id, area, x, y, width, height
    FROM rooms
    ORDER BY room_id
""")

data = cursor.fetchall()

df = pd.DataFrame(
    data,
    columns=[
        "Room ID",
        "Area (pixels)",
        "X Position",
        "Y Position",
        "Width",
        "Height"
    ]
)

st.dataframe(
    df,
    hide_index=True,
    use_container_width=True
)


st.divider()


# ==========================================
# QUESTION ANSWERING SYSTEM
# ==========================================

st.header("Ask Questions About Your Floor Plan")

st.write(
    "Ask questions about detected rooms, "
    "largest room, smallest room and total area."
)

question = st.text_input(
    "Enter your question",
    placeholder="Which is the largest room?"
)

if st.button("Get Answer"):

    if question.strip():

        answer = answer_question(question)

        st.success(answer)

    else:

        st.warning("Please enter a question.")


# ==========================================
# CLOSE DATABASE
# ==========================================

conn.close()


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Floor Plan Analyzer | Python | OpenCV | "
    "SQLite | Streamlit"
)
