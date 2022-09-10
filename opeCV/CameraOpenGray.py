import cv2


# define a video capture object
cap = cv2.VideoCapture(0)
#we write this line to make the video watchaple for all systems
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#save video to watch
out = cv2.VideoWriter('output.avi', fourcc, 20.0,(640,480))
while(True):

    # Capture the video frame by frame
    ret, frame = cap.read()
    #to make video gray
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    #Display the gray frame
    cv2.imshow('gray' , gray)
    #save the regular frame
    out.write(frame)
    # the 'q' button is set as the quitting button
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
cap.release()
# After the loop release the out object
out.release()
# Destroy all the windows
cv2.destroyAllWindows()
