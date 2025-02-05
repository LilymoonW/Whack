import librosa
import numpy as np
from midiutil import MIDIFile

def wav_to_midi(input_wav, output_midi, threshold=0.1, min_duration=0.1):
    # Load the WAV file
    y, sr = librosa.load(input_wav)

    # Perform onset detection
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)

    # Perform pitch detection
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

    # Create a new MIDI file with 1 track
    midi = MIDIFile(1)
    midi.addTempo(0, 0, 120)  # Track 0, time 0, tempo 120 BPM

    # Process the detected pitches and onsets
    for i in range(len(onset_times) - 1):
        start_time = onset_times[i]
        end_time = onset_times[i + 1]
        duration = end_time - start_time

        if duration < min_duration:
            continue

        # Find the pitch for this onset
        start_frame = librosa.time_to_frames(start_time, sr=sr)
        pitch_index = magnitudes[:, start_frame].argmax()
        pitch = pitches[pitch_index, start_frame]

        if pitch > 0 and magnitudes[pitch_index, start_frame] > threshold:
            # Convert frequency to MIDI note number
            midi_note = int(round(librosa.hz_to_midi(pitch)))
            
            # Add the note to the MIDI file
            midi.addNote(0, 0, midi_note, start_time, duration, 100)

    # Write the MIDI file
    with open(output_midi, "wb") as output_file:
        midi.writeFile(output_file)

# Usage
wav_to_midi('ttls.wav', 'output.mid')