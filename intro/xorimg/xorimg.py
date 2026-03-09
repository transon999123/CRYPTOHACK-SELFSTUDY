#download cv2: pip install opencv-contrib-python
#xor 2 ảnh vô với nhau
import cv2
i1=cv2.imread('img1.png')
i2=cv2.imread('img2.png')
if i1 is not None and i2 is not None and i1.shape == i2.shape:
    # XOR bitwise 2 ảnh
    result_image = cv2.bitwise_xor(i1, i2)

    # In ảnh
    cv2.imshow("XOR Result", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#crypto{X0Rly_n0t!}
