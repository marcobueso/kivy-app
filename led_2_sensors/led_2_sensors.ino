//#include <SoftwareSerial.h> // remove the inverted commas after you copy the code to the IDE
//SoftwareSerial BT(10, 11); 
// creates a "virtual" serial port/UART
// connect BT module TX to D10
// connect BT module RX to D11
// connect BT Vcc to 5V, GND to GND
void setup()  
{
  // set digital pin to control as an output
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(4, OUTPUT);
  // set the data rate for the SoftwareSerial port
  Serial.begin(9600);
  // Send test message to other device
  Serial.println("Hello from Arduino");
}
char a; // stores incoming character from other device
void loop() 
{
  if (Serial.available())
  // if text arrived in from BT serial...
  {
    a=(Serial.read());
    if (a=='1')
    {
      digitalWrite(4, HIGH);
      digitalWrite(LED_BUILTIN, HIGH);
      delay(500);
      digitalWrite(LED_BUILTIN, LOW);
      delay(500);
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println("LED on");
    }
    if (a=='2')
    {
      digitalWrite(4, LOW);
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("LED off");
    }
    if (a=='?')
    {
      Serial.println("Send '1' to turn LED on");
      Serial.println("Send '2' to turn LED on");
    }   
    // you can add more "if" statements with other characters to add more commands
    if (a == 'a')
    {
      while (Serial.read() != 'n' ) {
        float sensorValue = analogRead(A0);
        Serial.println(sensorValue);
        delay(500);        // delay in between reads for stability
      }
    }
    if (a == 'b')
    {
      while (Serial.read() != 'n' ) {
        float sensorValue = analogRead(A1);
        Serial.println(sensorValue);
        delay(500);        // delay in between reads for stability
      }
      
    }
  else{
  }
  delay(1000);
}
}
