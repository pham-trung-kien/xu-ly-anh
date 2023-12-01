import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('Logarit_transformation/logarit.png', cv2.IMREAD_GRAYSCALE)
c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(image + 1))

log_image = np.array(log_image, dtype=np.uint8)

plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(log_image, cmap='gray'), plt.title('Log Transformation')
plt.show()
