import numpy as np
import cv2
from scipy.signal import correlate2d, convolve2d

# Gunakan fungsi ini untuk mapping nilai pixel ke 0-255
def map_to_8bit(img_in):
    img_out = None
    img_out = ((img_in - img_in.min()) * 255/(img_in.max() - img_in.min())).astype(np.uint8)
    return img_out

def correlate(img_in, kernel):
    # Lengkapi fungsi berikut ini agar menghasilkan luaran berupa hasil correlation filter dengan parameter sebagai berikut
    # stride = 1
    # full padding
    # img_in : merupakan image input dalam bentuk BGR image
    # kernel : merupakan filter yang digunakan, ukuran dapat bervariasi (3x3, 5x5, 7x7, etc)
    # pada fungsi di bawah ini, lakukan konversi img_in dari BGR ke Grayscale terlebih dahulu, kemudian kalkulasi hasil correlation

    gray = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
    return correlate2d(gray.astype(np.int64), kernel, mode='full')

def convolve(img_in, kernel):
    # Lengkapi fungsi berikut ini agar menghasilkan luaran berupa hasil convolution dengan parameter sebagai berikut
    # stride = 1
    # same padding
    # kernel : merupakan filter yang digunakan, ukuran dapat bervariasi (3x3, 5x5, 7x7, etc)
    # pada fungsi di bawah ini, lakukan konversi img_in dari BGR ke Grayscale terlebih dahulu, kemudian kalkulasi hasil correlation

    gray = cv2.cvtColor(img_in, cv2.COLOR_BGR2GRAY)
    return convolve2d(gray.astype(np.int64), kernel, mode='same')

def main():
    image_path = "path/to/your/image.jpg"
    bgr_image = cv2.imread(image_path)

    # program untuk menguji coba correlation filter
    kernel_1 = np.array([[1, 0, -1],
                         [2, 0, -2],
                         [1, 0, -1]])
    coorelation_output = correlate(bgr_image, kernel_1)

    # program untuk menguji coba convolution filter, edge detection dengan sobel filter
    sobel_x = np.array([[1, 0, -1],
                        [2, 0, -2],
                        [1, 0, -1]])

    sobel_y = np.array([[1, 2, 1],
                        [0, 0, 0],
                        [-1, -2, -1]])
    
    output_x = convolve(bgr_image, sobel_x)
    output_y = convolve(bgr_image, sobel_y)
    sobel_output = np.sqrt(output_x**2 + output_y**2)

    cv2.imshow("Correlation Output", map_to_8bit(coorelation_output))
    cv2.imshow("Sobel X", map_to_8bit(output_x))
    cv2.imshow("Sobel Y", map_to_8bit(output_y))
    cv2.imshow("Sobel Output", map_to_8bit(sobel_output))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()