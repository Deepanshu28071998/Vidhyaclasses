import tkinter as tk
from tkinter import scrolledtext
import requests

# Function to send a message to Flask backend and get a response
def send_message(event=None):
    user_message = user_input.get()  # Get the message from the input box
    if user_message.strip() == "":
        return  # If input is empty, do nothing
    
    # Display user message in the chat window
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_message + "\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)  # Scroll to the bottom

    # Send message to Flask server (adjust the URL based on your Flask server)
    try:
        response = requests.post("http://127.0.0.1:5000/chat", json={"message": user_message})
        bot_message = response.json().get("reply")
    except:
        bot_message = "Error: Unable to connect to the chatbot server."
    
    # Display bot response in the chat window
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "Bot: " + bot_message + "\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)  # Scroll to the bottom
    
    user_input.delete(0, tk.END)  # Clear the input box

# Initialize the GUI application
root = tk.Tk()
root.title("Chatbot")

# Chat window (scrolled text area)
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# User input field
user_input = tk.Entry(root, width=100)
user_input.pack(padx=10, pady=10, fill=tk.X)
user_input.bind("<Return>", send_message)  # Bind the Enter key to send_message

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()
