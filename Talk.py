import pyttsx3

class Talk:
    def __init__(self, speed_rate=115, volume=1.0, voice_gender=0):
        self.voice = pyttsx3.init()
        self.voices = self.voice.getProperty('voices')
        self.speed_rate = speed_rate
        self.volume = volume
        self.voice_gender = voice_gender
        
        self.voice.setProperty('rate', speed_rate)
        self.voice.setProperty('volume', volume)
        self.voice.setProperty('voice', self.voices[voice_gender].id)
        
    def set_speed_rate(self, speed_rate):
        self.speed_rate = speed_rate
        self.voice.setProperty('rate', speed_rate)
    
    def get_speed_rate(self):
        return self.speed_rate
    
    def set_volume(self, volume):
        self.volume = volume
        self.voice.setProperty('volume', volume)
        
    def get_volume(self):
        return self.volume
    
    def set_voice_gender(self, voice_gender):
        self.voice_gender = voice_gender
        self.voice.setProperty('voice', self.voices[voice_gender].id)
        
    def get_voice_gender(self):
        if(self.voice_gender == 0):
            return "[0] Male"
        else:
            return "[1] Female"
        
    def say(self, text):
        self.voice.say(text)
        self.voice.runAndWait()