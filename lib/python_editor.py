import tkinter as tk
from tkinter import scrolledtext
from pygments import lex
from pygments.lexers import PythonLexer
from pygments.token import Token
import time
import re

class PythonTextEditor:
    def __init__(self, root, music_controller, rules):
        self.root = root
        self.music_controller = music_controller
        self.rules = rules
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH)
        self.text_area.bind('<KeyRelease>', self.on_key_release)
        self.configure_tags()
        self.start_time = time.time()
        self.word_count = 0
        self.average_wpm = 0
        self.instantaneous_wpm = 0
        self.def_count = 0
        self.display_widget = tk.Text(root, height=5, state=tk.DISABLED)
        self.display_widget.pack()
        self.audio_param_display = tk.Text(root, height=3, width=80, state=tk.DISABLED)
        self.audio_param_display.pack()

    def configure_tags(self):
        # Syntax highlighting configurations
        tags = {
            "Token.Keyword": "#CC7A00",
            "Token.Name.Class": "#0000FF",
            "Token.Name.Exception": "#0000FF",
            "Token.Name.Function": "#0000FF",
            "Token.Operator.Word": "#CC7A00",
            "Token.Comment": "#008000",
            "Token.Literal.String": "#BA2121",
        }
        for tag, color in tags.items():
            self.text_area.tag_configure(tag, foreground=color)

    def on_key_release(self, event):
        self.highlight_text()
        self.update_typing_stats()
        self.update_def_count()
        self.update_music_based_on_stats()
        self.update_title_bar()
        self.music_controller.update_display(self.display_widget)

    def update_typing_stats(self):
        text = self.text_area.get("1.0", tk.END)
        words = text.split()
        current_word_count = len(words)
        if current_word_count > self.word_count:
            current_time = time.time()
            time_diff = current_time - self.start_time
            self.instantaneous_wpm = 60 / time_diff
            self.average_wpm = current_word_count / (time_diff / 60)
            self.word_count = current_word_count
            self.start_time = current_time


    def update_def_count(self):
        text = self.text_area.get("1.0", tk.END)
        self.def_count = len(re.findall(r'\bdef\b', text))

    def update_music_based_on_stats(self):
        for melody_name, melody_rules in self.rules.items():
            for stat, effect in melody_rules.items():
                current_stat = self.get_stat(stat)
                effect_method = getattr(self.music_controller, effect['method'])

                if effect_method == self.music_controller.adjust_melody_adsr:
                    # Handle ADSR adjustments
                    attack, decay, sustain, release = effect['function'](current_stat)
                    effect_method(melody_name, attack=attack, decay=decay, sustain=sustain, release=release)
                else:
                    # Handle other adjustments
                    adjustment_value = effect['function'](current_stat)
                    effect_method(melody_name, adjustment_value)


    def get_stat(self, stat_name):
        if stat_name == 'instantaneous_wpm':
            return self.instantaneous_wpm
        elif stat_name == 'average_wpm':
            return self.average_wpm
        elif stat_name == 'def_count':
            return self.def_count

    def highlight_text(self):
        text = self.text_area.get("1.0", 'end-1c')
        self.text_area.mark_set("range_start", "1.0")
        data = text.encode('utf-8')
        for token, content in lex(data, PythonLexer()):
            self.text_area.mark_set("range_end", "range_start + %dc" % len(content))
            self.text_area.tag_add(str(token), "range_start", "range_end")
            self.text_area.mark_set("range_start", "range_end")

    def update_title_bar(self):
        stats = f"Avg WPM: {self.average_wpm:.2f}, Instant WPM: {self.instantaneous_wpm:.2f}, 'def' count: {self.def_count}"
        self.root.title(stats)


