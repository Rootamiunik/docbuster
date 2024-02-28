#!/bin/python3
import os
import undetected_chromedriver
from bs4 import BeautifulSoup
import time
import pyttsx3
from win10toast import ToastNotifier

notify = ToastNotifier()


def savetts(nametosave,secondoptiontosave,filename):
    engine = pyttsx3.init()

    location = r"E:\fics\chaptes\shadow of konoha"
    rate = engine.getProperty('rate')   
    engine.setProperty('rate', 150) 

    text = filename
    engine.save_to_file(text,f"{location}\{nametosave} to {secondoptiontosave}.mp3")
    print("file is been processed......")
    engine.runAndWait()
    print("\nfile has been saved.")
    notify.show_toast("Completed","File is saved.",duration=5)



def delpreviousfile():
    file_path = r"chap.txt"
    if os.path.isfile(file_path):
        os.remove(file_path)
        print("File has been deleted")
    else:
       pass

        

text_list = []
strings = ""
tim = 80

delpreviousfile()


if __name__ == "__main__":
    driver = undetected_chromedriver.Chrome()
    user_input = input("Url: ")
    previous_chapter = int(input("Start from chapter: "))
    chapter = int(input("To no: "))

    for inum in range(previous_chapter,chapter+1):
        driver.get(f"{user_input}{inum}")
        time.sleep(tim)
        html_data = driver.page_source
        soup = BeautifulSoup(html_data,"html.parser")

        tags = soup.find_all("p")

        for i in tags[1::]:
            text_list.append(str(i))

        for x in text_list:
            strings = strings + x

        strings = strings.replace("<p>"," ")
        strings = strings.replace("</p>"," ")
        strings = strings.replace("<em>"," ")
        strings = strings.replace("</em>"," ")
        strings = strings.replace("<strong>"," ")
        strings = strings.replace("</strong>"," ")
        strings = strings.replace("<span style=","")
        strings = strings.replace("text-decoration: underline;","")
        strings = strings.replace('''</span>!" ''',"")
        strings = strings.replace("text-decoration:underline;","")
        strings = strings.replace("xxxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxxx","-Break")
        strings = strings.replace("xXx","-Break")

        with open("chap.txt", "w", encoding="utf-8") as f:
            f.writelines(strings)
        tim = 3
        print(f"chapter no {inum}.Done")
        text_list.clear()
    print("\nAll chapter are completed downloading")
    notify.show_toast("location","Select location to save the file.",duration=1)
    with open("chap.txt", "r", encoding="utf-8") as f:
        savetts(previous_chapter,chapter,f.read())