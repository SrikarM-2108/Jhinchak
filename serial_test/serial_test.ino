int output;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    
    output = (Serial.read()- '0');
    }

  Serial.print(output);
  delay(1000);  
}
