#include "diabetesReg.h"

void setup() {
    Serial.begin(115200);
}

void loop() {
    // replace with your actual feature vector
    float input[10] = {0.1, -0.2, 0.2, -0.4, 0.5,0.6, 0.7, -0.8, 0.9, -1.0 };
    
    Serial.print("Prediction: ");
    Serial.println(score(input));
}
