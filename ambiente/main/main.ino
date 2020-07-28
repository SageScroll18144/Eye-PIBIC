#define LDR A0

const int trig = 8;
const int echo = 9; 

void setup() {
  Serial.begin(9600);

}

void loop() {
  Serial.print(read_ldr());
  Serial.print("% ");
  Serial.print(ultrassonicRead());
  Serial.println("cm"); 

}
