import cv2

# Load image
image = cv2.imread("image.jpg")

# Check if image loaded correctly
if image is None:
    print("Error: Image not found.")
    exit()

# Three predefined sizes
sizes = [
    (100, 100),
    (300, 300),
    (500, 500)
]

# Resize, display, and save images
for i, size in enumerate(sizes, start=1):
    resized = cv2.resize(image, size)

    cv2.imshow(f"Resized {i}", resized)

    filename = f"resized_{i}.jpg"
    cv2.imwrite(filename, resized)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()