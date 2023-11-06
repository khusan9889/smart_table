import speech_recognition as sr
import subprocess
# import RPi.GPIO as GPIO
# from ultrasonic import *
from gpt import gpt_answer
from height import *
from sounds import *
# from dht import runs
from notifications import run
# from volume import increase_vol, decrease_vol
from where_is import where_is
from music import music_function
from fuzzywuzzy import fuzz
from music import *


r = sr.Recognizer()
wake_word = "billy" 


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



# Initialize the current_distance variable with a default value


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
                wake_up("Hello. How can i help you?")
                play_wake_up_sound()
            elif wake_word_detected:

                if result:
                    # print("You said:")
                    # print(result)
                    print(type(result))

                    if "up" in result.lower():
                        # GPIO.output(11, 0)
                        # GPIO.output(11, 1)
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
                                    wake_up(f"Table is raised for {height} cm")
                                    play_wake_up_sound()
                                    break
                                except ValueError:
                                    print("Invalid height specified")

                    if "release" in result.lower():
                        # GPIO.output(13, 0)
                        # GPIO.output(13, 1)
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
                                    wake_up(f"Table is released for {height} cm")
                                    play_wake_up_sound()
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
                                # GPIO(16, 0)
                                # GPIO(16, 1)
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
                        wake_up("lights are switched on")
                        play_wake_up_sound()
                    elif "switch off" in result.lower():
                        play_peep_sound()
                        # GPIO.output(18, 1)
                        print("lights are switched off")
                        wake_up("lights are switched off")
                        play_wake_up_sound()
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
