import pytesseract
from PIL import Image, ImageTk
import pyttsx3
from googletrans import Translator
import tkinter as tk
from tkinter import filedialog

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = 'D:/study/sem7/minor_project/tesseract/tesseract.exe'

# A dictionary to map language names to their codes
language_codes = {"Afrikaans": "af", "Albanian": "sq", "Amharic": "am", "Arabic": "ar", "Armenian": "hy", "Azerbaijani": "az","Basque": "eu", "Belarusian": "be", "Bengali": "bn", "Bosnian": "bs", "Bulgarian": "bg", "Catalan": "ca","Cebuano": "ceb", "Chichewa": "ny", "Chinese (Simplified)": "zh-cn", "Chinese (Traditional)": "zh-tw","Corsican": "co", "Croatian": "hr", "Czech": "cs", "Danish": "da", "Dutch": "nl", "Esperanto": "eo","Estonian": "et", "English": "en", "Filipino": "tl", "Finnish": "fi", "French": "fr", "Frisian": "fy","Galician": "gl", "Georgian": "ka", "Greek": "el", "Gujarati": "gu", "Haitian Creole": "ht", "Hausa": "ha","Hawaiian": "haw", "Hebrew": "iw", "Hindi": "hi", "Hmong": "hmn", "Hungarian": "hu", "Icelandic": "is","Igbo": "ig", "Indonesian": "id", "Irish": "ga", "Italian": "it", "Japanese": "ja", "Javanese": "jw","Kannada": "kn", "Kazakh": "kk", "Khmer": "km", "Kinyarwanda": "rw", "Korean": "ko", "Kurdish (Kurmanji)": "ku","Kyrgyz": "ky", "Lao": "lo", "Latin": "la", "Latvian": "lv", "Lithuanian": "lt", "Luxembourgish": "lb","Macedonian": "mk", "Malagasy": "mg", "Malay": "ms", "Malayalam": "ml", "Maltese": "mt", "Maori": "mi","Marathi": "mr", "Mongolian": "mn", "Myanmar (Burmese)": "my", "Nepali": "ne", "Norwegian": "no", "Odia": "or","Pashto": "ps", "Persian": "fa", "Polish": "pl", "Portuguese": "pt", "Punjabi": "pa", "Romanian": "ro","Russian": "ru", "Samoan": "sm", "Scots Gaelic": "gd", "Serbian": "sr", "Sesotho": "st", "Shona": "sn","Sindhi": "sd", "Sinhala": "si", "Slovak": "sk", "Slovenian": "sl", "Somali": "so", "Sundanese": "su","Swahili": "sw", "Swedish": "sv", "Tajik": "tg", "Tamil": "ta", "Tatar": "tt", "Telugu": "te", "Thai": "th","Turkish": "tr", "Turkmen": "tk", "Ukrainian": "uk", "Urdu": "ur", "Uyghur": "ug", "Uzbek": "uz","Vietnamese": "vi", "Welsh": "cy", "Xhosa": "xh", "Yiddish": "yi", "Yoruba": "yo", "Zulu": "zu"}


def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        translate_text(file_path)

def translate_text(image_path):
    img = Image.open(image_path)
    result = pytesseract.image_to_string(img)

    # Get user's desired language for translation
    target_language = language_selection_var.get()

    p = Translator()
    translated_text = p.translate(result, dest=target_language)   

    # Clear previous labels
    original_label.config(text="Original Text:")
    translated_label.config(text="Translated Text:")
    image_label.config(image=None)

    # Update labels with new information
    original_text_var.set(result)
    translated_text_var.set(translated_text.text)

    # Display the image in the GUI
    img.thumbnail((300, 300))
    img_tk = ImageTk.PhotoImage(img)
    image_label.img = img_tk
    image_label.config(image=img_tk)

    # Speak translated text
    engine = pyttsx3.init()
    engine.say(translated_text.text)
    engine.runAndWait()

# GUI setup
root = tk.Tk()
root.title("Image to Text and Translation")

# Create variables to store text information
original_text_var = tk.StringVar()
translated_text_var = tk.StringVar()

# Labels to display original and translated text
original_label = tk.Label(root, text="Original Text:", font=("Helvetica", 14))
original_label.pack(pady=5)

original_text_label = tk.Label(root, textvariable=original_text_var, wraplength=400, font=("Helvetica", 12))
original_text_label.pack(pady=5)

translated_label = tk.Label(root, text="Translated Text:", font=("Helvetica", 14))
translated_label.pack(pady=5)

translated_text_label = tk.Label(root, textvariable=translated_text_var, wraplength=400, font=("Helvetica", 12))
translated_text_label.pack(pady=5)

# Label to display the image
image_label = tk.Label(root,text="Source Image:", font=("Helvetica", 14))
image_label.pack(pady=10)

# Dropdown menu to select target language
language_selection_var = tk.StringVar()
language_selection_var.set("en")  # Default language is English
language_menu = tk.OptionMenu(root, language_selection_var, *language_codes.keys())
language_menu.pack(pady=5)

browse_button = tk.Button(root, text="Browse Image", command=browse_image)
browse_button.pack(pady=10)

root.mainloop()
