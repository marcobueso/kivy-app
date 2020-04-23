//byte ipins[] = {A0, A1, A2, A3, A4, A5}; // Analog inputs, ys, cols
//byte opins[] = {0, 1, 2, 3, 4, 5}; // Digital outputs, xs, rows
byte ipins[] = {A0}; // Analog inputs, ys, cols
byte opins[] = { 2}; // Digital outputs, xs, rows

int xs = sizeof(opins);
int ys = sizeof(ipins);
int matrix[1][1] = {{0}};
int stopTest = false;
int sensorCount = 1;
int loopRun = 0;
String sensor = "";
int fullCycles = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(4, OUTPUT);
}

void loop() {
  while (Serial.available()> 0) {
    int a = Serial.read();
    if (isDigit(a)) {
      // convert the incoming byte to a char and add it to the string:
      sensor += (char)a;
      //Serial.println((char)a);
    }
    // if you get a newline, print the string, then the string's value:
    if (a == '\n') {
      if (sensor.toInt() > fullCycles) {
        Serial.println(random(50,200));
      }
      else {
        Serial.println(800);
      }

      // clear the string for new input:
      sensor = "";
    }
    if ( a == 'o') { // LED turn on
      digitalWrite(4, HIGH);
      Serial.read();
    }
    else if (a == 's') {
      Serial.read();
      Serial.read();
      return;
    }
//  }
//    if ( a == 'o') { // LED turn on
//      digitalWrite(4, HIGH);
//      Serial.read();
//    }
//    else if (a == 's') {
//      Serial.read();
//      Serial.read();
//      return;
//    }
//    else { // Sensor value request
//      Serial.print("Number entered.....");
//      Serial.print(Serial.available());
//      while (Serial.available()) {
//        sensor += char(a);
//        int inChar = Serial.read();
//        if (isDigit(inChar)) {
//          // convert the incoming byte to a char and add it to the string:
//          sensor += (char)inChar;
//        }
//        if (inChar == '\n') {
//          Serial.print("Value:");
//          Serial.println(sensor.toInt());
//          Serial.print("String: ");
//          Serial.println(sensor);
//          // clear the string for new input:
//          sensor = "";
//        }
//      }
//      
//      if (sensor.toInt() > fullCycles) {
//         //Serial.println(random(0,200));
//      }
//      else{
//        //Serial.println(800);
//      }
      loopRun++;
    }
  
  if (loopRun == 61) { loopRun = 0; fullCycles++;}
} 
//      for (int x=0; x<62; x++) {
//        for (int y=0; y<62; y++) {
//          int value = 800;
//          if (x < y) {
//            value = random(300);
//          }
//          if (x < y-15) {
//            value = 10;
//          }
//          Serial.println(value); 
//        }
//        if(Serial.available()){ // check at end of loop to see if another byte was received
//          return;
//        }
//      }
//    }
//  }
//}

//  // put your main code here, to run repeatedly:
//  for (int x=0; x<62; x++) {
//    for (int y=0; y<62; y++) {
//      int value = 800;
//      while(Serial.available()==0) {}; // wait for 1 keypress
//      while(Serial.available() > 0) {
//        if( Serial.read() == '0'){
//          return;
//        }
//      }
//      if (x < y) {
//        value = random(300);
//      }
//      if (x < y-15) {
//        value = 10;
//      }
//      Serial.println(value); 
//    }
//  }
//}
