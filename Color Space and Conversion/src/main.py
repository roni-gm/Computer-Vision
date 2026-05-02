import cv2
import os

def load_image(image_path):
    """
    Fungsi untuk memuat gambar dari path yang diberikan.
    
    :param image_path: path file gambar
    :return: gambar dalam format BGR (default OpenCV)
    """
    if os.path.exists(image_path):
        return cv2.imread(image_path)

    alt_path = os.path.join(os.getcwd(), image_path)
    if os.path.exists(alt_path):
        return cv2.imread(alt_path)

    alt_path2 = os.path.join(os.path.dirname(__file__), '..', image_path)
    if os.path.exists(alt_path2):
        return cv2.imread(alt_path2)

    return None

def convert_to_grayscale(image):
    """
    Fungsi untuk mengonversi gambar BGR ke Grayscale.
    
    :param image: gambar dalam format BGR
    :return: gambar dalam format Grayscale
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  

def convert_to_hsv(image):
    """
    Fungsi untuk mengonversi gambar BGR ke HSV.
    
    :param image: gambar dalam format BGR
    :return: gambar dalam format HSV
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


# Contoh penggunaan (dapat dihapus jika diinginkan)
if __name__ == "__main__":
    # Load image dari file milik Anda untuk mencoba fungsi yang telah dibuat
    image_path = "sample_image.jpg"
    image = load_image(image_path)
    gray_image = convert_to_grayscale(image)
    hsv_image = convert_to_hsv(image)

    # Tampilkan hasil (hapus jika diinginkan)
    cv2.imshow('Grayscale Image', gray_image)
    cv2.imshow('HSV Image', hsv_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()