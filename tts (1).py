import pyttsx3
from win10toast import ToastNotifier

notify = ToastNotifier()

frist,second =input("Frist:  "),input("second: ")
def savetts(nametosave,secondoptiontosave,filename):
    
    engine = pyttsx3.init()

    location = r"E:\fics\mabe i will read"
    rate = engine.getProperty('rate')   
    engine.setProperty('rate', 150) 

    text = filename
    engine.save_to_file(text,f"{location}\{nametosave} to {secondoptiontosave}.mp3")
    print("file is been processed......")
    engine.runAndWait()
    print("\nfile has been saved.")
    notify.show_toast("Completed","File is saved.",duration=5)


with open("chap.txt", "r", encoding="utf-8") as f:
        savetts(frist,second,f.read())