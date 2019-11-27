
"""
install speechrecognition , pyaudio and portaudio to run
"""
import speech_recognition as sr

r = sr.Recognizer()


def get_from_microphone():
	with sr.Microphone() as source:
		print("Say Somthing....")
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source, timeout=10)

	return audio


if __name__ == '__main__':
	
	audio = get_from_microphone()

	print('Wait.....')

	try:
		text = r.recognize_google(audio)
		print('You said: ' +  text)
	except sr.UnknownValueError as e:
		print("Couldn't Recognize the Audio")
	except sr.RequestError as e:
		print("Couldn't request results from Google Speech Recognition")

