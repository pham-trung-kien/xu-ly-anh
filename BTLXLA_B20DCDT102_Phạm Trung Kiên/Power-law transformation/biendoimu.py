import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Power-law transformation\\bien_doi_mu.jpg')

plt.subplot(3, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

for i, gamma in enumerate([0.1, 0.5, 1.2, 2.2]):

    gamma_corrected = np.array(255*(img / 255) ** gamma, dtype='uint8')


    plt.subplot(3, 2, i + 2)
    plt.imshow(cv2.cvtColor(gamma_corrected, cv2.COLOR_BGR2RGB))
    plt.title(f'Gamma={gamma}')
    plt.axis('off')

plt.show()
