
/////////////////////////////////////////////////////////////////////////////////
// Author: Marco Rubio 
// Date: 9/10/2017
// Description:
//    This code was not meant to be clean
//    its goal was to get a prototype up and running quick
/////////////////////////////////////////////////////////////////////////////////


unsigned long timer = millis();
unsigned int iterator = 0; //Used in iterations
unsigned int counter = 0;  //Also used in iterations, no more then 12 bits aka 4096
unsigned int record_length = 0;
unsigned int state = 1;
unsigned int debug_display = 0; //shows analog digits
unsigned int button_states_prev = 0;
unsigned int button_states_now  = 0;
unsigned int select_states_prev = 0;
unsigned int select_states_now  = 0;
bool DEBUG = 0;

//Records for up to 2 mintues and 30 seconds
const int REC_SIZE = 120;
const int REC_SPEED = 100; //Millesecond recording time
unsigned int r0[REC_SIZE];
unsigned int r1[REC_SIZE];
unsigned int r2[REC_SIZE];
unsigned int r3[REC_SIZE];
unsigned int r4[REC_SIZE];

unsigned int * recordings [5] = {(unsigned int *)&r0,(unsigned int *)&r1,(unsigned int *)&r2,(unsigned int *)&r3,(unsigned int *)&r4};

int a = 8;
int b = 9;
int c = 10;
int d = 11;
int e = 12;
int f = 13;
int g = A0;

int PLAY = 2;
int STOP = 3;
int LIGHT_IN = 4;
int M1_IN = 5;
int M2_IN = 6;
int M3_IN = 7;

//int M1_OUT = a;//A1;
//int M2_OUT = b;//A2;
//int M3_OUT = c;//A3;
//int LIGHT_OUT = d;//A4;

int M1_OUT = A1;
int M2_OUT = A2;
int M3_OUT = A3;
int LIGHT_OUT = A4;

int GREEN = A5;
int RED = 0;   //If it didn't have a resistor it would cause issues
int SELECT = A6;


int DISP[] = {a,b,c,d,e,f,g};

int d0[] = {1,1,1,1,1,1,0}; //0
int d1[] = {0,1,1,0,0,0,0}; //1
int d2[] = {1,1,0,1,1,0,1}; //2
int d3[] = {1,1,1,1,0,0,1}; //3
int d4[] = {0,1,1,0,0,1,1}; //4
int d5[] = {1,0,1,1,0,1,1}; //5
int d6[] = {1,0,1,1,1,1,1}; //6
int d7[] = {1,1,1,0,0,0,0}; //7
int d8[] = {1,1,1,1,1,1,1}; //8
int d9[] = {1,1,1,1,0,1,1}; //9
int de[] = {1,0,0,1,1,1,1}; //E
int off[] ={0,0,0,0,0,0,0}; //E

void rotate(int delay_length){  
  digitalWrite(g, 0);
  
  int val = 1;
  
  for(int i = 0; i < 6; i++){
    digitalWrite(DISP[i], val);
    delay(delay_length);
  }
  
  val = 0;
  
  for(int i = 0; i < 6; i++){
    digitalWrite(DISP[i], val);
    delay(delay_length);
  }
}

void down(int delay_length){ 
    digitalWrite(a, HIGH);
    digitalWrite(d, LOW);
    delay(delay_length);
    digitalWrite(g, HIGH);
    digitalWrite(a, LOW);
    delay(delay_length);
    digitalWrite(d, HIGH);
    digitalWrite(g, LOW);
    delay(delay_length);
}

void up(int delay_length){ 
    digitalWrite(d, HIGH);
    digitalWrite(a, LOW);
    delay(delay_length);
    digitalWrite(g, HIGH);
    digitalWrite(d, LOW);
    delay(delay_length);
    digitalWrite(a, HIGH);
    digitalWrite(g, LOW);
    delay(delay_length);
}

void upDown(int delay_length){
    digitalWrite(g, HIGH);
    digitalWrite(d, LOW);
    delay(delay_length);
    digitalWrite(a, HIGH);
    digitalWrite(g, LOW);
    delay(delay_length);
    digitalWrite(g, HIGH);
    digitalWrite(a, LOW);
    delay(delay_length);
    digitalWrite(d, HIGH);
    digitalWrite(g, LOW);
    delay(delay_length);
  
}


void leds(int a1[], int a2[]){
  for(int i = 0; i < 7; i++){
    digitalWrite(a2[i], a1[i]);
  }
}

