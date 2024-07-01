# app.py

import tkinter as tk
from resume_management import ResumeBuilderUI

def main():
    root = tk.Tk()
    app = ResumeBuilderUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
