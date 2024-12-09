# Finger Mouse Control and Click

This project implements a hand tracking system using OpenCV, MediaPipe, and PyAutoGUI. The system allows users to control the mouse pointer with their index finger and perform click actions by bringing the thumb and index finger tips together.

---

## Features

1. **Mouse Control with Index Finger**: Move the mouse pointer based on the position of your index finger.
2. **Click Action**: Perform a mouse click by touching the thumb and index finger tips together.

---

## Technologies Used

- **Python**: Programming language used for the implementation.
- **OpenCV**: For capturing video and processing frames.
- **MediaPipe**: For hand landmark detection and tracking.
- **PyAutoGUI**: For controlling the mouse pointer and simulating mouse clicks.

---

## Setup Instructions

### Prerequisites

1. **Python 3.7 or above**
   Ensure you have a compatible Python version installed.

2. **Required Libraries**
   Install the necessary Python libraries using pip:
   ```bash
   pip install opencv-python mediapipe pyautogui
   ```

---

## How to Run

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the Python script:
   ```bash
   python main.py
   ```

3. Allow camera access when prompted.

4. Use the following gestures:
   - **Move the mouse**: Use your index finger to control the cursor on the screen.
   - **Perform a click**: Bring the thumb and index finger tips together.

---

## How It Works

1. **Hand Detection**:
   - MediaPipe is used to detect hand landmarks in the video feed.
   - The system identifies the positions of the index finger and thumb tips.

2. **Mouse Control**:
   - The position of the index finger tip is mapped to the screen coordinates to move the mouse cursor.

3. **Click Detection**:
   - When the distance between the thumb and index finger tips falls below a certain threshold, PyAutoGUI simulates a mouse click at the cursor's location.

---

## Troubleshooting

- **Low FPS**: Reduce the video resolution or use a more optimized setup for real-time performance.
- **No Hand Detected**: Ensure your hand is within the camera frame and in clear lighting.
- **Incorrect Clicks**: Adjust the distance threshold in the script for detecting clicks.

---

## Acknowledgments

- **[MediaPipe](https://mediapipe.dev/)** for hand landmark detection.
- **[PyAutoGUI](https://pyautogui.readthedocs.io/)** for mouse control.

---

## Author

- Nakka Kiran Siva Koushik

