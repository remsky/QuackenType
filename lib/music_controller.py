# %%
import time
import threading

from pyo import Server

from lib.notes import NOTES
from lib.chords import CHORDS
from lib.melody import Melody


class MusicController:
    def __init__(self):
        self.server = Server().boot()
        self.server.start()
        self.melodies = {}

    def add_melody(self, name, chords):
        melody = Melody(chords)
        self.melodies[name] = melody
        threading.Thread(target=melody.play).start()

    def remove_melody(self, name):
        if name in self.melodies:
            self.melodies[name].playing = False
            del self.melodies[name]

    def adjust_melody_pitch(self, name, pitch_multiplier):
        if name in self.melodies:
            self.melodies[name].set_pitch(pitch_multiplier)

    def adjust_melody_tempo(self, name, tempo_multiplier):
        if name in self.melodies:
            self.melodies[name].set_tempo(tempo_multiplier)

    def adjust_melody_adsr(self, name, attack=None, decay=None, sustain=None, release=None):
        if name in self.melodies:
            melody = self.melodies[name]

            # Get current ADSR values from the melody
            current_attack, current_decay, current_sustain, current_release = melody.attack, melody.decay, melody.sustain, melody.release

            # Update the ADSR parameters only if they are specified
            attack = attack if attack is not None else current_attack
            decay = decay if decay is not None else current_decay
            sustain = sustain if sustain is not None else current_sustain
            release = release if release is not None else current_release

            melody.set_adsr(attack, decay, sustain, release)
            
    def stop_all(self):
        for melody in self.melodies.values():
            melody.stop()
        self.server.stop()
