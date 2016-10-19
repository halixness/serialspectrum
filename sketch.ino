
void setup(){
  Serial.begin(9600);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
}

void loop(){
  if(Serial.read() > '8'){ 
      digitalWrite(4,HIGH);
      digitalWrite(3,HIGH);
      digitalWrite(2,HIGH);
  }else {
    if(Serial.read() > '5'){ 
      digitalWrite(3,HIGH);
      digitalWrite(2,HIGH);
    }else{
      if(Serial.read() >'0'){
        digitalWrite(2,HIGH);
      }
      else{
        digitalWrite(4,LOW);
        digitalWrite(3,LOW);
        digitalWrite(2,LOW);
      }
    } 
  }
 delay(60);
}
