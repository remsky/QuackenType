"""
Dictionary of chords and their corresponding notes.
"""
from .notes import NOTES

# Define chords using the note names
CHORDS = {
    'C_major': (NOTES['C4'], NOTES['E4'], NOTES['G4']),
    'G_major': (NOTES['G4'], NOTES['B4'], NOTES['D5']),
    'A_minor': (NOTES['A4'], NOTES['C5'], NOTES['E5']),
    'E_minor': (NOTES['E4'], NOTES['G4'], NOTES['B4']),
    'D_major': (NOTES['D4'], NOTES['F#4'], NOTES['A4']),
    'B_minor': (NOTES['B4'], NOTES['D5'], NOTES['F#5']),
    'F_major': (NOTES['F4'], NOTES['A4'], NOTES['C5']),
    'B_flat_major': (NOTES['Bb4'], NOTES['D5'], NOTES['F5']),
    'E_flat_major': (NOTES['Eb4'], NOTES['G4'], NOTES['Bb4']),
    'A_flat_major': (NOTES['Ab4'], NOTES['C5'], NOTES['Eb5']),
    'D_flat_major': (NOTES['Db4'], NOTES['F4'], NOTES['Ab4']),
    'G_flat_major': (NOTES['Gb4'], NOTES['Bb4'], NOTES['Db5']),
    'F_minor': (NOTES['F4'], NOTES['Ab4'], NOTES['C5']),
    'B_flat_minor': (NOTES['Bb4'], NOTES['Db5'], NOTES['F5']),
    'E_flat_minor': (NOTES['Eb4'], NOTES['Gb4'], NOTES['Bb4']),
    'A_flat_minor': (NOTES['Ab4'], NOTES['B4'], NOTES['Eb5']),
    'D_flat_minor': (NOTES['Db4'], NOTES['E4'], NOTES['Ab4']),
    'G_flat_minor': (NOTES['Gb4'], NOTES['A4'], NOTES['Db5']),
    'D_minor': (NOTES['D4'], NOTES['F4'], NOTES['A4']),
    'Eb_major': (NOTES['Eb4'], NOTES['G4'], NOTES['Bb4']),
    'C_major7': (NOTES['C4'], NOTES['E4'], NOTES['G4'], NOTES['B4']),     # C major seventh chord
    'A_minor7': (NOTES['A4'], NOTES['C5'], NOTES['E5'], NOTES['G5']),    # A minor seventh chord
    'D_minor7': (NOTES['D4'], NOTES['F4'], NOTES['A4'], NOTES['C5']),    # D minor seventh chord
    'G7': (NOTES['G4'], NOTES['B4'], NOTES['D5'], NOTES['F5']),          # G dominant seventh chord
    'E_flat_major': (NOTES['Eb4'], NOTES['G4'], NOTES['Bb4']),           # E flat major chord
    'A_flat_minor': (NOTES['Ab4'], NOTES['Cb5'], NOTES['Eb5'])           # A flat minor chord (Cb is equivalent to B)
}
