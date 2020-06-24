import os
from pydub import AudioSegment

path = "PATH TO AUDIO FILES DIRECTORY"

#Change working directory
os.chdir(path)
audio_files = os.listdir()
import speech_recognition as sr
r = sr.Recognizer()
counter=00000
# You dont need the number of files in the folder, just iterate over them directly using:
for file in audio_files:
    counter+=1
    #spliting the file into the name and the extension
    name, ext = os.path.splitext(file)
    if ext == ".wav":
        # files                                                                         
        src = name+".wav"
        dst = str(counter)+".wav"

        # use from_wav or from_mp3 according to the files that you have                                     
        sound = AudioSegment.from_wav(src)
        sound.export(dst, format="wav")
        hellow=sr.AudioFile(str(counter)+".wav")
        with hellow as source:
            audio = r.record(source)
        try:
            s = r.recognize_google(audio)

            tran = str(counter)+ "\t" + s+ ""
            print(tran)
        except Exception as e:
            # print("Exception: "+str(e))
            pass

