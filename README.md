**AI-Powered Voice Recognition for Arduino LEDs**

Projenin dört aşaması var:

  1-Python üzerinden ses kayıt
  
  2-Python üzerinden ses dosyasını eğitimli model sayesinde okuma
  
  3-Python üzerinden okuduğumuz ses kaydına göre ardunioya veri göndermek
  
  4-Ardunio üzerinden gelen veriye göre RGB ledin bacaklarını aktifleştirmek
  
Bu projede Speech Recognition kütüphanesindeki vosk modeli sayesinde söylediğimiz kelimeyi yazıya çevirir. 

Vosk modelini internetsiz ortamda da kullanabileceiğimizden tercih ettim, kullanabilmek için ayrıca dosya olarak indirmeniz lazım 

The project consists of four stages:

  1-Recording audio using Python.
  
  2-Processing the recorded audio with a trained model in Python.
  
  3-Sending data to the Arduino based on the processed audio.
  
  4-Activating the RGB LED pins on the Arduino according to the received data.
  
In this project, we use the Vosk model from the Speech Recognition library to convert spoken words into text.

I chose the Vosk model because it can be used offline, but you need to download the necessary files separately to use it.
