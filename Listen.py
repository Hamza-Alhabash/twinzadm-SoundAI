import speech_recognition as sr

class Listen:
    def __init__(self, phrase_threshold=0.4, noise_duration=0.5, phrase_time=3, language="en"):
        self.r = sr.Recognizer()
        self.phrase_threshold = phrase_threshold
        self.noise_duration = noise_duration
        self.phrase_time = phrase_time
        self.language = language
        
        self.r.phrase_threshold = self.phrase_threshold
        
    def set_phrase_threshold(self, phrase_threshold):
        self.phrase_threshold = phrase_threshold
        
    def get_phrase_threshold(self):
        return self.phrase_threshold
    
    def set_noise_duration(self, noise_duration):
        self.noise_duration = noise_duration
        
    def get_noise_duration(self):
        return self.noise_duration
    
    def set_phrase_time(self, phrase_time):
        self.phrase_time = phrase_time
    
    def get_phrase_time(self):
        return phrase_time
    
    def set_language(self, language):
        self.language = language
        
    def get_language(self):
        return language
    
    def listen(self):
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source, duration=self.noise_duration)
            audio = self.r.listen(source, phrase_time_limit=self.phrase_time)

            recognized_text = ''
            try:
                if 'ar' == self.language:
                    recognized_text = self.r.recognize_google(audio, language=self.language)
                elif 'en' == self.language:
                    recognized_text = self.r.recognize_google(audio, language=self.language)
            except sr.UnknownValueError:
                print("Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

        return recognized_text.lower()
