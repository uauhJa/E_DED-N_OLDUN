
import speech_recognition as sr
import pyautogui
import pyperclip
import time

r = sr.Recognizer()

print("E DEDİN OLDUN")
print("Mikrofon başlatılıyor...")

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)

    while True:
        try:
            audio = r.listen(source)
            word = r.recognize_google(audio, language="tr-TR")

            print("Algılandı:", word)

            pyperclip.copy("!ses " + word)
            pyautogui.press("t")
            time.sleep(0.2)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.press("enter")

        except sr.UnknownValueError:
            print("Anlaşılamadı")

        except Exception as e:
            print("Hata:", e)
            time.sleep(1)

