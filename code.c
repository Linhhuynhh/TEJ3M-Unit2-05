// C code
// Created by: Linh Huynh
// Created on: Mar 2025
// This program controls a servo motor

#include <Servo.h>

Servo servoNumber1;

void setup() {
  // setup servo pins
  servoNumber1.attach(8);
  servoNumber1.write(0);
}

void loop() {
  // put your main code here, to run repeatedly
  servoNumber1.write(180);
  delay(1000);
  servoNumber1.write(0);
  delay(1000);
}
