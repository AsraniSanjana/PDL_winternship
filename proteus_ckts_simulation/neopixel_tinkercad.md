a neopixel has 3 inputs, din vcc gnd. 
using din, all leds in the string can be controlled.
each led is taking 3 i/p from prev led in strip and each led is giving 3 o/ps (it can be same pins)

![image](https://github.com/AsraniSanjana/PDL_winternship/assets/109857762/1d1ad002-ca09-487a-a418-2e457313ffe5)

**Code:**
//using 1 pin i.e. din, we can lightup a series of leds.
#include <Adafruit_NeoPixel.h>

#define PIN            5 // Define the pin number to which the NeoPixel is connected
#define NUMPIXELS      25  // Define the number of NeoPixels in your strip

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  pixels.begin();  // Initialize the NeoPixel library
  pixels.setBrightness(50);  // Set the brightness (0 to 255)
}

void loop() {
  // Set the color of the first NeoPixel (index 0)
  pixels.setPixelColor(24, pixels.Color(255, 0, 0));  // RGB color: Red
  pixels.show();  // Send the updated pixel colors to the hardware
  delay(1000);    // Wait for 1 second (you can adjust the delay as needed)

  // Turn off the first NeoPixel
  pixels.setPixelColor(0, pixels.Color(0, 0, 0));  // RGB color: Black (turn off)
  pixels.show();  // Send the updated pixel colors to the hardware
  delay(1000);    // Wait for 1 second before repeating
}
