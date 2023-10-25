import cv2

# Load an image
path = r'TechBlogzz\Computer-Vision-Introduction\Assets\image.jpg'
image = cv2.imread(path)

# Define the kernel size for Gaussian blur (adjust this as needed)
kernel_size = (7, 7)

# Apply Gaussian blur to the image
blurred_image = cv2.GaussianBlur(image, kernel_size, 0)

# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

