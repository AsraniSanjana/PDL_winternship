
#include "dtcCurrency.h"


void setup() {
   Serial.begin(115200);
}

void loop() {
   // Input features
   double input[] = {17, 21,  5, 3728.95, 1356.12, 18,  27,  6, 3908.32, 1814.4};
double output[8];
    Serial.print("Prediction: ");
    Serial.println(classify(input,output));
}
