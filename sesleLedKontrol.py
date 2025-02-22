from pickle import FALSE
import serial
import speech_recognition as sr #Gerekli modeli secip eklemek lazım ben internetsiz calissin diye vosk modelini tercih ettim
import pyaudio
import wave
import re

def extract_value(text):#vosk modelinde output sadece söylenen kelime değil ondan dolayı o desene ozel kelime ayıklayıcı kullandım
    # Deseni belirliyoruz (örnek olarak '{ 'text' : 'değer' }' şeklinde bir yapı kullanıyoruz)
    pattern = r" \"text\"\s*:\s*\"([^']*)\""
    match = re.search(pattern, text)
    
    if match:
        return match.group(1)  # Yakalanan değeri döndür
    return "olmadı"




FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 2
OUTPUT_FILENAME = "output.wav"

audio = pyaudio.PyAudio()

ser = serial.Serial(port = 'COM7',baudrate=9600)
x=True
while x:
    print(ser.read_all())
    y =input("Ses kaydına baslamak icin herhangi bir tusa basınız: ")
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, 
                        frames_per_buffer=CHUNK) 
    print("Ses kaydediliyor...")
    
    frames = [] #Ses datası buna ekleniyor
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream() 
    stream.close()
    
    
    with wave.open(OUTPUT_FILENAME, 'wb') as wf: #Ses datası dosyaya dönüşüyor
        wf.setnchannels(CHANNELS) 
        wf.setsampwidth(audio.get_sample_size(FORMAT)) 
        wf.setframerate(RATE) 
        wf.writeframes(b''.join(frames))
        
    AudioFile=OUTPUT_FILENAME
    recrognizer = sr.Recognizer()
    with sr.AudioFile(OUTPUT_FILENAME) as source:
        audio_data = recrognizer.record(source) 
        try:
            text = recrognizer.recognize_vosk(audio_data=audio_data,language='tr') # ses dosyası okunuyor ve çıktı alınıyor
            
            print(text) # normal çıktısı
        
            text = extract_value(text) # istediğimiz çıktıya döndürüyoruz
            if text=="yeşil": #hangi kelime olduğunu anlamak için if else yapısını tercih ettim
                ser.write(b'1')

            elif  (text == "kırmızı"):
                ser.write(b'2')

            elif text == "mavi":
                ser.write(b'3')

            elif  (text == "sarı"):
                ser.write(b'4')

            elif text == "cam göbeği":
                ser.write(b'5')
            
            elif text == "magenta":
                ser.write(b'6')
                
            elif text == "beyaz":
                ser.write(b'7')

            elif text == "sön":
                ser.write(b'8')
                
            elif text == "kapat":
                ser.write(b'9')
                x=False;
            else:
                print("else "+ text)
                ser.write(b'10')
                
            print(text) #söylediğimiz kelime ne onu görebilme amacıyla
            
        except sr.UnknownValueError:#hata satırları olası hata durumları için
            print("kayıt okunamadı")
        except sr.RequestError:
            print("Servise erişilemedi")