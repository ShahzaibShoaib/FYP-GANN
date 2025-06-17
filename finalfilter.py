import cv2
import numpy as np
import argparse
import os

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Apply sharpening and blur reduction to a video.')
parser.add_argument('input_video', help='Path to the input video file.')
parser.add_argument('output_video', help='Path to save the enhanced video.')
parser.add_argument('--sharpening', type=int, default=50, help='Sharpening intensity (0-100).')
parser.add_argument('--noise_reduction', type=str, default='low', choices=['low', 'medium', 'high'])
args = parser.parse_args()

# Load the video
if not os.path.exists(args.input_video):
    raise FileNotFoundError(f"Input video not found: {args.input_video}")

cap = cv2.VideoCapture(args.input_video)

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(args.output_video, fourcc, fps, (width, height))

# Convert sharpening intensity (0-100) to kernel strength
strength = args.sharpening / 50.0  # maps 50 to 1.0, 100 to 2.0
sharpen_kernel = np.array([
    [0, -strength, 0],
    [-strength, 1 + 4 * strength, -strength],
    [0, -strength, 0]
])

# Noise reduction mapping
noise_levels = {
    'low': 5,
    'medium': 10,
    'high': 20
}
noise_var = noise_levels.get(args.noise_reduction, 5)

def wiener_filter(img, kernel_size=5, noise_var=noise_var):
    kernel = np.ones((kernel_size, kernel_size)) / (kernel_size ** 2)
    img_blur = cv2.filter2D(img, -1, kernel)
    noise = noise_var * np.random.randn(*img.shape).astype(np.float32)
    return np.clip(img - img_blur + noise, 0, 255).astype(np.uint8)

# Process video frame-by-frame
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale for contrast enhancement
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)
    frame_enhanced = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)

    # Apply sharpening
    sharpened = cv2.filter2D(frame_enhanced, -1, sharpen_kernel)

    # Apply noise reduction
    deblurred = wiener_filter(sharpened)

    # Write to output
    out.write(deblurred)

cap.release()
out.release()
print("Video enhancement complete. Saved as:", args.output_video)