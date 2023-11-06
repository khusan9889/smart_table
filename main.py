import speech_recognition as sr
import subprocess
import sounddevice as sd
import soundfile as sf
from gtts import gTTS

# import RPi.GPIO as GPIO
# from ultrasonic import *
from gpt import gpt_answer

# from dht import runs
from notifications import run

# from volume import increase_vol, decrease_vol
from where_is import where_is
from music import music_function
from fuzzywuzzy import fuzz

import re
import time


r = sr.Recognizer()
wake_word = "hey billy"


# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(11, GPIO.OUT)
# GPIO.output(11, 1)

# GPIO.setup(13, GPIO.OUT)
# GPIO.output(13, 1)

# GPIO.setup(15, GPIO.OUT)
# GPIO.output(15, 1)

# GPIO.setup(16, GPIO.OUT)
# GPIO.output(16, 1)


# GPIO.setup(18, GPIO.OUT)
# GPIO.output(18, 1)

# GPIO.setup(22, GPIO.OUT)
# GPIO.output(22, 1)


# Функция Текст-в-речь
def speak(text):
    tts = gTTS(text=text, lang="en")
    tts.save("output.mp3")
    subprocess.run(["mpg321", "output.mp3"])


def play_peep_sound():
    peep_sound_path = "peep.wav"
    peep_data, sample_rate = sf.read(peep_sound_path)
    sd.play(peep_data, sample_rate)
    sd.wait()


# Initialize the current_distance variable with a default value
current_distance = 0


def up_table(height_cm):
    global current_distance  # Use the global variable to update current_distance
    height_cm = int(height_cm)
    print("Increase to:", height_cm)

    # Calculate the target height
    target_height = current_distance + height_cm
    print(f"Raising table to {target_height} cm")

    # Check if the target height is less than the current height
    if target_height < current_distance:
        print("Error: Target height is lower than the current height.")
        return

    # Calculate the height difference
    height_difference = target_height - current_distance

    # Calculate the time required to raise the table to the target height
    time_to_raise_factor = 0.5  # Adjust this factor as needed
    time_to_raise = height_difference * time_to_raise_factor

    # Raise the table
    # GPIO.output(11, 0)
    time.sleep(time_to_raise)
    # GPIO.output(11, 1)
    print(f"Table is raised to {target_height} cm")


def down_table(height_cm):
    global current_distance
    height_cm = int(height_cm)
    print("Decrease by:", height_cm)

    # Calculate the target height
    target_height = current_distance - height_cm
    print(f"Lowering table to {target_height} cm")

    # Check if the target height is greater than the current height
    # if target_height > current_distance:
    # print("Error: Target height is higher than the current height.")
    # return

    # Calculate the height difference
    height_difference = target_height - current_distance

    # Calculate the time required to lower the table to the target height
    time_to_lower_factor = 0.5  # Adjust this factor as needed
    time_to_lower = height_difference * time_to_lower_factor

    # GPIO.output(13, 0)
    time.sleep(time_to_lower)
    # GPIO.output(13, 1)
    current_distance = target_height  # Update the current distance
    print(f"Table is lowered to {target_height} cm")


def bind_button():
    print("Binding button")
    # press save button and off
    # GPIO.output(15, 0)
    # GPIO.output(15, 1)


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="en-US").lower()
            print("You said:")
            print(text)
            return text
        except sr.UnknownValueError:
            pass

        return ""


if __name__ == "__main__":
    remember_mode = False
    play_peep_sound()
    wake_word_detected = False

    while True:
        try:
            result = listen()

            if wake_word in result:
                print("Wake word detected")
                wake_word_detected = True
            elif wake_word_detected:

                if result:
                    print("You said:")
                    print(result)
                    print(type(result))

                    if "up" in result.lower():
                        print("Table mode activated.")
                        # Split the result into words
                        words = result.lower().split()
                        for i, word in enumerate(words):
                            if word == "up" and i + 1 < len(words):
                                try:
                                    height = int(words[i + 1])
                                    # Calculate the target height
                                    target_height = current_distance + height
                                    up_table(target_height)
                                    print(f"Table is raised for {height} cm")
                                    break
                                except ValueError:
                                    print("Invalid height specified")

                    if "release" in result.lower():
                        print("Table mode activated.")
                        # Split the result into words
                        words = result.lower().split()
                        for i, word in enumerate(words):
                            if word == "release" and i + 1 < len(words):
                                try:
                                    height = int(words[i + 1])
                                    # Calculate the target height
                                    target_height = current_distance - height
                                    down_table(target_height)
                                    print("release_table function is called")
                                    print(f"Table is released {height} cm")
                                    break
                                except ValueError:
                                    print("Invalid height specified")

                    if "exit" in result.lower() or "stop" in result.lower():
                        print("Exiting...")
                        break

                    if "set settings" in result.lower():
                        print(
                            "Set up mode activated. Choose which button to bind (A,B,B)"
                        )
                        bind_button()
                        print("To which button you want to bind?")
                        option = listen()
                        if option is not None:
                            option = option.lower()

                            if "first" in option:
                                print("binding to first button")
                                # switch on then off the GPIO of neccessary button to which we want to bind
                                # GPIO(16, 0)
                                # GPIO(16, 1)
                            if "second" in option:
                                print("binding to second button")
                                # switch on then off the GPIO of second button
                                # GPIO(13, 0)
                                # GPIO(13, 1)
                            if "third" in option:
                                print("binding to third button")
                                # switch on then off the GPIO of third button
                                # GPIO(14, 0)
                                # GPIO(14, 1)

                    # if "apply settings" in result.lower():
                    # print("Applying settings:")
                    # option = listen()
                    # if "first" in option:
                    # GPIO(12, 0)
                    # if "second" in option:
                    # GPIO(13, 0)
                    # if "third" in option:
                    # GPIO(14, 0)

                    if "switch on" in result.lower():
                        play_peep_sound()
                        # GPIO.output(18, 0)
                        print("lights are switched on")
                    elif "switch off" in result.lower():
                        play_peep_sound()
                        # GPIO.output(18, 1)
                        print("lights are switched off")
                    # elif "increase volume" in result.lower():
                    #     increase_vol()
                    # elif "decrease volume" in result.lower():
                    #     decrease_vol()

                    if "remember" in result.lower():
                        print("Remember mode activated.")
                        remember_mode = True
                        continue

                    print("remember_mode", remember_mode)

                    if remember_mode:
                        user_question = (
                            result  # Store the user's question for later use
                        )
                        print("You talked:")
                        print(result)
                        print(type(result))
                        remember_mode = (
                            False  # Disable help mode after capturing the question
                        )
                        run(message=result)

                    if "where is" in result.lower():
                        print("Notification mode activated.")
                        notification = where_is()
                        print("notification: ", notification)
                        speak(notification)
                        music_function()

                    if "help me" in result.lower():
                        print(
                            "Help mode activated. Please ask a question within 5 seconds."
                        )
                        help_mode = True
                        continue

                    # if "temperature" in result.lower():
                    #     temperature = runs()

                    # if help_mode:
                    #     user_question = result  # Store the user's question for later use
                    #     print("You asked:")
                    #     print(result)
                    #     # print(type(result))
                    #     help_mode = False  # Disable help mode after capturing the question
                    #     answer = gpt_answer(query=user_question)
                    #     speak(answer)
                    #     music_function()
        except KeyboardInterrupt:
            print("Exiting...")
            break
        except Exception as e:
            # Redirect ALSA error messages to /dev/null (suppress them)
            subprocess.run(["python3", "your_script.py"], stderr=subprocess.DEVNULL)
