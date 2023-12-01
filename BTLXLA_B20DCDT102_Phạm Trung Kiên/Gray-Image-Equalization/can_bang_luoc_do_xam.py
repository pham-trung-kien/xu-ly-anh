
import matplotlib.pyplot as plt
from PIL import Image


def transform(img):
    width, height = img.size
    
    tan_xuat= {}

    for y in range(height):
        for x in range(width):
            do_xam = img.getpixel((x, y))
            if do_xam in tan_xuat:
                tan_xuat[do_xam] += 1
            else:
                tan_xuat[do_xam] = 1
    key_sorted=sorted(tan_xuat.keys())
    bien_doi = 0
    for key in key_sorted:
        bien_doi += 255*(tan_xuat[key]/(width*height))
        tan_xuat[key]=round(bien_doi)
        
    for y in range(height):
        for x in range(width):
            pixel_value = img.getpixel((x, y))
            
            img.putpixel((x, y), tan_xuat[pixel_value])

    return img

def plot(image_path):
    # Đọc hình ảnh
    img = Image.open(image_path)
    img = img.convert('L')

    # Hiển thị hình ảnh ban đầu
    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(img,cmap='gray')
    plt.axis('off')
    img = transform(img)

    plt.subplot(1, 2, 2)
    plt.title('Tranformed Image')
    plt.imshow(img,cmap='gray')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

plot("Gray-Image-Equalization\image.png")