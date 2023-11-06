from gtts import gTTS
import sounddevice as sd
import soundfile as sf



def speak(text):
    tts = gTTS(text=text, lang="en")
    tts.save("output.mp3")

def wake_up(text):
    tts = gTTS(text=text, lang="en")
    tts.save("wake_up_message.mp3")
def play_wake_up_sound():
    wake_up_sound_path = "wake_up_message.mp3"
    wake_up_data, sample_rate = sf.read(wake_up_sound_path)
    sd.play(wake_up_data, sample_rate)
    sd.wait()
    # subprocess.run(["mpg321", wake_up_sound_path])

def play_peep_sound():
    peep_sound_path = "peep.wav"
    peep_data, sample_rate = sf.read(peep_sound_path)
    sd.play(peep_data, sample_rate)
    sd.wait()
