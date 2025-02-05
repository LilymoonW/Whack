import numpy as np
import librosa
import matplotlib.pyplot as plt

piano_note_freqs = {
    "A0": 27.5, "A#0": 29.14, "B0": 30.87,
    "C1": 32.70, "C#1": 34.65, "D1": 36.71, "D#1": 38.89, "E1": 41.20, "F1": 43.65, "F#1": 46.25, "G1": 49.00, "G#1": 51.91,
    "A1": 55.0, "A#1": 58.27, "B1": 61.74,
    "C2": 65.41, "C#2": 69.30, "D2": 73.42, "D#2": 77.78, "E2": 82.41, "F2": 87.31, "F#2": 92.50, "G2": 98.00, "G#2": 103.83,
    "A2": 110.0, "A#2": 116.54, "B2": 123.47,
    "C3": 130.81, "C#3": 138.59, "D3": 146.83, "D#3": 155.56, "E3": 164.81, "F3": 174.61, "F#3": 185.00, "G3": 196.00, "G#3": 207.65,
    "A3": 220.0, "A#3": 233.08, "B3": 246.94,
    "C4": 261.63, "C#4": 277.18, "D4": 293.66, "D#4": 311.13, "E4": 329.63, "F4": 349.23, "F#4": 369.99, "G4": 392.00, "G#4": 415.30,
    "A4": 440.0, "A#4": 466.16, "B4": 493.88,
    "C5": 523.25, "C#5": 554.37, "D5": 587.33, "D#5": 622.25, "E5": 659.25, "F5": 698.46, "F#5": 739.99, "G5": 783.99, "G#5": 830.61,
    "A5": 880.0, "A#5": 932.33, "B5": 987.77,
    "C6": 1046.50, "C#6": 1108.73, "D6": 1174.66, "D#6": 1244.51, "E6": 1318.51, "F6": 1396.91, "F#6": 1479.98, "G6": 1567.98, "G#6": 1661.22,
    "A6": 1760.0, "A#6": 1864.66, "B6": 1975.53,
    "C7": 2093.00, "C#7": 2217.46, "D7": 2349.32, "D#7": 2489.02, "E7": 2637.02, "F7": 2793.83, "F#7": 2959.96, "G7": 3135.96, "G#7": 3322.44,
    "A7": 3520.0, "A#7": 3729.31, "B7": 3951.07,
    "C8": 4186.01
}

def detect_piano_notes_from_fft(wav_file, expected_notes):
    # Load audio file
    y, sr = librosa.load(wav_file, sr=None)

    # Calculate the number of samples per block
    samples_per_block = len(y) // expected_notes

    detected_notes = []
    for i in range(expected_notes):
        start = i * samples_per_block
        end = (i + 1) * samples_per_block

        # Extract the block of audio
        block = y[start:end]

        # Apply window function
        window = np.hanning(len(block))
        block_windowed = block * window

        # Perform FFT on the block
        fft_block = np.fft.rfft(block_windowed)
        fft_freq = np.fft.rfftfreq(len(block), 1/sr)

        # Find the index of the maximum magnitude in the FFT
        max_index = np.argmax(np.abs(fft_block))
        peak_freq = fft_freq[max_index]

        # Find the closest note
        closest_note = min(piano_note_freqs.items(), key=lambda x: abs(x[1] - peak_freq))[0]
        detected_notes.append((closest_note, peak_freq))

    return detected_notes, y, sr

def plot_fft_and_piano_notes(wav_file, expected_notes):
    detected_notes, y, sr = detect_piano_notes_from_fft(wav_file, expected_notes)

    # Plot the waveform
    plt.figure(figsize=(15, 10))
    plt.subplot(2, 1, 1)
    librosa.display.waveshow(y, sr=sr)
    plt.title("Waveform")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")

    # Plot the detected notes
    plt.subplot(2, 1, 2)
    times = np.linspace(0, len(y)/sr, len(detected_notes))
    frequencies = [freq for _, freq in detected_notes]
    plt.scatter(times, frequencies)
    plt.title(f"Detected Piano Notes (Expected Notes: {expected_notes})")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.yscale('log')
    plt.ylim(20, 5000)

    # Annotate the plot with note names
    for i, (note, freq) in enumerate(detected_notes):
        plt.annotate(note, (times[i], freq), xytext=(5, 5),
                    textcoords='offset points', fontsize=8,
                    bbox=dict(boxstyle="round", fc="w", ec="0.5", alpha=0.8))

    # Display detected piano notes
    print(f"Detected Piano Notes:")
    for i, (note, freq) in enumerate(detected_notes):
        print(f"Block {i+1}: {note} ({freq:.2f} Hz)")

    plt.tight_layout()
    plt.show()

# Example usage
wav_file = 'ttls.wav'  # Replace with your file path
plot_fft_and_piano_notes(wav_file, expected_notes=46)