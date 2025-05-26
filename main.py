import time
import pyautogui
import tkinter as tk
from tkinter import ttk
import threading

class WhatsAppSpammer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("WhatsApp Spammer")
        self.root.geometry("580x295")
        
        # Configure dark theme colors
        self.bg_color = "#2b2b2b"
        self.fg_color = "#ffffff"
        self.accent_color = "#7289da"
        self.button_color = "#404040"
        self.stop_color = "#d9534f"  # Red for stop
        self.status_running_color = "#5cb85c"  # Green
        self.status_stopped_color = "#d9534f"  # Red
        
        # Configure root window
        self.root.configure(bg=self.bg_color)
        self.root.attributes('-topmost', True)
        
        # Configure ttk styles
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure styles for different widgets
        default_font = ('Montserrat', 10)
        title_font = ('Montserrat', 14, 'bold')
        button_font = ('Montserrat', 10, 'bold')
        status_font = ('Montserrat', 10, 'italic')
        # fallback to Arial if Montserrat is not available
        try:
            self.root.option_add('*Font', 'Montserrat 10')
        except:
            default_font = ('Arial', 10)
            title_font = ('Arial', 14, 'bold')
            button_font = ('Arial', 10, 'bold')
            status_font = ('Arial', 10, 'italic')

        self.style.configure('TFrame', background=self.bg_color)
        self.style.configure('TLabel', 
                           background=self.bg_color, 
                           foreground=self.fg_color,
                           font=default_font)
        self.style.configure('TButton',
                           background=self.button_color,
                           foreground=self.fg_color,
                           font=button_font,
                           padding=10)
        self.style.map('TButton',
                      background=[('active', self.accent_color)],
                      foreground=[('active', self.fg_color)])
        self.style.configure('TEntry',
                           fieldbackground=self.button_color,
                           foreground=self.fg_color,
                           font=default_font,
                           padding=5)
        self.style.configure('Red.TButton',
                            background=self.stop_color,
                            foreground=self.fg_color,
                            font=button_font,
                            padding=10)
        self.style.map('Red.TButton',
                       background=[('active', self.stop_color)],
                       foreground=[('active', self.fg_color)])
        
        # Create main frame with padding
        self.frame = ttk.Frame(self.root, padding="20")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(self.frame, 
                              text="WhatsApp Spammer",
                              font=title_font)
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 16))
        
        # Name input with better layout
        name_frame = ttk.Frame(self.frame)
        name_frame.grid(row=1, column=0, columnspan=2, pady=12, sticky='ew')
        
        ttk.Label(name_frame, 
                 text="Friend's Name:",
                 font=default_font).grid(row=0, column=0, padx=(0, 10))
        
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(name_frame, 
                                  textvariable=self.name_var,
                                  width=28)
        self.name_entry.grid(row=0, column=1, padx=(0, 4))
        
        # Button frame for better spacing
        button_frame = ttk.Frame(self.frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=18)
        
        # Buttons with better styling
        self.start_button = ttk.Button(button_frame,
                                     text="Start Spamming",
                                     command=self.start_spamming,
                                     width=15)
        self.start_button.grid(row=0, column=0, padx=10)
        
        self.stop_button = ttk.Button(button_frame,
                                     text="Stop",
                                     command=self.stop_spamming,
                                     state='disabled',
                                     width=15,
                                     style='TButton')
        self.stop_button.grid(row=0, column=1, padx=10)
        
        # Status label with better styling
        self.status_label = ttk.Label(self.frame,
                                    text="Status: Ready",
                                    font=status_font)
        self.status_label.grid(row=3, column=0, columnspan=2, pady=12)
        
        # Initialize variables
        self.is_running = False
        self.spam_thread = None
        
        self.animals = [
            "ant", "bear", "cat", "dog", "elephant", "fox", "giraffe", "horse", "iguana", "jaguar",
            "kangaroo", "lion", "monkey", "newt", "owl", "panda", "quokka", "rabbit", "snake", "tiger",
            "unicorn", "vulture", "wolf", "xerus", "zebra", 
            "alpaca", "bat", "cheetah", "dolphin", "eagle", "flamingo", "goat", "hamster", "impala",
            "jellyfish", "koala", "lemur", "mongoose", "narwhal", "otter", "penguin", "quail", "rhinoceros",
            "sloth", "toucan", "urial", "viper", "wombat", "x-ray tetra", "yabby", "zebu",
            "alligator", "buffalo", "chimpanzee", "dalmatian", "elephant seal", "frog", "gazelle", "hedgehog",
            "ibex", "jackal"
        ]

    def spam_messages(self):
        name = self.name_var.get()
        if not name:
            self.status_label.config(text="Status: Please enter a name!", foreground=self.status_stopped_color)
            self.stop_spamming()
            return
        self.status_label.config(text="Status: Running...", foreground=self.status_running_color)
        self.stop_button.config(style='Red.TButton')
        while self.is_running:
            for animal in self.animals:
                if not self.is_running:
                    break
                message = f"*{name}* `aik {animal} hai`"
                pyautogui.typewrite(message)
                pyautogui.press('enter')
                # Responsive sleep: check self.is_running every 0.05s for 1s
                for _ in range(20):
                    if not self.is_running:
                        break
                    time.sleep(0.05)
        self.stop_button.config(style='TButton')

    def start_spamming(self):
        self.is_running = True
        self.start_button.config(state='disabled')
        self.stop_button.config(state='normal')
        self.name_entry.config(state='disabled')
        self.spam_thread = threading.Thread(target=self.spam_messages)
        self.spam_thread.start()

    def stop_spamming(self):
        self.is_running = False
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')
        self.name_entry.config(state='normal')
        self.stop_button.config(style='TButton')
        self.root.after(0, lambda: self.status_label.config(text="Status: Stopped", foreground=self.status_stopped_color))

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = WhatsAppSpammer()
    app.run()

