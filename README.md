
<img alt="Harmony" src="https://github.com/user-attachments/assets/1996e914-5631-4db5-8bf5-89f736be1595" />

## Inspiration
Studies have shown that students who study music are more likely to excel academically due to the cognitive and emotional benefits music education provides. Learning an instrument enhances memory, concentration, and problem-solving skills, while also fostering emotional expression and self-discipline. These skills are transferable to other subjects, helping students perform better in areas like math, reading, and even social interactions. However, we noticed that despite the proven benefits of music education, there were few free and accessible apps on the market that catered specifically to elementary school students learning music. This gap inspired us to create Harmony, a web app designed to make piano lessons fun, interactive, and easy to follow for young learners, providing them with the tools they need to succeed academically and emotionally.

## What it does
Harmony takes a unique approach by breaking up complex pieces of music into smaller, more manageable sections, allowing young learners to focus on mastering one part at a time. To make learning even more accessible, the app plays the music at different speeds, enabling students to practice at a pace that suits their skill level and gradually increase the tempo as they improve. Additionally, Harmony visually shows finger positions on the keyboard, offering clear guidance on which keys to press for each note. Once students are ready, they can play the song themselves, and the app provides real-time feedback, helping them correct mistakes instantly and encouraging continuous improvement. This combination of gradual learning, visual cues, and immediate feedback helps students build confidence and achieve a greater understanding of music.

## How we built it
The front end was developed using HTML, CSS, and JavaScript, allowing us to create a visually appealing interface with smooth interactivity. We used modern JavaScript techniques to implement features like real-time feedback, audio playback at variable speeds, and interactive visual elements such as finger position guides on the keyboard. For the backend, we used Python to handle the more complex tasks, such as processing audio, managing user data, and delivering personalized content.


## Technical Process
The pipeline begins with Recording.py, which captures audio input and saves it as a .wav file. This functionality will later be integrated with a front-end button for seamless recording. The .wav file is processed by Reading.py, which transcribes the audio into a .txt file, aiming for accurate note detection and transcription.

To measure transcription accuracy, the project uses output from MIDI Code, which converts MIDI files into text-based sheet music representations. By comparing the outputs of Reading.py and Nessas MIDI Code, the system calculates the percentage correctness of the transcription. This comparison forms the basis of evaluating and improving transcription accuracy.

Future developments include converting .wav files directly to MIDI for streamlined comparisons, animating a virtual piano with Pygame to visualize notes and play synthesized sound, and leveraging machine learning models to enhance note detection. The project also plans to connect the back end with a front-end interface using Flask, enabling users to interact with the system effortlessly.

This pipeline offers a foundation for expanding the scope of musical transcription, accuracy evaluation, and visualization. It sets the groundwork for more advanced features like integrating ML-based note detection and automating sheet music transcription.

![Screenshot 2024-11-10 035045](https://github.com/user-attachments/assets/c5db6760-64fe-4c8a-8653-a1821e9921e6)

## Challenges we ran into
One of the major hurdles was accurately transcribing audio input into readable note data. Initially, we attempted live detection of notes for real-time feedback, but this proved too difficult given our technical limitations. We also explored converting WAV files into MIDI format, which would allow for direct comparisons with sheet music, but this process is still in progress. Additionally, integrating the backend and frontend posed its own set of challenges, as we needed to synchronize Python scripts (like the ones used for audio transcription and note comparison) with the JavaScript-driven user interface.

## Accomplishments that we're proud of
One of our biggest accomplishments is the simplified user experience we’ve designed, which ensures that the app is intuitive and not overstimulating for elementary school students. We focused on creating an interface that is visually clean, easy to navigate, and engaging for kids, without overwhelming them with too many options or distractions. The design incorporates bright, inviting colors and playful elements, making the learning process both fun and effective.

## What's next for Harmony
One of our main goals is to improve the real-time feedback feature, making it more accurate and responsive to students’ performances. We’re also working on developing a parser that will automatically break down sheet music into smaller sections, and cut the audio accordingly. This will allow us to create lesson plans for songs that are longer. Additionally, we plan to introduce user authentication, which will enable us to tailor the learning experience to each student’s unique needs and progress. By tracking individual performance and preferences, we can offer personalized recommendations and a more adaptive learning journey. Lastly, we want to start adding difficult pieces to cater to a variety of different skill levels.

# View the Front End:  [cs.wellesley.edu](https://cs.wellesley.edu/~ek118/cs204/harmony/home.html)



