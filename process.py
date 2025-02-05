import pyaudio as pya
import subprocess
import pretty_midi as pm

def run_terminal_library(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return e.stderr

# make sure to install the pypi audio to midi library 

#literally just fucking runs the library but lowk dont think this would work 
# psuedocode/instructions for when you want to change it based on how the input works
def process(wvName):
    #wf = wave.open(wvName)
    #p = pya.PyAudio()
    #stream = pya.Audio
    
    # recorded file should be called Recorded.wav
    # change the bpm based on the real bpm of which the piece should be played (this might be bad bc it theres no way a child would play in time)
    #-t is the time span of the audio in ms  (FFTs shit)
    command = f"audio-to-midi {wvName} -b 120 -t 30 -o output.mid"
    run_terminal_library(command)
    return "output.mid"

    # should save to a file called output.mid, use ./output.mid to find it

# file names of the played and the answer
#returns if it is corect or not in boolean 
def extract(wvName, ansName):
    pm1 = pm.PrettyMIDI(midi_file=wvName)
    pm2 = pm.PrettyMIDI(midi_file=ansName)
    temp1 = pm1.estimate_tempo()
    temp2 = pm2.estimate_tempo()
    
    #extract the note pitches
    #end1 = pm1.get_end_time()
    #end2 = pm2.get_end_time()
    notes = pm1.get_piano_roll()#returns a numpy array of the notes
    notesAns = pm2.get_piano_roll()
    #for each note compare
    correct = True

#    for i in notes: 
#        for j in notes1:
#            if i.get_duration() < j.get_duration()-50 or i.get_duration() > j.get_duration()+50: # it think the type i s piano roll, but not sure if it should be a pretty midi Note 
#                correct = False
#            if i.get_pitch
    midiNotes = []
    midiNotesAns =[]
    for time, pitches in enumerate(notes):
        for velocity, pitch in enumerate(pitches):
            midiNotes.append([time, velocity, pitch])

    for time, pitches in enumerate(notes):
        for velocity, pitch in enumerate(pitches):
            midiNotesAns.append([time, velocity, pitch])
    for played in midiNotes:
        for ans in midiNotesAns:
            #check time/duration
            #duration is relative to the tempo that was estimated by pretty midi or one second 
            if (played[0])/temp1 < (ans[0]-1900)/temp2 and (played[0])/temp1> (ans[0]+1900)/temp2: #it is in ticks not seconds i think 1 second is 96*120/60 ticks so 11420/60 = 1900 (this could be entirely wrong i used my mental math)
                correct = False
            #pitch
            if (played[1] == (ans[1]-2)) and (played[0]> (ans[0]+2)):
                correct = False
            #i hjave no idea waht the fuck velocity is, it might be frequency so maybe you can use
    
    return correct

class Process():
    # Example of usage
    wvName = "ttls.wav"  # Path to your audio file
    ansName = "Twinkle_Twinkle_Little_Star.mid"  # Path to the answer MIDI file

    # Convert audio to MIDI
    output_midi = process(wvName)

    # Compare the converted MIDI with the reference MIDI
    is_correct = extract(output_midi, ansName)

    # Print the result
    print(f"Is the conversion correct? {is_correct}")
        