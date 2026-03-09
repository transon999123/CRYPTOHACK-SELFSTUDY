import cv2
i1=cv2.imread('img1.png')
i2=cv2.imread('img2.png')
if i1 is not None and i2 is not None and i1.shape == i2.shape:
    # Perform the bitwise XOR operation
    result_image = cv2.bitwise_xor(i1, i2)

    # Display the result
    cv2.imshow("XOR Result", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#crypto{X0Rly_n0t!}
