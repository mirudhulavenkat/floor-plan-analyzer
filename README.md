Floor Plan Analyzer
Floor Plan Analysis and Automated Room Detection System

1. Project Overview

Floor Plan Analyzer is an image-processing-based application designed to analyze architectural floor plans and automatically identify room regions.

The system uses computer vision techniques to process floor plan images, extract room regions, calculate their areas, and store the detected information in an SQLite database.

An interactive web interface built using Streamlit allows users to visualize floor plan images, explore detected rooms, view room statistics, and ask questions about the analyzed floor plan.

2. Objectives

Automate room detection from floor plan images.
Analyze segmentation masks using image processing techniques.
Identify connected room regions.
Calculate the area and position of detected regions.
Store room information in an SQLite database.
Provide an interactive interface for floor plan analysis.
Enable users to ask questions about detected rooms.

3. Features

3.1 Dataset Inspection

Loads original floor plan images and corresponding segmentation masks.
Displays image dimensions and dataset information.
Checks the availability of input images.
3.2 Mask Analysis

Analyzes segmentation masks using OpenCV.
Identifies dominant colours in the masks.
Generates mask previews for visualization.
3.3 Room Detection and Extraction

Identifies room regions based on colour segmentation.
Uses connected component analysis to identify separate regions.
Filters small regions based on area.
Calculates room area, coordinates, width, and height.
Generates visualizations with detected room boundaries.
3.4 Database Management

Uses SQLite to store extracted room information.
Stores room IDs, areas, positions, widths, and heights.
Retrieves room information for analysis and visualization.
3.5 Interactive Web Interface

Developed using Streamlit.
Displays original floor plans and segmentation masks.
Shows detected room regions and overlays.
Displays room statistics and information.
Provides an interactive question-answering section.
3.6 Question Answering System

Allows users to ask questions about the analyzed floor plan.

Supports questions about:

Room counts.
Largest room.
Smallest room.
Total detected area.
All detected regions.
The question-answering system retrieves information using SQLite database queries.

4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenCV | Image processing and room detection |
| NumPy | Numerical operations and array processing |
| SQLite | Database management |
| Streamlit | Interactive web interface |
| Pandas | Tabular data presentation |

5. Project Folder Structure

## Project Structure

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
6. Installation and Setup

Step 1: Clone the Repository

bash
git clone YOUR_GITHUB_REPOSITORY_URL

Step 2: Navigate to the Project Folder

bash
cd floor-plan

Step 3: Install Required Libraries

bash
pip3 install opencv-python numpy streamlit pandas
7. How to Run the Project

Execute the following scripts in the appropriate order.

Step 1: Check the Dataset

bash
python3 check_dataset.py

Step 2: Analyze the Segmentation Mask

bash
python3 mask_analysis.py

Step 3: Generate Mask Preview

bash
python3 view_mask.py

Step 4: Extract Room Regions

bash
python3 room_extraction.py

Step 5: Create the Database

bash
python3 database.py

Step 6: Run the Question Answering System (Optional)

bash
python3 qa.py

Step 7: Launch the Web Application
bash
python3 -m streamlit run app.py

The application will open in your browser.

8. Question Answering Capabilities

The system supports questions such as:

How many rooms are detected?
How many regions are there?
Count detected rooms.
Which is the largest room?
Show the largest room.
Which is the smallest room?
Show the smallest room.
What is the largest area?
What is the total area?
Calculate total area.
Show all rooms.
List all detected regions.
The question-answering system retrieves information from the SQLite database.

9. Design Choices

The project follows a modular image-processing pipeline.

Colour Segmentation: OpenCV identifies room regions using colours in segmentation masks.
Connected Component Analysis: Identifies separate connected regions and calculates their bounding boxes and areas.
Area Filtering: Removes small regions to reduce noise and unwanted detections.
SQLite Database: Stores extracted room information and enables efficient data retrieval.
Streamlit Interface: Provides an interactive way to visualize floor plans and explore room statistics.
Database-Based Question Answering: Uses SQL queries to provide answers based on actual extracted room information rather than generating unsupported results.
These choices keep the application lightweight, explainable, and easy to maintain.

10. Limitations

Segmentation Dependency: The current implementation requires corresponding segmentation masks and cannot independently analyze every raw floor plan image.
Detection Accuracy: Incorrect mask colours, noise, or connected regions can affect room detection.
Area Threshold: Small legitimate rooms may be removed if they fall below the selected minimum area.
Pixel-Based Measurement: Room areas are calculated in pixels and cannot directly represent real-world square metres without scale calibration.
Question Answering: The system supports predefined types of questions rather than unrestricted natural-language understanding.
Dataset Dependency: The processing pipeline currently follows a specific dataset folder structure.

11. Future Improvements – What I Would Do Next

Direct Room Detection: Implement a computer vision or deep learning model to identify rooms directly from raw floor plan images without depending on existing segmentation masks.
Improved Accuracy: Introduce morphological image-processing techniques to reduce noise and improve room boundary detection.
Real-World Area Calculation: Add scale calibration to calculate approximate room areas in square metres or square feet.
Room Connectivity: Build a graph-based model using rooms as nodes and doors as connections to support navigation.
Advanced Question Answering: Support more flexible natural-language questions while keeping answers grounded in database information.
Multiple Floor Plans: Extend the database to store and analyze multiple floor plans independently.
Better Visualization: Add interactive room selection, highlighting, charts, and downloadable analysis reports.
My next major improvement would be to enable direct room detection from raw architectural floor plan images while retaining the existing SQLite database and Streamlit interface.

12. Conclusion

Floor Plan Analyzer demonstrates how computer vision, image processing, and database technologies can be combined to analyze architectural floor plans.

By using OpenCV-based colour segmentation and connected component analysis, the system identifies room regions, calculates their pixel-based areas and dimensions, and stores the extracted information in an SQLite database.

The Streamlit interface provides an interactive platform to visualize floor plans, explore detected regions, view room statistics, and retrieve information through database-driven question answering.

Although the current implementation depends on segmentation masks, it establishes a foundation for further development of intelligent architectural floor plan analysis systems.

Future improvements will focus on direct room detection,
