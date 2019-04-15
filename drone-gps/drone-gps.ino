#include "A2CanDecoderLib.h"
#include "FlexCAN.h"
#include "FastCRC.h"

// Use Serial to output data via USB or Serial1 to use Teensy's first serial port
#define SERIAL_PORT Serial
#define NSPIN 8//lat
#define WEPIN 9//lon
#define DOWNPIN 10//kakou

uint32_t currTime, otherTime, clockTime;
char dateTime[20];
uint32_t messageId;
float latpm, lonpm, latgopoint, longopoint;
int latp, latm, lonp, lonm, latadd, lonadd, addspoint;
void setup()
{
  SERIAL_PORT.begin(115200);
  A2CanDecoder.begin();
  pinMode(NSPIN, OUTPUT);
  pinMode(WEPIN, OUTPUT);
  pinMode(DOWNPIN, OUTPUT);
  pinMode(13, OUTPUT);
  latp = 0;
  latm = 0;
  lonp = 0;
  lonm = 0;
  latadd = 0;
  lonadd = 0;
  latgopoint = 35.605897;
  longopoint = 139.358482;
  addspoint = 0;
  digitalWrite(13, HIGH);
}

void loop() {
  messageId = A2CanDecoder.decode();
  currTime = millis();

  if (otherTime < currTime)
  {
    otherTime = currTime + 200;
    SERIAL_PORT.print("Lat: "); SERIAL_PORT.print(A2CanDecoder.getLat(), 7);
    SERIAL_PORT.print(", Lon: "); SERIAL_PORT.print(A2CanDecoder.getLon(), 7);

    latpm = latgopoint - A2CanDecoder.getLat(); //latpmが+なら北
    lonpm = longopoint - A2CanDecoder.getLon(); //lonpmが+なら東
    if (latpm >= 0) {
      digitalWrite(NSPIN, HIGH);
      SERIAL_PORT.println("NS HIGH");
      latp = 1;

    } else {
      digitalWrite(NSPIN, LOW);
      SERIAL_PORT.println("NS LOW");
      latm = 1;
    }
    if (lonpm >= 0) {
      digitalWrite(WEPIN, HIGH);
      SERIAL_PORT.println("WE HIGH");
      lonp = 1;
    }
    else {
      digitalWrite(WEPIN, LOW);
      SERIAL_PORT.println("WE LOW");
      lonm = 1;
    }
    latadd = latp + latm;
    lonadd = lonp + lonm;
    addspoint = latadd + lonadd;
    if (addspoint == 4) {
      digitalWrite(DOWNPIN, HIGH);
      SERIAL_PORT.println("DOWN HIGH");
      digitalWrite(13, LOW);
    }
  }
}

