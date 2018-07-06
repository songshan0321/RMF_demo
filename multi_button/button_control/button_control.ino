#define runEvery(t) for (static uint16_t _lasttime;\
                         (uint16_t)((uint16_t)millis() - _lasttime) >= (t);\
                         _lasttime += (t))
                         
int btn0 = 2;
int btn1 = 4;
int led0 = 12;
int led1 = 13;

int state0 = LOW;      // the current state of the led pin
int reading0;           // the current reading from the input pin
int previous0 = LOW;    // the previous reading from the input pin
int state1 = LOW;
int reading1;
int previous1 = LOW;

int count0 = 0;
int count1 = 0;

int msg;               // 0000000000000000

int swap_state(int state){
  if (state == HIGH){
    return LOW;}
  else{
    return HIGH;}
}

void setup()
{
  Serial.begin(9600);
  pinMode(btn0, INPUT);
  pinMode(led0, OUTPUT);
  pinMode(btn1, INPUT);
  pinMode(led1, OUTPUT);
}

void loop()
{
  runEvery(50){
    reading0 = digitalRead(btn0);
    reading1 = digitalRead(btn1);
//    Serial.print(count0);
//    Serial.println(count1);
    // Button 0
    if (state0 == LOW){ // When call is inactive, check press
      if (reading0 == HIGH && previous0 == LOW) {
        state0 = swap_state(state0);
      }
    }
    else{ // When call is active
      if(reading0 == HIGH){ // Check press
        count0 += 1;
        if (count0 >= 40){ // Check if button is being pressed for 2 second
          state0 = LOW;
          count0 = 0;
        }
      }
      else{
        count0 = 0;
      }
    }
        
    // Button 1
    if (state1 == LOW){ // When call is inactive, check press
      count1 == 0;
      if (reading1 == HIGH && previous1 == LOW) {
        state1 = swap_state(state1);
      }
    }
    else{ // When call is active
      if(reading1 == HIGH){ // Check press
        count1 += 1;
        if (count1 >= 40){ // Check if button is being pressed for 2 second
          state1 = LOW;
          count1 = 0;
        }
      }
      else{
        count1 = 0;
      }
    }

    
  //  Serial.println(state);
    digitalWrite(led0, state0);
    digitalWrite(led1, state1);
  
    previous0 = reading0;
    previous1 = reading1;
  }

  runEvery(110){
    String msg ;
    msg.concat(int(state0));
    msg.concat(int(state1));
    for(int i=0;i<14;i++){
      msg.concat(0);
    }
    Serial.println(msg);
//    Serial.print("SENT: ");
//    Serial.println(bytesSent);
  }
}
