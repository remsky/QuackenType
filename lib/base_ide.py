import tkinter as tk
from tkinter import scrolledtext
from pygments import lex
from pygments.lexers import PythonLexer
from pygments.token import Token
import time

class PythonTextEditor:
    def __init__(self, root):
        self.root = root
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH)
        self.text_area.bind('<KeyRelease>', self.on_key_release)
        self.text_area.tag_configure("Token.Keyword", foreground="#CC7A00")
        self.text_area.tag_configure("Token.Keyword.Constant", foreground="#CC7A00")
        self.text_area.tag_configure("Token.Keyword.Declaration", foreground="#CC7A00")
        self.text_area.tag_configure("Token.Keyword.Namespace", foreground="#CC7A00")
        self.text_area.tag_configure("Token.Keyword.Pseudo", foreground="#CC7A00")
        self.text_area.tag_configure("Token.Keyword.Reserved", foreground="#CC7A00")
        self.text_area.tag_configure("Token.Keyword.Type", foreground="#CC7A00")
        self.text_area.tag_configure("Token.Name.Class", foreground="#0000FF")
        self.text_area.tag_configure("Token.Name.Exception", foreground="#0000FF")
        self.text_area.tag_configure("Token.Name.Function", foreground="#0000FF")
        self.text_area.tag_configure("Token.Operator.Word", foreground="#CC7A00")
        self.text_area.tag_configure("Token.Comment", foreground="#008000")
        self.text_area.tag_configure("Token.Literal.String", foreground="#BA2121")
        self.last_keypress_time = time.time()

    def on_key_release(self, event):
        self.highlight_text()
        current_time = time.time()
        typing_speed = 1 / (current_time - self.last_keypress_time) * 60  # Words per minute
        self.last_keypress_time = current_time
        word_count = len(self.text_area.get("1.0", tk.END).split())
        # Update external stuff based on word count, typing speed, etc.
        print(f"Word Count: {word_count}, Typing Speed: {typing_speed:.2f} WPM")

    def highlight_text(self):
        text = self.text_area.get("1.0", 'end-1c')
        self.text_area.mark_set("range_start", "1.0")
        data = text.encode('utf-8')
        for token, content in lex(data, PythonLexer()):
            self.text_area.mark_set("range_end", "range_start + %dc" % len(content))
            self.text_area.tag_add(str(token), "range_start", "range_end")
            self.text_area.mark_set("range_start", "range_end")

if __name__ == "__main__":
    root = tk.Tk()
    editor = PythonTextEditor(root)
    root.mainloop()
