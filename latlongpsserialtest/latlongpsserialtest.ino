#define NSPIN 9
#define WEPIN 10
#define DOWNPIN 11

float latpm, lonpm, latgopoint, longopoint, incomingByte, latnpoint, lonnpoint;
int latp, latm, lonp, lonm, latadd, lonadd, addspoint, ded;
void setup()
{
  Serial.begin(9600);
  pinMode(NSPIN, OUTPUT);
  pinMode(WEPIN, OUTPUT);
  pinMode(DOWNPIN, OUTPUT);
  ded = 0;
  latp = 0;
  latm = 0;
  lonp = 0;
  lonm = 0;
  latadd = 0;
  lonadd = 0;
  latgopoint = 35.606386;
  longopoint = 139.358479;
  addspoint = 0;
}

void loop() {

  if (Serial.available() > 0) {
    incomingByte = Serial.read() - 0x30;

    Serial.println(incomingByte);
    Serial.println(ded);
    ded = ded + 1;
    if (ded == 1) {
      latnpoint = incomingByte * 10;
      Serial.println(latnpoint);
      Serial.println("lat10 ok");
    }
    else if (ded == 2) {
      latnpoint = incomingByte + latnpoint;
      Serial.println(latnpoint);
      Serial.println("lat ok");
    }
    if (ded == 3) {
      lonnpoint = incomingByte * 100;
      Serial.println(lonnpoint);
      Serial.println("lon100 ok");
    }
    else if (ded == 4) {
      lonnpoint = incomingByte * 10 + lonnpoint;
      Serial.println(lonnpoint);
      Serial.println("lon10 ok");
    }
    else if (ded == 5) {
      lonnpoint = incomingByte + lonnpoint;
      Serial.println(lonnpoint);
      Serial.println("lon ok");
      ded = 0;
      latadd = latp + latm;
      lonadd = lonp + lonm;
      addspoint = latadd + lonadd;


      latpm = latgopoint - latnpoint; //latpmが+なら北
      lonpm = longopoint - lonnpoint; //lonpmが+なら東
      if (latpm >= 0) {
        digitalWrite(NSPIN, HIGH);
        latp = 1;
      } else {
        digitalWrite(NSPIN, LOW);
        latm = 1;
      }
      if (lonpm >= 0) {
        digitalWrite(WEPIN, HIGH);
        lonp = 1;
      }
      else {
        digitalWrite(WEPIN, LOW);
        lonm = 1;
      }
    }
      latadd = latp + latm;
      lonadd = lonp + lonm;
      addspoint = latadd + lonadd;
    if (addspoint == 4) {
      digitalWrite(DOWNPIN, HIGH);
    }
    Serial.println("Done");
  }
}
