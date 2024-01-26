#include <iostream>

// Include the header file with your SVM class
#include "rgbti_svc_microml.h"

int main() {
    // Create an instance of the SVM classifier
    Eloquent::ML::Port::SVM classifier;

    // Example input vectors
    //float X_1[] = {190, 149, 102, 3436.37, 1045.86, 210, 281, 258, 6108.59, 1526.8};
    //float X_2[] = {173, 175, 151, 4716.49, 1061.46, 205, 268, 237, 5818.32, 1497.22};

    float X_1[] = {161,	188,	165,		5295.66,	1103.05,	184,	256,	226,		6105.07,	1419.51};
    float X_2[] = {107,	122,	132,	6091.19,	629.235,	118,	154,	148,	6208.05,	817.157};






    // Perform predictions
    int result_1 = classifier.predict(X_1);
    int result_2 = classifier.predict(X_2);

    // Classes corresponding to indices [0, 10, 20, 50, 100, 200, 500]
    int classes[] = {0, 10, 20, 50, 100, 200, 500};

    // Display results
    std::cout << "Result of predict with input X1: " << classes[result_1] << std::endl;
    std::cout << "Result of predict with input X2: " << classes[result_2] << std::endl;

    return 0;
}
