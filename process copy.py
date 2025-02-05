import subprocess
import pretty_midi as pm

# Function to run terminal library (audio-to-midi)
def run_terminal_library(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return e.stderr

# Process function to convert audio to MIDI
def process(wvName):
    # Ensure the audio-to-midi tool is installed and available
    command = f"audio-to-midi {wvName} -b 120 -t 30 -o output.mid"
    run_terminal_library(command)
    return "output.mid"  # Return the output MIDI file

# Function to extract and compare MIDI files
def extract(wvName, ansName):
    pm1 = pm.PrettyMIDI(midi_file=wvName)
    pm2 = pm.PrettyMIDI(midi_file=ansName)
    
    # Estimate tempos
    temp1 = pm1.estimate_tempo()
    temp2 = pm2.estimate_tempo()
    
    # Get the piano roll representation (time vs pitch)
    notes = pm1.get_piano_roll()
    notesAns = pm2.get_piano_roll()

    # Compare note positions and pitches
    correct = True

    for time, pitches in enumerate(notes):
        for velocity, pitch in enumerate(pitches):
            midiNotes = [time, velocity, pitch]
            
            found_match = False
            for time_ans, pitches_ans in enumerate(notesAns):
                for velocity_ans, pitch_ans in enumerate(pitches_ans):
                    midiNotesAns = [time_ans, velocity_ans, pitch_ans]
                    
                    # Time comparison (based on tempo)
                    if abs(midiNotes[0] / temp1 - midiNotesAns[0] / temp2) > 0.1:  # Adjust tolerance
                        correct = False
                        break
                    
                    # Pitch comparison (with a slight tolerance)
                    if abs(midiNotes[2] - midiNotesAns[2]) > 2:  # Allow small tolerance
                        correct = False
                        break

            if not found_match:
                correct = False
                break

    return correct

# Example usage
class Process():
    # File names of the recorded audio and answer MIDI
    wvName = "ttls.wav"  # Path to your audio file
    ansName = "Twinkle_Twinkle_Little_Star.mid"  # Path to the answer MIDI file

    # Convert audio to MIDI
    output_midi = process(wvName)

    # Compare the converted MIDI with the reference MIDI
    is_correct = extract(output_midi, ansName)

    # Print the result
    print(f"Is the conversion correct? {is_correct}")
