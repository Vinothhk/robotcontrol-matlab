
#include <Servo.h>

Servo joint1;
Servo joint2;
int pos = 0;
void setup() {
  
  joint1.attach(7);
  joint2.attach(8);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) { 
      String A = Serial.readStringUntil('\n');
     
      int spaceIndex = A.indexOf(' ');
    
      String num1_str = A.substring(0, spaceIndex);
      String num2_str = A.substring(spaceIndex + 1);
    
      // Convert the extracted strings to integers
      int num1 = num1_str.toInt();
      int num2 = num2_str.toInt();
      Serial.print("DATA: ");
      Serial.print(num1);
      joint1.write(num1);  
      Serial.print(" ");
      Serial.println(num2);
      joint2.write(num2); 

  }
  
//    for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
//    // in steps of 1 degree
//    joint1.write(pos);              // tell servo to go to position in variable 'pos'
//    delay(15);                       // waits 15ms for the servo to reach the position
//  }
//  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
//    joint1.write(pos);              // tell servo to go to position in variable 'pos'
//    delay(15);                       // waits 15ms for the servo to reach the position
//  }
  }
