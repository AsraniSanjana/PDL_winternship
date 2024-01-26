
#include "Loan_wo_scaling.h"

void setup() {
   Serial.begin(115200);
}

void loop() {
   // Input features
//double input[] = { 0, 1, 2, 1, 0, 4006,1526, 168, 360, 1,  1};
double input[]={0, 1, 0, 1, 0, 0, 3307, 3166, 200, 1, 1};
// no-scaled code... 11 features
   double pred=score(input);
   
    Serial.print("Prediction: ");
    Serial.println(score(input));
    //Serial.println("prediction result: {}".format(int(pred)))
    Serial.println(int(pred));


    
}
