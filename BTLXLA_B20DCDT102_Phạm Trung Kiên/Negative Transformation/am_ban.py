import cv2
import matplotlib.pyplot as plt

# Read an image
img_bgr = cv2.imread('am_ban.jpg', 1)


plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

img_negative = 255 - img_bgr
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(img_negative, cv2.COLOR_BGR2RGB))
plt.title('Negative Transformed Image')
plt.axis('off')

plt.tight_layout()
plt.show()
