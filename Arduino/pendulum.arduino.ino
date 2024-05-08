#include <Arduino.h>
const int potentiometerPin = A0; // Analog pin for potentiometer
int potentiometerValue;

void setup() {
  Serial.begin(9600); // Initialize serial communication
}

void loop() {
  potentiometerValue = analogRead(potentiometerPin); // Read potentiometer value
  Serial.println(potentiometerValue); // Send data to Python
  delay(100); // Adjust as needed
}
