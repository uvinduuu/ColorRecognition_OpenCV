import cv2

''' #Read the image
img = cv2.imread("red.jpeg")

print(img) 

cv2.imshow("Image", img)
cv2.waitKey(0) # keep the image open
'''

# Frame capture from webcam

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) 

while True:
    _, frame = cap.read() # _ to store the return value of the function
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Convert the BGR image to HSV image
    height, width, _ = frame.shape # _ to ignore the third value - number of color channels
    
    cx = int(width / 2)
    cy= int(height / 2)

    #pick the color of the center pixel
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    color = "UNKNOWN"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 15:
        color = "DARK RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW ORANGE"
    elif hue_value < 38:
        color = "YELLOW"
    elif hue_value < 45:
        color = "LIGHT YELLOW"
    elif hue_value < 55:
        color = "YELLOW GREEN"
    elif hue_value < 75:
        color = "GREEN"
    elif hue_value < 85:
        color = "CYAN GREEN"
    elif hue_value < 95:
        color = "CYAN"
    elif hue_value < 110:
        color = "LIGHT BLUE"
    elif hue_value < 130:
        color = "BLUE"
    elif hue_value < 140:
        color = "DARK BLUE"
    elif hue_value < 150:
        color = "VIOLET"
    elif hue_value < 160:
        color = "PURPLE"
    elif hue_value < 170:
        color = "MAGENTA"
    elif hue_value < 179:
        color = "RED"
    else:
        color = "UNKNOWN"
    print(color)

    print(pixel_center)
    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    cv2.putText(frame, color, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (b, g, r), 2, cv2.LINE_AA) # 10, 70 is the position of the text
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3) # 5 is the radius, 3 is the thickness
    
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27: # 27 is the ASCII value of the escape key
        break

cap.release()
cv2.destroyAllWindows()

# The code above is a simple color recognition program that uses the webcam to capture frames and determine the color of the center pixel.

