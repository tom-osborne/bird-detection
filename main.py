import pafy
import cv2

URL = "https://www.youtube.com/watch?v=7EPJEg6R3SM"
VIDEO = pafy.new(URL)
BEST = VIDEO.getbest(preftype="mp4")
CAPTURE = cv2.VideoCapture(BEST.url)
BIRDS_CASCADE = cv2.CascadeClassifier("birds1.xml")

count = 0
while True:
    grabbed, frame = CAPTURE.read()
    
    if count % 10 == 0:
        
        # convert the frame into gray scale for better analysis
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        birds = BIRDS_CASCADE.detectMultiScale(
            grey,
            scaleFactor=1.8,
            minNeighbors=5,
            minSize=(10, 10),
            maxSize=(660, 660),
            flags = cv2.CASCADE_SCALE_IMAGE 
        )
        if (len(birds) >= 1):
            print(f"Detected a Bird in Frame {count}!")
                
            # Draw a rectangle around the detected birds approaching the farm
            for (x, y, w, h) in birds:
                cv2.rectangle(grey, (x, y), (x+w, y+h), (0, 200, 0), 2)
            
            cv2.imwrite("./frames/frame%d.jpg" % count, grey)

        

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
  
    count += 1