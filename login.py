import face_recognition
from tkinter import *
import cv2
from PIL import Image, ImageTk
import os

class Webcam:
    def __init__(self, window):
        self.__window = window
        self.__window.title("Teacher's Portal - Login")

        f = open("teacher.txt", "r")
        self.__teacher = f.read()

        #Initializes OpenCV camera and current_image variable
        self.__video_capture = cv2.VideoCapture(0)
        self.__current_image = None
        
        #Creates space for webcam
        self.__canvas = Canvas(window, width=1800, height=900)
        self.__canvas.pack()

        self.__login_button = Button(window, text="Login", command=self.try_login)
        self.__login_button.pack()

        self.__back_button = Button(window, text="Return", command=self.run)
        self.__back_button.pack()

        #Runs webcam
        self.update_webcam()

    def update_webcam(self):
        ret,frame = self.__video_capture.read()

        #Checks if there was a return in the camera
        if ret:
            #Creates image from current frame
            self.__current_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            self.__photo = ImageTk.PhotoImage(image=self.__current_image)
            self.__canvas.create_image(0,0,image=self.__photo,anchor=NW)

            #Runs every 10 milliseconds, making a live camera
            self.__window.after(10,self.update_webcam)

    def try_login(self):
        if self.__current_image is not None:
            path = os.path.expanduser('./current_image.jpg')
            self.__current_image.save(path)

            #Formats image so that it can be detected
            ref_detection1 = face_recognition.load_image_file(f"images/{self.__teacher}/image1.png")
            ref_detection2 = face_recognition.load_image_file(f"images/{self.__teacher}/image2.png")
            current_detection = face_recognition.load_image_file("./current_image.jpg")

            #Encodes each image
            ref_encoding1 = face_recognition.face_encodings(ref_detection1)[0]
            ref_encoding2 = face_recognition.face_encodings(ref_detection2)[0]
            current_encoding = face_recognition.face_encodings(current_detection)[0]

            #Compares images: result is returned as list of boolean values (tolerance is 60% similarity)
            results = face_recognition.compare_faces([ref_encoding1, ref_encoding2], current_encoding, 0.6)

            if results[0] == True or results[1] == True:
                success = Label(self.__window,text="Success")
                success.pack()
                
            else:
                failure = Label(self.__window, text="Failure")
                failure.pack()

            os.remove("./current_image.jpg")

    def run(self):
        os.system("python3 main.py")
        body.destroy()

body = Tk()

app = Webcam(body)

body.mainloop()