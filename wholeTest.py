import openai
import pyttsx3 
import speech_recognition as sr
import time

#initialize Openai API
openai.api_key = "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"
#initialize the text to speech engine
engine = pyttsx3.init()

def transcribe_audio_to_test(filename):
        recognizer = sr.Recognizer()
        with sr.AudioFile(filename)as sources:
                #print("Yes, say something please:")
                audio = recognizer.record(sources)
        try:
            return recognizer.recognize_google(audio)
        except:
               print("skipping unknown error") 


def generate_response(prompt):
       response = openai.Completion.create(
              engine = "text-davinci-003", #using text-davinci-003 egine
              prompt = prompt,
              max_tokens = 4000, #given max 4000 tokens to model
              n = 1,
              stop = None,
              temperature = 0.5,
       )
       return response ["choices"][0]["text"]

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
       while True:
              #Waith for user say "genius"
              print("Say 'Genius' to start recording your question")
              #transfer music to test
              with sr.Microphone() as source:
                     recognizer = sr.Recognizer()
                     audio = recognizer.listen(source)
                     try:
                        transcription = recognizer.recognize_google(audio)
                        if transcription.lower() == "genius":
                               #record audio
                               filename = "input.wav"
                               print("Say your question")
                               with sr.Microphone() as source:
                                      recognizer = sr.Recognizer()
                                      source.pause_threshold=1
                                      audio = recognizer.listen(source,phrase_time_limit=None,timeout=None)
                                      with open(filename,"wb")as f:
                                             f.write(audio.get_wav_data())

                                #transcript audio to text
                        text=transcribe_audio_to_test(filename)
                        if text:
                                     print(f"your said{text}")

                                     #generate the response
                                     response = generate_response(text)
                                     print(f"chatgpt3 say {response}")

                                     #read response using GPT3
                                     speak_text(response)
                     except Exception as e:
                            print("An error ocurred : {}".format(e))
if __name__=="__main__":
       main()
                               