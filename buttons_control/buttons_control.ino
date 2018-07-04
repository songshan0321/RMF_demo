#define runEvery(t) for (static uint16_t _lasttime;\
                         (uint16_t)((uint16_t)millis() - _lasttime) >= (t);\
                         _lasttime += (t))
                         
int btn1 = 2;
int btn2 = 4;
int led1 = 12;
int led2 = 13;

int state1 = LOW;      // the current state of the led pin
int reading1;           // the current reading from the input pin
int previous1 = LOW;    // the previous reading from the input pin
int state2 = LOW;
int reading2;
int previous2 = LOW;

int msg;               // 0000000000000000

void setup()
{
  Serial.begin(9600);
  pinMode(btn1, INPUT);
  pinMode(led1, OUTPUT);
  pinMode(btn2, INPUT);
  pinMode(led2, OUTPUT);
}

void loop()
{
  runEvery(50){
    reading1 = digitalRead(btn1);
    reading2 = digitalRead(btn2);
  
    // if the input just went from LOW and HIGH and we've waited long enough
    // to ignore any noise on the circuit, toggle the output pin and remember
    // the time
    if (reading1 == HIGH && previous1 == LOW) {
      if (state1 == HIGH){
        state1 = LOW;}
      else{
        state1 = HIGH;}
    }
        
    if (reading2 == HIGH && previous2 == LOW) {
      if (state2 == HIGH){
        state2 = LOW;}
      else{
        state2 = HIGH;}
        
    }
  //  Serial.println(state);
    digitalWrite(led1, state1);
    digitalWrite(led2, state2);
  
    previous1 = reading1;
    previous2 = reading2;
  }

  runEvery(110){
    String msg ;
    msg.concat(int(state1));
    msg.concat(int(state2));
    for(int i=0;i<14;i++){
      msg.concat(0);
    }
    Serial.println(msg);
//    Serial.print("SENT: ");
//    Serial.println(bytesSent);
  }
}
