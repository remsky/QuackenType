# %%
from lib.notes import NOTES
from lib.chords import CHORDS

from pyo import Sine, Adsr
import time

class Melody:
    def __init__(self, chords, base_freq=1, attack=0.01, decay=0.1, sustain=0.3, release=0.1, volume=0.5):
        self.chords = chords  # List of tuples (chord_name, duration)
        self.base_freq = base_freq
        self.attack = attack
        self.decay = decay
        self.sustain = sustain
        self.release = release
        self.volume = volume
        self.osc_env_pairs = self.create_osc_env_pairs()
        self.playing = True

    def create_osc_env_pairs(self):
        osc_env_pairs = {}
        for note, freq in NOTES.items():
            osc = Sine(freq=freq * self.base_freq, mul=0)
            env = Adsr(attack=self.attack, decay=self.decay, sustain=self.sustain, release=self.release, mul=self.volume)
            osc_env_pairs[note] = (osc, env)
        return osc_env_pairs
    

    def play_chord(self, chord_name, duration):
        if duration > 10:
            duration = 10  # Set to some reasonable maximum value
        elif duration < 0:
            duration = 0.1
    
        # Existing code to play the chord
        time.sleep(duration)

        chord_freqs = CHORDS[chord_name]
        for freq in chord_freqs:
            note = [note for note, f in NOTES.items() if f == freq][0]
            osc, env = self.osc_env_pairs[note]
            osc.mul = env
            osc.out()
            env.play()
        time.sleep(duration)

        for freq in chord_freqs:
            note = [note for note, f in NOTES.items() if f == freq][0]
            _, env = self.osc_env_pairs[note]
            env.stop()

    def play(self):
        while self.playing:
            for chord_name, duration in self.chords:
                self.play_chord(chord_name, duration)

    def set_pitch(self, pitch_multiplier):
        self.base_freq = pitch_multiplier
        for note, (osc, _) in self.osc_env_pairs.items():
            osc.setFreq(NOTES[note] * self.base_freq)

    def set_tempo(self, tempo_multiplier):
        self.chords = [(chord, duration / tempo_multiplier) for chord, duration in self.chords]

    def set_adsr(self, attack=None, decay=None, sustain=None, release=None):
        # Update the ADSR parameters only if they are specified
        self.attack = attack if attack is not None else self.attack
        self.decay = decay if decay is not None else self.decay
        self.sustain = sustain if sustain is not None else self.sustain
        self.release = release if release is not None else self.release

        for _, env in self.osc_env_pairs.values():
            if attack is not None:
                env.setAttack(self.attack)
            if decay is not None:
                env.setDecay(self.decay)
            if sustain is not None:
                env.setSustain(self.sustain)
            if release is not None:
                env.setRelease(self.release)