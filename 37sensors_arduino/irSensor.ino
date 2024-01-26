int irPin=A0;
//int irPin=13;
void setup() {
  pinMode(irPin, INPUT);
  Serial.begin(9600);
}

void loop() {
int irValue=analogRead(irPin);
//int irValue=digitalRead(irPin);
Serial.print("irValue= ");
Serial.println(irValue);
delay(500);
 
}
