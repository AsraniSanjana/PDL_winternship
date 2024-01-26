
#include "blob_classifier.h"

void setup() {
    Serial.begin(115200);
}

void loop() {
    // replace with your actual feature vector
    float input[2] = {1.5, 2.5};

    Serial.print("Prediction: ");
    Serial.println(blobClassifier.predict(input));
}
