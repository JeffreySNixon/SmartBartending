import cv2
import os
import tkinter as tk
import boto3
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import zipfile
import shutil


obj = boto3.client("s3")

obj.download_file(
    Filename="SmartBartending/facial_recognition/dataset.zip",	# directory + name where to download .zip
    Bucket="smartbartending-faces",				# desired s3 bucket
    Key="dataset.zip"					# name assigned to .zip in the s3 bucket
)
with zipfile.ZipFile('SmartBartending/facial_recognition/dataset.zip') as zObject: 
  
    # Extracting all the members of the zip  
    # into a specific location. 
        zObject.extractall( 
        path='SmartBartending/facial_recognition/dataset') 

class PhotoCaptureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Capture App")

        self.user_name = simpledialog.askstring("Input", "Enter your name:")
        self.photo_folder = 'SmartBartending/facial_recognition/dataset/dataset/' + self.user_name

        # Create folder for photos
        os.makedirs(self.photo_folder, exist_ok=True)

        self.photo_count = 0

        self.capture_button = tk.Button(root, text="Capture Photo", command=self.capture_photo)
        self.capture_button.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=self.root.destroy)
        self.quit_button.pack(pady=10)

        # Create a Canvas to display the camera feed
        self.canvas = tk.Canvas(root, width=640, height=480)
        self.canvas.pack()

        # Open a camera capture
        self.cap = cv2.VideoCapture(0)

        # Update the camera feed on the canvas
        self.update_camera_feed()

    def update_camera_feed(self):
        # Capture a single frame
        ret, frame = self.cap.read()

        # Convert the frame from BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the RGB frame to a PhotoImage
        img = ImageTk.PhotoImage(Image.fromarray(rgb_frame))

        # Update the canvas with the new image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
        self.canvas.image = img

        # Schedule the function to run again after 10 milliseconds
        self.root.after(10, self.update_camera_feed)

    def capture_photo(self):
        if self.photo_count < 10:
            # Capture a single frame in RGB
            ret, frame = self.cap.read()
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Save the captured photo
            photo_path = os.path.join(self.photo_folder, f"photo_{self.photo_count + 1}.png")
            cv2.imwrite(photo_path, cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR))

            self.photo_count += 1
            if self.photo_count == 10:
                self.capture_button.config(state=tk.DISABLED)
                messagebox.showinfo("Info", "Photo capture completed!")

                shutil.make_archive("SmartBartending/facial_recognition/dataset/dataset", 'zip', "SmartBartending/facial_recognition/dataset", "dataset")
                obj.upload_file(
	                Filename='SmartBartending/facial_recognition/dataset.zip', # directory where the .zip is located
	                Bucket="smartbartending-faces",			# destination s3 bucket
	                Key="dataset.zip"				# name assigned to .zip in the s3 bucket
                    )

                if os.path.isdir("SmartBartending/facial_recognition/dataset"):
                    shutil.rmtree("SmartBartending/facial_recognition/dataset")
        else:
            messagebox.showinfo("Info", "You have already captured 10 photos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoCaptureApp(root)
    root.mainloop()
