import cv2



image = cv2.imread('nature.jpg')


cv2.namedwindow('Load Image', cv2.Window_Normal)

cv2.resizeWindow('Load Image', 800, 500)


cv2.imshow('Loaded Image', image)

cv2.waitKey(0) # Wait for a key press

cv2.destroyAllWindow() # Close the window


# Print image properties

print(f"Image Dimensions : {image.shape}") # Height, Width, Channels