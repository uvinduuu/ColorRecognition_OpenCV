# Color Recognition and Picker using OpenCV

This project demonstrates a simple color recognition program that captures frames from a webcam and determines the color of the center pixel. Additionally, it includes a color picker interface using trackbars to adjust HSV values and visualize the corresponding BGR color.

## Features

1. **Webcam Color Recognition:**
   - Captures frames from a webcam.
   - Converts the BGR image to HSV.
   - Identifies the color of the center pixel based on its hue value.
   - Displays the detected color name on the video frame.

2. **Color Picker:**
   - Provides a GUI with trackbars to adjust HSV values.
   - Displays the corresponding BGR color based on the selected HSV values.

## Understanding HSV and RGB

### RGB (Red, Green, Blue)
- A color model in which colors are described in terms of the combination of Red, Green, and Blue light.
- Commonly used in digital displays and image editing.

### HSV (Hue, Saturation, Value)
- A color model that describes colors in terms of Hue (color type), Saturation (color intensity), and Value (brightness).
- More closely aligns with how humans perceive and interpret colors.
- Useful for tasks like color detection and filtering.

## Installation

1. Ensure you have Python installed on your system.
2. Install the required libraries using pip:
    ```sh
    pip install opencv-python numpy
    ```

## Usage

### Webcam Color Recognition

1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/uvinduuu/ColorRecognition_OpenCV.git
    ```
2. Navigate to the project directory:
    ```sh
    cd ColorRecognition_OpenCV
    ```
3. Run the `ColorRecognition.py` script:
    ```sh
    python ColorRecognition.py
    ```
4. The script will open a window displaying the video feed from your webcam. The color of the center pixel will be detected and displayed on the frame.

### Color Picker

1. Run the `hsv_color_picker.py` script:
    ```sh
    python hsv_color_picker.py
    ```
2. A window with trackbars for Hue, Saturation, and Value will appear. Adjust the trackbars to see the corresponding BGR color displayed.

---

## Contact

For any clarifications or Inquiries please feel free to [Contact Me](mailto:uvindukodikara@gmail.com)
