import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

# Define the main window
root = tk.Tk()
root.title("YOUR AI ASSISTANT")

# Background color
root.configure(bg="steelblue")

# Google Search
def search_google():
    query = entry.get()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# YouTube Search
def search_youtube():
    query = entry.get()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

# Instagram Profile
def search_instagram():
    username = entry.get().replace("@", "")
    url = f"https://www.instagram.com/{username}/"
    webbrowser.open(url)

# Widgets
Label(root, text="Enter your command:", bg="steelblue", fg="white").pack(pady=10)

entry = Entry(root, width=50)
entry.pack(pady=10)

Button(root, text="Search on Google", command=search_google).pack(pady=5)
Button(root, text="Search on YouTube", command=search_youtube).pack(pady=5)
Button(root, text="Search on Instagram", command=search_instagram).pack(pady=5)

# Run GUI
root.mainloop()