import cv2

# Color planes

img = cv2.imread('images/fruit.png')
cv2.imshow("Fruit image", img)

print(img.shape)

# TODO: Select a color plane, display it, inspect values from a row

# OpenCV uses BGR
red = img[:,:, 2]
green = img[:,:,1]
blue = img[:,:,0]

print("Red color plane, 100th Row \n {}".format(red[99,:]))
print("Green color plane, 100th Row \n {}".format(green[99,:]))
print("Blue color plane, 100th Row \n {}".format(blue[99,:]))

# Let's draw a horizontal line across that row we picked, just for fun
# But in order to see the line in color we need to convert green to a 3-channel array
green_bgr = cv2.cvtColor(green, cv2.COLOR_GRAY2BGR)

# You will notice that cv2.line uses x-y coordinates instead of row-cols
cv2.line(green_bgr, (0, 99), (green.shape[1], 99), (0, 0, 255))
cv2.imshow("50-th row drawn on the green color plane", green_bgr)


cv2.waitKey(0)