void digit(int num){
  switch(num){
    case 0: leds(d0, DISP); break;
    case 1: leds(d1, DISP); break;
    case 2: leds(d2, DISP); break;
    case 3: leds(d3, DISP); break;
    case 4: leds(d4, DISP); break;
    case 5: leds(d5, DISP); break;
    case 6: leds(d6, DISP); break;
    case 7: leds(d7, DISP); break;
    case 8: leds(d8, DISP); break;
    case 9: leds(d9, DISP); break;
    case -1: leds(off, DISP); break;
    default: leds(de, DISP); break;
  }
}

void countDown(int delay_length){
  digit(3);
  delay(delay_length);
  digit(2);
  delay(delay_length);
  digit(1);
  delay(delay_length);  
  digit(-1);
}

int get_selection(){
  return map(analogRead(SELECT), 0,900, 0,4);
}

void debug_on(){
  M1_OUT = a;
  M2_OUT = b;
  M3_OUT = c;
  LIGHT_OUT = d;  
}
void debug_off(){  
  M1_OUT = A1;
  M2_OUT = A2;
  M3_OUT = A3;
  LIGHT_OUT = A4;  
}

void setup() {
  // put your setup code here, to run once:
  pinMode(PLAY,INPUT_PULLUP);
  pinMode(STOP,INPUT_PULLUP);
  pinMode(M1_IN,INPUT_PULLUP);
  pinMode(M2_IN,INPUT_PULLUP);
  pinMode(M3_IN,INPUT_PULLUP);
  pinMode(LIGHT_IN,INPUT_PULLUP);
  
  pinMode(M1_OUT,OUTPUT);
  pinMode(M2_OUT,OUTPUT);
  pinMode(M3_OUT,OUTPUT); 
  pinMode(LIGHT_OUT,OUTPUT); 
  pinMode(RED,OUTPUT);
  pinMode(GREEN,OUTPUT);
  
  pinMode(SELECT,INPUT);
  
  pinMode(a,OUTPUT);
  pinMode(b,OUTPUT);
  pinMode(c,OUTPUT);
  pinMode(d,OUTPUT);
  pinMode(e,OUTPUT);
  pinMode(f,OUTPUT);
  pinMode(g,OUTPUT);

  digitalWrite(M1_OUT,LOW);
  digitalWrite(M2_OUT,LOW);
  digitalWrite(M3_OUT,LOW);
  digitalWrite(LIGHT_OUT,LOW);
  digitalWrite(RED,LOW);
  digitalWrite(GREEN,LOW);  
  
  r0[0] = 0xFFFF;
  r1[0] = 0xFFFF;
  r2[0] = 0xFFFF;
  r3[0] = 0xFFFF;
  r4[0] = 0xFFFF;
  delay(100);

  //If holding down light button on restart enter dbug modes
  if(!digitalRead(LIGHT_IN)) DEBUG = 1;

  Serial.begin(9600);

}

void normal(){  
  digitalWrite(M1_OUT, !digitalRead(M1_IN));
  digitalWrite(M2_OUT, !digitalRead(M2_IN));
  digitalWrite(M3_OUT, !digitalRead(M3_IN));
  digitalWrite(LIGHT_OUT, !digitalRead(LIGHT_IN));
}

int play(unsigned int record){    
  if(recordings[record][iterator] == 0xFFFF){
    return 1;
  }
  if(millis()- timer >= REC_SPEED && counter < 4096){
    if(counter == (recordings[record][iterator] & 0x0FFF)) //Ignore the upper 4 bytes where motors states are
     {
      digitalWrite(M1_OUT, (recordings[record][iterator] &  0x1000) == 0);
      digitalWrite(M2_OUT, (recordings[record][iterator] &  0x2000) == 0);
      digitalWrite(M3_OUT, (recordings[record][iterator] &  0x4000) == 0);
      digitalWrite(LIGHT_OUT, (recordings[record][iterator] &  0x8000) == 0);
      iterator++;
    }
    counter++;
    timer = millis();
    return 0;
  }
}

int record(unsigned int record){  
  //save to array
  button_states_now = digitalRead(M1_IN) | digitalRead(M2_IN) << 1 | digitalRead(M3_IN) << 2 | digitalRead(LIGHT_IN) << 3;
  if(millis()- timer >= REC_SPEED && counter < 4096)
  {
    normal();
    //Save states to  recording array
    
    if(button_states_now != button_states_prev)
    {
      recordings[record][iterator] = (button_states_now << 12) | counter;
      iterator++;
      int prev = button_states_now;
      button_states_prev = prev;      
    }
    
    //increment iterator
    counter++;

    //reset timer
    timer = millis();
  }
}

