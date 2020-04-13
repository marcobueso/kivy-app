//byte ipins[] = {A0, A1, A2, A3, A4, A5}; // Analog inputs, ys, cols
//byte opins[] = {0, 1, 2, 3, 4, 5}; // Digital outputs, xs, rows
byte ipins[] = {A0}; // Analog inputs, ys, cols
byte opins[] = { 2}; // Digital outputs, xs, rows

int xs = sizeof(opins);
int ys = sizeof(ipins);
int a = 1;
int matrix[1][1] = {{0}};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
for (int x=0; x<xs; x++) {
   a = setRow(x);
     for (int y=0; y<ys; y++) {
      int value = random(800);//readCol(y);
      //wait for 
      while(Serial.available()==0) {}; // wait for 1 keypress
      while(Serial.available() > 0) {Serial.read();};
      // delay(500)//delay in millisecs, can change # if needed
      // uncomment line above and use it instead of "while (Serial.available)" if needed
      Serial.println(value);
   }
  }
}

int setRow(int x) {
  for (int i=0; i<xs; i++) {
    if (i==x) {
      pinMode(opins[i], OUTPUT);
      digitalWrite(opins[i], HIGH); // set selected row to HIGH
    }
    else {
      pinMode(opins[i], INPUT); // float unselected pin
    }
  }
  return a;
}


int readCol(int y) {
  for (int j=0; j<ys; j++) {
    if (j==y){
      pinMode(ipins[j], INPUT);
    }
    else {
      pinMode(ipins[j], OUTPUT);
      digitalWrite(ipins[j], LOW);
    }
  }
    int result = analogRead(ipins[y]);
    return result;
}
