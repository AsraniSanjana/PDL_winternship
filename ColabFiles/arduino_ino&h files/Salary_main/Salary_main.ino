#include "salary.h"

void setup() {
    Serial.begin(115200);
}

void loop() {
    // replace with your actual feature vector
    float input[] = { 8 };
    
    Serial.print("Prediction: ");
    Serial.println(score(input));
}
