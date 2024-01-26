#include <iostream>

// Include the header file with your SVM class
#include "svm_microml.h"

int main() {
    // Create an instance of the SVM classifier
    Eloquent::ML::Port::SVM classifier;

    // Example input vectors
    float X_1[] = {3.6, 1., 0.2};
    float X_2[] = {2.9, 4.7, 1.4};

    // Perform predictions
    int result_1 = classifier.predict(X_1);
    int result_2 = classifier.predict(X_2);

    // Display results
    std::cout << "Result of predict with input X1: " << result_1 << std::endl;
    std::cout << "Result of predict with input X2: " << result_2 << std::endl;

    return 0;
}

