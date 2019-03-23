const int ledpin=13; // ledpin and soundpin are not changed throughout the process 
const int soundpin=A2;
const int threshold=200; // sets threshold value for sound sensor
int vibr_Pin =3;
int LED_Pin = 13;
void setup() {
Serial.begin(9600);
pinMode(LED_Pin, OUTPUT);
pinMode(vibr_Pin, INPUT);
pinMode(soundpin,INPUT);
}
void loop() {
int soundsens=analogRead(soundpin); // reads analog data from sound sensor

Serial.println(soundsens);

long measurement =TP_init();
 
  //Serial.print(",");
  Serial.println(measurement);
 
}

long TP_init(){
  delay(10);
  long measurement=pulseIn (vibr_Pin, HIGH);  //wait for the pin to get HIGH and returns measurement
  return measurement;
}
