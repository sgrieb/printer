const int ledPin = 13;
int n;

void setup() {
  // put your setup code here, to run once:

  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  n = 7;
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()) { 
    n = Serial.read() - '0';  
  }

  digitalWrite(ledPin, HIGH);
  delay(n*100);
  digitalWrite(ledPin, LOW);
  delay(n*100); 
}