import speech_recognition as sr


listening = True
while listening:
	with sr.Microphone() as source:
		recognizer = sr.Recognizer()
		recognizer.adjust_for_ambient_noise(source)
		recognizer.dynamic_energy_treshold = 3000
		try:
			print("list")
			audio = recognizer.listen(source, timeout=5.0)
			text = recognizer.recognize_google(audio, language="en-US")
			print(text)
		except sr.UnknownValueError:			
			print("Речь не распознана")


