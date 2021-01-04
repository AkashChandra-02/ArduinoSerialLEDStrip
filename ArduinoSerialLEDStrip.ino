#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
 #include <avr/power.h> // Required for 16 MHz Adafruit Trinket
#endif

#define LED_PIN 11 

#define NUMPIXELS 12 

Adafruit_NeoPixel pixels(NUMPIXELS, LED_PIN, NEO_GRB + NEO_KHZ800);

String serialData;

void setup() 
{
  pixels.begin(); 
  pixels.clear();
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() 
{
  
}

void serialEvent() 
{
  serialData = Serial.readString();

  if(serialData == "CLS")
  {
    pixels.clear();
  }
  
  else
  {
    pixels.setBrightness(parseBrightness(serialData)); 
    pixels.setPixelColor(parseIndex(serialData), pixels.Color(parseRed(serialData), parseGreen(serialData), parseBlue(serialData)));
    pixels.show();
  }
}

int parseIndex(String data)
{
  data.remove(data.indexOf("L"));
  data.remove(data.indexOf("I"), 1);
  return data.toInt();
}

int parseBrightness(String data)
{
  data.remove(data.indexOf("R"));
  data.remove(0,data.indexOf("L") + 1);
  return data.toInt();
}

int parseRed(String data)
{
  data.remove(data.indexOf("G"));
  data.remove(0,data.indexOf("R") + 1);
  return data.toInt();
}

int parseGreen(String data)
{
  data.remove(0,data.indexOf("G") + 1);
    data.remove(data.indexOf("B"));
  return data.toInt();
}

int parseBlue(String data)
{ 
    data.remove(0, data.indexOf("B") + 1);
    return data.toInt();
}
