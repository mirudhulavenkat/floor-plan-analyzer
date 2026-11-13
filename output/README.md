# Floor Plan Analyzer
### Floor Plan Analysis and Automated Room Detection System

## 1. Project Overview

Floor Plan Analyzer is an image-processing-based application designed to analyze architectural floor plans and automatically identify room regions.

The system uses computer vision techniques to process floor plan images, extract room regions, calculate their areas, and store the detected information in an SQLite database.

An interactive web interface built using Streamlit allows users to visualize floor plan images, explore detected rooms, view room statistics, and ask questions about the analyzed floor plan.

## 2. Objectives

- Automate room detection from floor plan images.
- Analyze segmentation masks using image processing techniques.
- Identify connected room regions.
- Calculate the area and position of detected regions.
- Store room information in an SQLite database.
- Provide an interactive interface for floor plan analysis.
- Enable users to ask questions about detected rooms.

## 3. Features

### 3.1 Dataset Inspection
- Loads original floor plan images and corresponding segmentation masks.
- Displays image dimensions and dataset information.
- Checks the availability of input images.

### 3.2 Mask Analysis
- Analyzes segmentation masks using OpenCV.
- Identifies dominant colours in the masks.
- Generates mask previews for visualization.

### 3.3 Room Detection and Extraction
- Identifies room regions based on colour segmentation.
- Uses connected component analysis to identify separate regions.
- Filters small regions based on area.
- Calculates room area, coordinates, width, and height.
- Generates visualizations with detected room boundaries.

### 3.4 Database Management
- Uses SQLite to store extracted room information.
- Stores room IDs, areas, positions, widths, and heights.
- Retrieves room information for analysis and visualization.

### 3.5 Interactive Web Interface
- Developed using Streamlit.
- Displays original floor plans and segmentation masks.
- Shows detected room regions and overlays.
- Displays room statistics and information.
- Provides an interactive question-answering section.

### 3.6 Question Answering System
- Allows users to ask questions about the analyzed floor plan.
- Retrieves answers using SQLite database queries.
- Supports questions about room counts, largest room, smallest room, total area, and all detected regions.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenCV | Image processing and room detection |
| NumPy | Numerical operations and array processing |
| SQLite | Database management |
| Streamlit | Interactive web interface |
| Pandas | Tabular data presentation |

## 5. Project Folder Structure

```text
FLOOR-PLAN/
│
├── dataset/
│   ├── X/
│   │   └── Original floor plan images
│   │
│   └── Y/
│       └── Segmentation masks
│
├── database/
│   └── floorplan.db
│
├── output/
│   ├── mask_preview.png
│   ├── room_candidates.png
│   ├── room_mask.png
│   ├── overlay_1.png
│   ├── overlay_2.png
│   ├── overlay_3.png
│   └── evaluation_results.csv
│
├── check_dataset.py
├── mask_analysis.py
├── view_mask.py
├── room_extraction.py
├── database.py
├── qa.py
├── app.py
└── README.md
```

## 6. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd floor-plan
```

### Step 3: Install Required Libraries

```bash
pip3 install opencv-python numpy streamlit pandas
```

## 7. How to Run the Project

Execute the following scripts in the appropriate order.

**Step 1: Check the Dataset**

```bash
python3 check_dataset.py
```

**Step 2: Analyze the Segmentation Mask**

```bash
python3 mask_analysis.py
```

**Step 3: Generate Mask Preview**

```bash
python3 view_mask.py
```

**Step 4: Extract Room Regions**

```bash
python3 room_extraction.py
```

**Step 5: Create the Database**

```bash
python3 database.py
```

**Step 6: Run the Question Answering System (Optional)**

```bash
python3 qa.py
```

**Step 7: Launch the Web Application**

```bash
python3 -m streamlit run app.py
```

The application will open in your browser.

## 8. Question Answering Capabilities

The system supports questions such as:

1. How many rooms are detected?
2. How many regions are there?
3. Count detected rooms.
4. Which is the largest room?
5. Show the largest room.
6. Which is the smallest room?
7. Show the smallest room.
8. What is the largest area?
9. What is the total area?
10. Calculate total area.
11. Show all rooms.
12. List all detected regions.

The question-answering system retrieves information from the SQLite database.


## 9. Sample Results

The current dataset produced the following results:

| Metric | Result |
|---|---:|
| Detected Regions | 12 |
| Total Detected Area | 862,306 pixels |
| Largest Region | Room 12 |
| Largest Area | 218,818 pixels |
| Smallest Region | Room 9 |
| Smallest Area | 10,139 pixels |


## 10. Conclusion

Floor Plan Analyzer demonstrates the application of computer vision and image processing techniques in architectural floor plan analysis.

By combining OpenCV-based room extraction, SQLite database management, and a Streamlit-based interactive interface, the system provides a way to analyze floor plans, retrieve room information, and visualize detected regions.

The project establishes a foundation for further development of intelligent architectural floor plan analysis systems.

