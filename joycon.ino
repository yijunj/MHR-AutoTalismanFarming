// Program used to test the Nintento Switch Joystick object on the 
// Arduino Leonardo or Arduino Micro.
//
// Joystick.pressButton(buttonID)
// Joystick.releaseButton(buttonID)

#define BUTTON_Y 0
#define BUTTON_B 1
#define BUTTON_A 2
#define BUTTON_X 3
#define BUTTON_L 4
#define BUTTON_R 5
#define BUTTON_ZL 6
#define BUTTON_ZR 7
#define BUTTON_MINUS 8
#define BUTTON_PLUS 9
#define BUTTON_LCLICK 10
#define BUTTON_RCLICK 11
#define BUTTON_HOME 12
#define BUTTON_CAPTURE 13
#define DIRECTION_UP 0
#define DIRECTION_RIGHT 90
#define DIRECTION_DOWN 180
#define DIRECTION_LEFT 270
#define MIN 0
#define MAX 255
#define NEUTRAL 128

#include "SwitchJoystick.h"

// Create Joystick
SwitchJoystick_ Joystick;

String str;

void parseString(String str) {
  int substrStart = 0;
  int lenStr = str.length();
  String command;
  int duration;

  while(substrStart+6 <= lenStr) {
    command = str.substring(substrStart, substrStart+2);
    duration = str.substring(substrStart+2, substrStart+6).toInt();

    if(command == "AA") {
      Joystick.pressButton(BUTTON_A);
    }
    else if(command == "aa") {
      Joystick.releaseButton(BUTTON_A);
    }
    else if(command == "BB") {
      Joystick.pressButton(BUTTON_B);
    }
    else if(command == "bb") {
      Joystick.releaseButton(BUTTON_B);
    }
    else if(command == "XX") {
      Joystick.pressButton(BUTTON_X);
    }
    else if(command == "xx") {
      Joystick.releaseButton(BUTTON_X);
    }
    else if(command == "YY") {
      Joystick.pressButton(BUTTON_Y);
    }
    else if(command == "yy") {
      Joystick.releaseButton(BUTTON_Y);
    }
    else if(command == "LE") {
      Joystick.pressButton(BUTTON_L);
    }
    else if(command == "le") {
      Joystick.releaseButton(BUTTON_L);
    }
    else if(command == "RI") {
      Joystick.pressButton(BUTTON_R);
    }
    else if(command == "ri") {
      Joystick.releaseButton(BUTTON_R);
    }
    else if(command == "ZL") {
      Joystick.pressButton(BUTTON_ZL);
    }
    else if(command == "zl") {
      Joystick.releaseButton(BUTTON_ZL);
    }
    else if(command == "ZR") {
      Joystick.pressButton(BUTTON_ZR);
    }
    else if(command == "zr") {
      Joystick.releaseButton(BUTTON_ZR);
    }
    else if(command == "PL") {
      Joystick.pressButton(BUTTON_PLUS);
    }
    else if(command == "pl") {
      Joystick.releaseButton(BUTTON_PLUS);
    }
    else if(command == "MI") {
      Joystick.pressButton(BUTTON_MINUS);
    }
    else if(command == "mi") {
      Joystick.releaseButton(BUTTON_MINUS);
    }
    else if(command == "HO") {
      Joystick.pressButton(BUTTON_HOME);
    }
    else if(command == "ho") {
      Joystick.releaseButton(BUTTON_HOME);
    }
    else if(command == "CA") {
      Joystick.pressButton(BUTTON_CAPTURE);
    }
    else if(command == "ca") {
      Joystick.releaseButton(BUTTON_CAPTURE);
    }
    else if(command == "LC") {
      Joystick.pressButton(BUTTON_LCLICK);
    }
    else if(command == "lc") {
      Joystick.releaseButton(BUTTON_LCLICK);
    }
    else if(command == "RC") {
      Joystick.pressButton(BUTTON_RCLICK);
    }
    else if(command == "rc") {
      Joystick.releaseButton(BUTTON_RCLICK);
    }
    else if(command == "DU") {
      Joystick.setHatSwitch(DIRECTION_UP);
    }
    else if(command == "du") {
      Joystick.setHatSwitch(-1);
    }
    else if(command == "DD") {
      Joystick.setHatSwitch(DIRECTION_DOWN);
    }
    else if(command == "dd") {
      Joystick.setHatSwitch(-1);
    }
    else if(command == "DL") {
      Joystick.setHatSwitch(DIRECTION_LEFT);
    }
    else if(command == "dl") {
      Joystick.setHatSwitch(-1);
    }
    else if(command == "DR") {
      Joystick.setHatSwitch(DIRECTION_RIGHT);
    }
    else if(command == "dr") {
      Joystick.setHatSwitch(-1);
    }
    else if(command == "LU") {
      Joystick.setYAxis(MIN);
    }
    else if(command == "LD") {
      Joystick.setYAxis(MAX);
    }
    else if(command == "LL") {
      Joystick.setXAxis(MIN);
    }
    else if(command == "LR") {
      Joystick.setXAxis(MAX);
    }
    else if(command == "LN") {
      Joystick.setXAxis(NEUTRAL);
      Joystick.setYAxis(NEUTRAL);
    }
    else if(command == "RU") {
      Joystick.setRzAxis(MIN);
    }
    else if(command == "RD") {
      Joystick.setRzAxis(MAX);
    }
    else if(command == "RL") {
      Joystick.setZAxis(MIN);
    }
    else if(command == "RR") {
      Joystick.setZAxis(MAX);
    }
    else if(command == "RN") {
      Joystick.setZAxis(NEUTRAL);
      Joystick.setRzAxis(NEUTRAL);
    }
    
    Joystick.sendState();
    delay(duration);

    substrStart += 6;
  }
}

void setup() {
  
  Joystick.begin(false);
  Serial1.begin(9600);
  
  Joystick.setXAxis(NEUTRAL);
  Joystick.setYAxis(NEUTRAL);
  Joystick.setZAxis(NEUTRAL);
  Joystick.setRzAxis(NEUTRAL);
  Joystick.sendState();
}

void loop() {
  if (Serial1.available() > 0) {
    str = Serial1.readString();
  }
  parseString(str);
  str = "";
}