unsigned long rtimer = millis();
int red_state = 0;
void blinkRed(int rate){  
  if(millis()- rtimer >= rate){
    digitalWrite(RED, red_state);
    digitalWrite(GREEN, LOW);
    red_state = !red_state;  
    rtimer = millis();    
  }
  
}

unsigned long gtimer = millis();
int green_state = 0;
void blinkGreen(int rate){
  if(millis()- gtimer >= rate){
    digitalWrite(GREEN, green_state);
    digitalWrite(RED, LOW);
    green_state = !green_state; 
    gtimer = millis();   
  }
  
}

void blinkNone(){
  digitalWrite(GREEN, LOW);
  digitalWrite(RED, LOW);
}

void blinkWarn(int rate){
  digitalWrite(RED,HIGH);
  delay(rate);
  digitalWrite(RED, LOW);
  digitalWrite(GREEN,HIGH);
  delay(rate);
  digitalWrite(GREEN,LOW);
  digitalWrite(RED,HIGH);
  delay(rate);
  digitalWrite(RED, LOW);
  digitalWrite(GREEN,HIGH);
  delay(rate);
  digitalWrite(GREEN,LOW);
  
}

void printStates(){       
      Serial.print(!digitalRead(M1_IN));
      Serial.print(",");
      Serial.print(!digitalRead(M2_IN));
      Serial.print(",");
      Serial.print(!digitalRead(M3_IN));
      Serial.print(",");
      Serial.print(!digitalRead(LIGHT_IN));
      Serial.print(",");
      Serial.print(!digitalRead(PLAY));
      Serial.print(",");
      Serial.print(!digitalRead(STOP));
      Serial.print(",");
      Serial.println(!digitalRead(get_selection()));
}

void getStates(){
  Serial.readStringUntil("\n")
}


void loop() 
{
  state = 1; // Dont record or play back NOTE: remove this for original functinability
  
  switch(state)
  {
    case 1:
    
      button_states_now = digitalRead(M1_IN) | digitalRead(M2_IN) << 1 | digitalRead(M3_IN) << 2 | digitalRead(LIGHT_IN) << 3;
      if(DEBUG){
        debug_on();        
        select_states_now = get_selection();
        if(button_states_now != button_states_prev){
          //display motors
          digit(-1);
          debug_display = 1;
          button_states_prev = button_states_now;
        }
        else if(select_states_now != select_states_prev){
          digit(-1);
          debug_display = 0;
          select_states_prev = select_states_now;          
        }
        
        if(debug_display) normal();  
        else digit(get_selection()+1);
      }
      else{
        //normal(); // NOTE: add back in
        digit(get_selection()+1);        
        if(button_states_now != button_states_prev){        
          button_states_prev = button_states_now;   
        }
      }
      iterator = 0;
      counter = 0;
      blinkNone();
      if(!digitalRead(STOP)){
        state = 2; //Go to recording state
        digit(-1);
        rotate(60); // NOTE: add back in for nurmal function
        countDown(600); // NOTE: add back in to work normal
      }
      if(!digitalRead(PLAY)){
        state = 3; //Go to recording state
        digit(-1);
        rotate(60);
        rotate(60);
        rotate(60);
         
        if(recordings[get_selection()][0] == 0xFFFF){
            blinkWarn(200);
            state = 4;
            break;
        }
        countDown(600);
      }
      break;
    case 2:
      if(DEBUG) debug_on();
      record(get_selection());
      blinkRed(500);
      if(!digitalRead(STOP) || counter >= 4096)
      {
        recordings[get_selection()][iterator] = 0xFFFF; //End Signal
        state = 4; //Go to normal state
        digit(-1);
        rotate(60);
        rotate(60);
        rotate(60);
      }
      break;
    case 3:   
      if(DEBUG) debug_on();
      //blinkGreen(500);
      digitalWrite(RED, HIGH);
      if(play(get_selection()))
      {
        state = 4;
      }
      break;
    case 4:
      delay(100);
      if(digitalRead(STOP) && digitalRead(PLAY)) state = 1;
      record_length = iterator; //Used by playback
      break;
    default: state = 1; break;
  }
  
  delay(100);
  printStates();
}

