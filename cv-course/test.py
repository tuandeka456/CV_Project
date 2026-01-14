import cv2

# Initialize video capture from default camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Display the resulting frame
    cv2.imshow('frame', gray)
    
    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()