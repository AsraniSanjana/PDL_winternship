
#include "Loan.h"

void setup() {
   Serial.begin(115200);
}

void loop() {
double input[]={-0.1,  3.0906627,  -0.55448733, -0.24693908,  1.2732313,   0.41173269,
  2.11710719, -2.11710719,  1.37208932, -1.37208932, -1.89264089,  1.89264089, -2.54711697,  2.54711697, -0.64147818, -0.7820157,   1.42814704};
// scaled code... 17 features
   double pred=score(input);
    Serial.print("Prediction: ");
    Serial.println(score(input));
    //Serial.println("prediction result: {}".format(int(pred)))
    Serial.println(int(pred));


    
}
