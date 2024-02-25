"""
Simple music-responsive python code IDE
"""
# %%
import tkinter as tk
from lib.python_editor import PythonTextEditor
from lib.music_controller import MusicController
from lib.melodies import MELODIES

RULES = {
    'Ambient': {
        'instantaneous_wpm': {
            'method': 'adjust_melody_tempo',
            'function': lambda wpm: wpm / 60
        },
        'average_wpm': {
            'method': 'adjust_melody_adsr',
            'function': lambda avg_wpm: (max(0.01, 0.1 - avg_wpm / 600), 0.1, 0.3, 0.1)
            # Adjusts attack between 0.01 and 0.1 seconds
        }
    },
    'SimpleTune': {
        'def_count': {
            'method': 'adjust_melody_pitch',
            'function': lambda count: 1 + count * 0.1
        }
    }
}

def main():
    root = tk.Tk()

    music_controller = MusicController()
    music_controller.add_melody('Ambient', MELODIES['Ambient'])
    music_controller.add_melody('SimpleTune', MELODIES['SimpleTune'])
    editor = PythonTextEditor(root, music_controller, RULES)
    root.mainloop()

if __name__ == "__main__":
    main()

# %%
