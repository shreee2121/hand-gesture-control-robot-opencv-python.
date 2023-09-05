
#include <AFMotor.h>
int incomingData;
AF_DCMotor motor1(1);
AF_DCMotor motor2(2);
AF_DCMotor motor3(3);
AF_DCMotor motor4(4);

void setup(){
  Serial.begin(9600);

  motor1.setSpeed(80);
  motor2.setSpeed(80);
  motor3.setSpeed(80);
  motor4.setSpeed(80);
  
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
  
}

void loop() {
  if (Serial.available()>0){
    incomingData = Serial.read();
    if (incomingData == 'F'){
  
  motor1.run(BACKWARD);
  motor2.run(FORWARD);
  motor3.run(BACKWARD);
  motor4.run(BACKWARD);
  }
  if (incomingData == 'Q'){
  motor1.run(RELEASE);
  motor2.run(RELEASE);
  motor3.run(RELEASE);
  motor4.run(RELEASE);
  }
  if (incomingData == 'R'){
  motor1.run(FORWARD);
  motor2.run(BACKWARD);
  motor3.run(FORWARD);
  motor4.run(FORWARD);
  }
  if (incomingData == 'S'){
  motor1.run(FORWARD);
  motor2.run(FORWARD);
  motor3.run(BACKWARD);
  motor4.run(FORWARD);
}
if (incomingData == 'T'){
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  motor3.run(FORWARD);
  motor4.run(BACKWARD);
}
}
}