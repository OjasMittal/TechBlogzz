![MasterHead](https://www.sacmi.it/SacmiCorporate/media/Closures_Preforms_Containers/News_Images/2022/BANNER_NEWS_GULFCAN_2022.png)

# Introduction to Computer Vision

In today's tech-driven era, computers are doing something truly remarkable - they're learning to see and make sense of the visual world. Welcome to the intriguing domain of computer vision, where art meets science in a blend of artificial intelligence, image processing, and machine learning. In this exploration, we'll embark on a captivating journey through the world of computer vision. We'll uncover its historical roots, grasp the fundamental concepts, and appreciate its profound impact on our daily lives. Whether you're a curious beginner or a seasoned tech enthusiast, let's delve into the realm of pixels, algorithms, and machines that understand the visual universe.

##

## How it works?

- <h4>Gaining a Machine's Visual Perspective</h4>

  Imagine a computer looking at an image or a video. The first step is image acquisition, where the machine captures visual data through cameras or other sensors. These sensors transform light into digital information, creating a pixel-based representation of the scene.

- <h4>Preprocessing: Sharpening the Senses</h4>

  Next comes preprocessing, where the computer cleans and enhances the data. It might adjust brightness and contrast, correct colors, or remove noise to improve the quality of the visual input. This step is akin to getting the "glasses" just right for the computer's eyes.

- <h4> Feature Extraction: What's Worth Noticing </h4>

  Now, the computer identifies patterns and features within the visual data. It locates edges, identifies objects, and understands shapes, textures, and colors. This is where the magic happens as the machine starts to comprehend the contents of the image.

- <h4>Recognition and Interpretation: Making Sense of It All</h4>

  Once the machine has identified these features, it moves on to recognition and interpretation. It matches what it "sees" with patterns it has learned from extensive training. This could be recognizing a face, a handwritten letter, or a specific object.

- <h4>Decision-Making: Taking Action</h4>

  Finally, based on its interpretation, the computer makes decisions or takes actions. This can range from simple tasks like sorting images to complex processes such as autonomous navigation in self-driving cars.

---

## Real World Applications

1. Autonomous Vehicles
2. Healthcare and Medical Imaging
3. Facial Recognition and Security
4. Augmented Reality (AR)
5. Object Detection in Retail
6. Agriculture and Precision Farming
7. Industrial Automation and Robotics
8. Sports and Entertainment
9. Environmental Monitoring
10. Accessibility and Assistive Technologies

---

## [Various Image Processing Techniques](./Various-Image-Processing-Techniques.md)

Click to learn about the different kinds of techniques for processing images.

---

## Demos

For all the demos we will be using Python and the library [opencv-python](https://pypi.org/project/opencv-python/).
[OpenCV](https://opencv.org) or Open Source Computer Vision Library, is an open-source computer vision and machine learning software library. It's designed to provide a comprehensive set of tools and functions for various computer vision tasks, including image and video processing, object detection, face recognition, image stitching, and more. OpenCV is written in C++ and has bindings for various programming languages, including Python.

1. To check whether python is installed `python --version`

2. To install opencv `pip install opencv-python`

---

<h4>1. Edge Detection using Canny</h3>

```py
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
```

#### Output

<div style="text-align:center;">
<img src = "https://i.imgur.com/ms3bSS8.png" alt = "Canny Edge Detection">
</div>

---

<h4>2. Gaussian Blur </h4>

```py
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
```

#### Output

<div style="text-align:center;">
<img src="https://i.imgur.com/onxVBh1.png" alt="Gaussian Blur">
</div>

---

#### 3. [MediaPipe](https://developers.google.com/mediapipe)

MediaPipe is an open-source framework developed by Google that empowers developers to build applications with real-time perception capabilities. It offers a wide range of pre-built machine learning models and tools for various computer vision tasks, including object detection, hand tracking, face detection, and pose estimation. MediaPipe simplifies complex computer vision tasks, making it accessible to developers for applications in fields like augmented reality, virtual reality, gesture recognition, and more. With its versatility and ease of integration, MediaPipe is a valuable resource for creating interactive and immersive experiences in diverse domains.

Refer [MediaPipe Solutions](https://developers.google.com/mediapipe/solutions/guide) to see the entire list of solutions it offers.

#### Recommended MediaPipe Demos

1. [Object Detection Model](https://developers.google.com/mediapipe/solutions/vision/object_detector)
2. [Face Detection](https://developers.google.com/mediapipe/solutions/vision/face_detector)
3. [Gesture Recognition](https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer)

The reason i decided to provide google console tutorials rather than the actual code is because the installation procedure of [mediapipe framework for windows](https://developers.google.com/mediapipe/framework/getting_started/install#installing_on_windows) is complicated and is still experimental. However if you want to try this in your local windows machine, either follow the installation guide or install a version of python 3.8.10 or earlier. (MediaPipe was a library before it became a framework)

    pip install mediapipe

## Conclusion

In conclusion, computer vision is a captivating field that bridges the realms of science and art, where machines learn to perceive and understand the visual world. This extraordinary journey takes us through a landscape of pixels, algorithms, and machine learning, enabling computers to interpret images, identify objects, and make sense of their surroundings. With applications ranging from autonomous vehicles and healthcare to augmented reality and security, computer vision's impact on our daily lives is profound and ever-expanding. As we continue to explore this dynamic domain, we uncover its inner workings, real-world applications, and the ongoing innovations that are reshaping the way we interact with technology

<div style="text-align: right;">
<a href =https://github.com/parzi-val>KR Bala</a>
</div>
