#define B 3
#define G 2
#define R 4
#define CONTROL 13

void setup() {
  /* Bu kısımda seri iletişimi aktif hale getirdim 9600 bant genişliğiyle
  Sonrasında RGB ledin bacaklarının bacaklarını R G B olarak ayırıp sırasıyla 4 2 3 pinlerine bağladım ve output olarak ayarldım*/
  Serial.begin(9600);
  pinMode(R,OUTPUT);
  pinMode(B,OUTPUT);
  pinMode(G,OUTPUT);
  pinMode(CONTROL,OUTPUT);
}

void loop() {
  /* Bu kısımda seri iletişim ile char değeri aldım sonrasında o değerden 0'ın char değerini çıkardım
  Sonrasında gelen değere göre sırasıyla hangi renk yanacağına göre ledlerin RGB bacaklarına güç verdim */
  
  if(Serial.available()){
    digitalWrite(CONTROL,0);
    int mode = Serial.read() - '0';
    Serial.println(mode);
    switch(mode){
        case 1:
        analogWrite(B,0);
        analogWrite(G,129);
        analogWrite(R,0);
        
        break;
        case 2:
        analogWrite(R,128);
        analogWrite(G,0);
        analogWrite(B,0);
        break;
        case 3:
        analogWrite(B,128);
        analogWrite(G,0);
        analogWrite(R,0);;
        break;
        case 4:
        analogWrite(B,0);
        analogWrite(G,128);
        analogWrite(R,128);
        break;
        case 5:
        analogWrite(B,128);
        analogWrite(G,128);
        analogWrite(R,0);
        break;
        case 6:
        analogWrite(B,128);
        analogWrite(G,0);
        analogWrite(R,128);
        break;
        case 7:
        analogWrite(B,128);
        analogWrite(G,128);
        analogWrite(R,128);
        break;
        case 8:
        analogWrite(B,0);
        analogWrite(G,0);
        analogWrite(R,0);
        break;
        case 9:
        analogWrite(B,0);
        analogWrite(G,0);
        analogWrite(R,0);
        return;
        break;
        default:
        digitalWrite(CONTROL,1);
        analogWrite(B,0);
        analogWrite(G,0);
        analogWrite(R,0);
    }    
    delay(100);
  }}
