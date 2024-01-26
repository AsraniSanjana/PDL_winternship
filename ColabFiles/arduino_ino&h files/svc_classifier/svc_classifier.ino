#include "SVC_classifier.h"
int main() {
    double input_array[] = {1.96, 2.04, 2.12, 1700, 10.72, 32.19};
    int input_size = sizeof(input_array) / sizeof(input_array[0]);

    // Assuming your classification result is a one-hot encoded vector
    double pred[input_size];
    double output_loc[2];

    // Call the classify function
    classify(input_array, output_loc);

    // Find the index with the maximum value as the predicted class
    int max_index = 0;
    for (int i = 1; i < input_size; i++) {
        if (pred[i] > pred[max_index]) {
            max_index = i;
        }
    }
    Serial.print("Prediction: ");
    Serial.println(max_index);

    return 0;
}
