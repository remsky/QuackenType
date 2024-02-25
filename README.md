# QuackenType: Dynamic Music Coding Environment

Welcome to QuackenType, a unique Python-based coding environment that dynamically adjusts ambient music in reaction to your coding activity. Enjoy an immersive and responsive coding experience that harmonizes your programming with melody.

## Features

- **Dynamic Music Adjustment**: 
  - Adjusts ambient music based on your coding metrics.
  - Changes in melody, tempo, ADSR (Attack, Decay, Sustain, Release) settings, and pitch occur in real-time.

- **Intuitive Interface**:
  - Automatic syntax highlighting (Python basics only)
  - User-friendly interface for coding and music interaction.
  - Developed using Tkinter for ease of use.

## How It Works

The application uses coding metrics to adjust music:

- **Ambient Melody**:
  - *Instantaneous Words Per Minute (WPM)*: Modifies the melody's tempo based on typing speed.
  - *Average WPM*: Alters the melody's ADSR settings, with attack time reflecting average typing speed.

- **SimpleTune Melody**:
  - *Function Definition Count*: Changes the melody's pitch correlating to the number of function definitions.

## Setup

1. Clone the repository.
2. Install dependencies, including Tkinter and Pygments.
3. Run `app.py` to start the application.

## Dependencies

- Python 3.x
- Tkinter
- Pygments (for syntax highlighting)
- Pyo (for simple tone generation)

## Conclusion

QuackenType offers a novel coding experience, aiming to intertwine your programming style with ambient music to keep you in the flow
