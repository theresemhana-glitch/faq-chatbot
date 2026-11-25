import tkinter as tk
from chatbot import get_answer

window = tk.Tk()
window.title("FAQ Bot")

chat = tk.Text(window, width=60, height=20, state="disabled", wrap="word")
chat.pack(padx=10, pady=10)

entry = tk.Entry(window, width=50)
entry.pack(side="left", padx=10, pady=(0, 10))


def add(text):
    chat.config(state="normal")
    chat.insert("end", text + "\n\n")
    chat.config(state="disabled")
    chat.see("end")


def send(event=None):
    text = entry.get().strip()
    if not text:
        return
    entry.delete(0, "end")
    add("You: " + text)
    add("Bot: " + get_answer(text))


entry.bind("<Return>", send)
tk.Button(window, text="Send", command=send).pack(side="left", pady=(0, 10))

add("Bot: Hi! Ask me a question.")
window.mainloop()