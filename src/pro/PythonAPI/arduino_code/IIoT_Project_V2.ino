#include <AFMotor.h> // Motor Controller Library


AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

#define echoPin 16 // attach pin D2 Arduino to pin Echo of HC-SR04
#define trigPin 17 //attach pin D3 Arduino to pin Trig of HC-SR04


int distance;
int min_distance;
int x= 0;
long t1;
long t2;
long duration; // variable for the duration of sound wave travel
int distanceU; // variable for the distance measurement


int ultrasonic()
{
  // Clears the trigPin condition
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin HIGH (ACTIVE) for 10 microseconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distanceU = duration * 0.034 / 2; // Speed of sound wave divided by 2 (go and back)
  // Displays the distance on the Serial Monitor
  //Serial.print("Distance: ");
  //Serial.print(distanceU);
  //Serial.println(" cm");

  return distanceU;
  
}



void moveForward() {
  motor1.setSpeed(200);
  motor2.setSpeed(200);
  motor3.setSpeed(200);
  motor4.setSpeed(200);
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
}
void moveBackward() {
  motor1.setSpeed(200);
  motor2.setSpeed(200);
  motor3.setSpeed(200);
  motor4.setSpeed(200);
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
}

void Stop() {
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
}

void setup() {
  Serial.begin(9600);
  min_distance = 5;

  // Ultrasonic setup
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed
  //Serial.println("Ultrasonic Sensor HC-SR04 Test"); // print some text in Serial Monitor
  //Serial.println("with Arduino UNO R3");

}

void loop() {
//t1 = millis();  
distance = ultrasonic();


  if (distance <= min_distance)
  {
    Stop();
    
    Serial.println(distance);
    //Serial.write('\n');
    //Serial.write("stop");
    //Serial.write('\n');
    //delay ();
    
  }
  else
  {
    moveForward();
    Serial.println(distance);
    //Serial.write('\n');
    //Serial.write("moving");
    //Serial.write('\n');
    //delay (3000);

  }
delay(1500);
//t2 = millis();


}
