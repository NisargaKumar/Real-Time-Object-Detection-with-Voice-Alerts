import cv2
import cvzone
import pyttsx3
import threading

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function for speech output in a separate thread
def speak_out(object_name):
    engine.say(f"I see {object_name}")
    engine.runAndWait()

# Load labels from the file
with open('MyModel/labels2.txt', 'r') as f:
    labels = f.read().strip().split('\n')

# Initialize video capture
cap = cv2.VideoCapture(1)

# Load classifier
myClassifier = cvzone.Classifier('MyModel/keras_model.h5', 'MyModel/labels2.txt')

while True:
    _, img = cap.read()
    predictions, index = myClassifier.getPrediction(img)

    if predictions:
        # Get the index of the highest confidence prediction
        pred_index = predictions.index(max(predictions))
        
        # Get the corresponding label
        object_name = labels[pred_index]
        print(f"Detected object: {object_name}")
        
        # Speak out the detected object
        threading.Thread(target=speak_out, args=(object_name,)).start()
        
        # Display the detected object name on the image
        cv2.putText(img, str(object_name), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the image
    cv2.imshow("Image", img)
    
    key = cv2.waitKey(1)
    if key == 27:  # Press Esc to exit
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
