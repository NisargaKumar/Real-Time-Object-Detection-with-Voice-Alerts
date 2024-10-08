# Real-Time-Object-Detection-with-Voice-Alerts
**Overview**:
A real-time object detection system that integrates voice notifications using computer vision and text-to-speech technologies, enhancing accessibility and user interaction.

**Features**:
**Real-time Object Detection**: Uses OpenCV and Cvzone.
**Voice Alerts**: Provides auditory feedback via Pyttsx3.
**Machine Learning**: Custom-trained model through Teachable Machine.
**Efficient Processing**: Utilizes multithreading for smooth performance.

**Tools and Technologies**:
**Programming Language**: Python
**Libraries**: OpenCV, Cvzone, Pyttsx3, TensorFlow
**Hardware**: Camera (Either Webcam or Droidcam) and speakers

**Steps to Create and Run the Project**

1)  Clone the Repository:

- Open your terminal or Git Bash.  
- Clone the repository:  
  git clone https://github.com/your-username/real-time-object-detection.git

2) Navigate to the Project Directory:  
   cd real-time-object-detection  

3) Install Required Dependencies:  
- Create a requirements.txt file in the project directory and add the following:  
opencv-python  
cvzone  
pyttsx3  
tensorflow  

- Install the dependencies:  
  pip install -r requirements.txt  
 
- Run the Project:  
  python main.py  



**BUILDING FROM SCRATCH**
1. **Create the Machine Learning Model with Teachable Machine**
- Visit Teachable Machine:  
    Go to Teachable Machine.

- Select the Model Type:  
    Choose "Image Project" to create a model for object detection.

- Upload Training Images:  
    Click on "Get Started".
    Use your webcam or upload images for different objects you want to recognize. Label each class accordingly.

- Train the Model:  
    Once you've uploaded images, click on "Train Model". Wait for the process to complete.

- Export the Model:  
    After training, click "Export Model".

Choose "TensorFlow" and download the model files, including the .h5 file and the labels file.

**2. Set Up Your Development Environment**

- Install Required Libraries:  
    Open your terminal or command prompt and run:  
    pip install opencv-python cvzone pyttsx3 tensorflow

**3. Create Your Project Structure**  

- Create a New Directory:
  - Create a folder for your project:
      mkdir real-time-object-detection
      cd real-time-object-detection

- Add Model Files:
    Place the downloaded .h5 model file and the labels text file into the project directory, organizing them into a folder called MyModel.

**4. Write the Main Script**

- Create main.py:
    In the project directory, create a file named main.py
