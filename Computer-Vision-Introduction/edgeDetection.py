import cv2

# Load an image
path = r'TechBlogzz\Computer-Vision-Introduction\Assets\image.jpg'
image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)


# Perform Canny edge detection
edges = cv2.Canny(image, 100, 200)  # Adjust the thresholds as needed

# Display the original image and the detected edges
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
