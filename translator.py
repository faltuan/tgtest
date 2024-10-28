from pynput import keyboard
import pyperclip
from deep_translator import GoogleTranslator
from tkinter import Tk, messagebox
import time

def translate_clipboard_text():
    clipboard_text = get_clipboard_text()

    if clipboard_text:
        # Metni Türkçeye çevir
        translator = GoogleTranslator(source='auto', target='tr')
        translated_text = translator.translate(clipboard_text)

        # Popup olarak göster
        root = Tk()
        root.withdraw()  # Ana pencereyi gizle
        root.attributes('-topmost', True)  # Pencereyi en üstte tut
        messagebox.showinfo("Çeviri", f"{translated_text}")
        root.destroy()
    else:
        print("Panoda metin yok.")

def get_clipboard_text(max_retries=5):
    """Panoyu güvenilir bir şekilde kontrol et."""
    for _ in range(max_retries):
        clipboard_text = pyperclip.paste()
        if clipboard_text:
            return clipboard_text
        time.sleep(0.1)  # Panonun güncellenmesini bekle
    return None

def on_activate_ctrl_c():
    print("Ctrl + C basıldı!")  # Konsola mesaj yazdır
    time.sleep(0.2)  # Panonun güncellenmesini bekle
    translate_clipboard_text()

# Global hotkey dinleyiciyi başlat
with keyboard.GlobalHotKeys({'<ctrl>+c': on_activate_ctrl_c}) as h:
    print("Ctrl + C tuşlarını izliyor...")
    h.join()
