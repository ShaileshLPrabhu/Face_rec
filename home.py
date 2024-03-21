import os  # accessing the os functions
import check_camera,Capture_Image,Train_Image,Recognize
def title_bar():
    os.system('cls')  # for windows
    # title of the program

    print("\t**********************************************")
    print("\t***** Face Recognition Attendance System *****")
    print("\t**********************************************")

def mainMenu():
    title_bar()
    print()
    print(10 * "*", "WELCOME MENU", 10 * "*")
    print("[1] Check Camera")
    print("[2] Capture Faces")
    print("[3] Train Images")
    print("[4] Recognize & Attendance")
    print("[5] Quit")

    while True:
        try:
            choice = int(input("Enter Choice: "))
            if choice == 1:
                print("check camera...")
                checkCamera()
                break
            elif choice == 2:
                print("Capture image from video...")
                CaptureFaces()
                break
            elif choice == 3:
                print("Train images...")
                Trainimages()
                break
            elif choice == 4:
                print("Recognize face...")
                RecognizeFaces()
                break
            elif choice == 5:
                print("Thank You, bye...")
                break
            else:
                print("Invalid Choice. Enter 1-5")
                mainMenu()
        except Exception as e:
            print("Error:", e)
            print("Invalid Choice. Enter 1-5\n Try Again")


#------------Menus-------#
# ---------------------------------------------------------
# calling the camera test function from check camera.py file
def checkCamera():
    check_camera.camer()
    print("For check camera...")
    key = input("Enter any key to return main menu")
    mainMenu()

# --------------------------------------------------------------
# calling the take image function form capture image.py file

def CaptureFaces():
    Capture_Image.takeImages()
    key = input("Enter any key to return main menu")
    mainMenu()

def Trainimages():
    Train_Image.TrainImages()
    key = input("Enter any key to return main menu")
    mainMenu()

def RecognizeFaces():
    Recognize.recognize_attendence()
    key = input("Enter any key to return main menu")
    mainMenu()

mainMenu()

