import cv2
import numpy as np
import matplotlib.pyplot as plt
img_noisy = cv2.imread('Median_filter\median_filter.png', 0)
m, n = img_noisy.shape
img_new = np.zeros([m, n])
for i in range(1, m-1):
    for j in range(1, n-1):
        temp = [img_noisy[i-1, j-1],
                img_noisy[i-1, j],
                img_noisy[i-1, j + 1],
                img_noisy[i, j-1],
                img_noisy[i, j],
                img_noisy[i, j + 1],
                img_noisy[i + 1, j-1],
                img_noisy[i + 1, j],
                img_noisy[i + 1, j + 1]]

        temp = sorted(temp)
        img_new[i, j] = temp[4]

img_new = img_new.astype(np.uint8)
cv2.imwrite('new_median_filtered.png', img_new)

plt.subplot(121), plt.imshow(img_noisy, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(img_new, cmap='gray'), plt.title('Median Filtered Image')
plt.show()
