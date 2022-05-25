#include <Servo.h>

//defining Servos

#include <dht.h>

//defining Humidity Sensor

String data;
double data1;

Servo servo;
int servo1Low = 0;
int servo1High = 90;


dht DHT;
#define DHT11_PIN 5


int PIR = 2;
int led = 7;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  
  servo.attach(10);

  servo.write(0);

  delay(500);

  pinMode(PIR,INPUT);

  pinMode(led,OUTPUT);

   
  delay(500);

}

void loop() {
  // put your main code here, to run repeatedly:

  int chk = DHT.read11(DHT11_PIN);

  float temperature = DHT.temperature;

  float humidity = DHT.humidity;

  int sensorValue = analogRead(A1);

  if(Serial.available() > 0)//From RPi to Arduino
  {                                 
    data = (Serial.readStringUntil('\n'));
    Serial.println("Data from Arduino: "+data);
  }

  data1 = data.toDouble();
  
  Serial.println(sensorValue);
  
  Serial.println(temperature);
  //if(data1) {
    //Serial.println("Data from Web: " +data1);
  //}
  
  if(temperature > 30.00)
  {
   data1 = data1 + (0.15*data1);
    }

  else if(temperature > 35.00)
  {
     data1 = data1 + (0.2*data1);
    }

  else
  {
      data1 = data1;
    }
  

  if(data1 > sensorValue)
  {
    servo.write(90);
    Serial.println("Closing Valve");
    }

  else 
  {
    servo.write(0);
    Serial.println("Opening Valve");
    }

  if(digitalRead(PIR)== HIGH)
  {
    digitalWrite(7,HIGH);
    Serial.println("LED => ON");
    delay(2000);
    }  

  else 
  {
    digitalWrite(7,LOW);
    Serial.println("LED => OFF");
    delay(2000);
    }  

}
