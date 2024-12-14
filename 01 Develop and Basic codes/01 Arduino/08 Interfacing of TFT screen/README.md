### Interfacing of TFT Screen

```js
// Adafruit ST7735 and ST7789 Library by Adafruit OR TFT by Arduino, Adafruit


// include TFT and SPI libraries
#include<TFT.h>
#include<SPI.h>

// pin definition for arduino UNO
#define cs   10
#define dc   9
#define rst  8

// create an instance of the library
TFT TFTscreen = TFT(cs, dc, rst);

void setup() {
  // initialize the screen
  TFTscreen.begin();

  // clear the screen with the black background
  TFTscreen.background(0,0,0);

  // set the text size
  TFTscreen.setTextSize(2);
}

void loop() {
  // generate random color
  int redRandom = random(0, 255);
  int greenRandom = random(0, 255);
  int blueRandom = random(0, 255);

  // set a random font color
  TFTscreen.stroke(redRandom, greenRandom, blueRandom);

  // print Hello, World! in the middle of the Screen
  TFTscreen.text("Hello, World!", 6, 57);

  // wait 200 miliseconds until change to next color
  delay(200);
}
```
