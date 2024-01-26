
#ifndef UUID135911236015808
#define UUID135911236015808

/**
  * RandomForestClassifier(base_estimator=deprecated, bootstrap=True, ccp_alpha=0.0, class_name=RandomForestClassifier, class_weight=None, criterion=gini, estimator=DecisionTreeClassifier(), estimator_params=('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha'), max_depth=None, max_features=sqrt, max_leaf_nodes=None, max_samples=None, min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=None, num_outputs=3, oob_score=False, package_name=everywhereml.sklearn.ensemble, random_state=None, template_folder=everywhereml/sklearn/ensemble, verbose=0, warm_start=False)
 */
class RandomForestClassifier {
    public:

        /**
         * Predict class from features
         */
        int predict(float *x) {
            int predictedValue = 0;
            size_t startedAt = micros();

            
                    
            uint16_t votes[3] = { 0 };
            uint8_t classIdx = 0;
            float classScore = 0;

            
                tree0(x, &classIdx, &classScore);
                votes[classIdx] += classScore;
            
                tree1(x, &classIdx, &classScore);
                votes[classIdx] += classScore;
            
                tree2(x, &classIdx, &classScore);
                votes[classIdx] += classScore;
            
                tree3(x, &classIdx, &classScore);
                votes[classIdx] += classScore;
            
                tree4(x, &classIdx, &classScore);
                votes[classIdx] += classScore;
            
                tree5(x, &classIdx, &classScore);
                votes[classIdx] += classScore;
            
                tree6(x, &classIdx, &classScore);
                votes[classIdx] += classScore;
            
                tree7(x, &classIdx, &classScore);
                votes[classIdx] += classScore;
            
                tree8(x, &classIdx, &classScore);
                votes[classIdx] += classScore;
            
                tree9(x, &classIdx, &classScore);
                votes[classIdx] += classScore;
            

            // return argmax of votes
            uint8_t maxClassIdx = 0;
            float maxVote = votes[0];

            for (uint8_t i = 1; i < 3; i++) {
                if (votes[i] > maxVote) {
                    maxClassIdx = i;
                    maxVote = votes[i];
                }
            }

            predictedValue = maxClassIdx;

                    

            latency = micros() - startedAt;

            return (lastPrediction = predictedValue);
        }

        
            
            /**
             * Get latency in micros
             */
            uint32_t latencyInMicros() {
                return latency;
            }

            /**
             * Get latency in millis
             */
            uint16_t latencyInMillis() {
                return latency / 1000;
            }
            

    protected:
        float latency = 0;
        int lastPrediction = 0;

        
            

        
            
                /**
                 * Random forest's tree #0
                 */
                void tree0(float *x, uint8_t *classIdx, float *classScore) {
                    
                        if (x[1] < 2.8285751342773438) {
                            
                                
                        if (x[0] < 0.47395316511392593) {
                            
                                
                        if (x[1] < 2.528783440589905) {
                            
                                
                        *classIdx = 2;
                        *classScore = 35.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[0] < -0.4202517494559288) {
                            
                                
                        *classIdx = 2;
                        *classScore = 35.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 34.0;
                        return;

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 1;
                        *classScore = 31.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[0] < -1.5859326720237732) {
                            
                                
                        *classIdx = 2;
                        *classScore = 35.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 4.305071592330933) {
                            
                                
                        if (x[1] < 4.1765196323394775) {
                            
                                
                        if (x[0] < -0.6963706314563751) {
                            
                                
                        *classIdx = 2;
                        *classScore = 35.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 3.719429612159729) {
                            
                                
                        if (x[0] < -0.24976365640759468) {
                            
                                
                        *classIdx = 2;
                        *classScore = 35.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 34.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 34.0;
                        return;

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 2;
                        *classScore = 35.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 34.0;
                        return;

                            
                        }

                            
                        }

                            
                        }

                }
            
        
            
                /**
                 * Random forest's tree #1
                 */
                void tree1(float *x, uint8_t *classIdx, float *classScore) {
                    
                        if (x[0] < -0.3518848568201065) {
                            
                                
                        if (x[1] < 4.062972784042358) {
                            
                                
                        *classIdx = 2;
                        *classScore = 26.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 4.698897361755371) {
                            
                                
                        if (x[1] < 4.361135959625244) {
                            
                                
                        *classIdx = 0;
                        *classScore = 42.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 2;
                        *classScore = 26.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 42.0;
                        return;

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[1] < 2.8453532457351685) {
                            
                                
                        if (x[1] < 2.1375531554222107) {
                            
                                
                        *classIdx = 1;
                        *classScore = 32.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 2.6855287551879883) {
                            
                                
                        if (x[1] < 2.350584626197815) {
                            
                                
                        *classIdx = 0;
                        *classScore = 42.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 2.4778414964675903) {
                            
                                
                        *classIdx = 1;
                        *classScore = 32.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 42.0;
                        return;

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 1;
                        *classScore = 32.0;
                        return;

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[1] < 4.203420162200928) {
                            
                                
                        *classIdx = 0;
                        *classScore = 42.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 4.339936256408691) {
                            
                                
                        *classIdx = 2;
                        *classScore = 26.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 42.0;
                        return;

                            
                        }

                            
                        }

                            
                        }

                            
                        }

                }
            
        
            
                /**
                 * Random forest's tree #2
                 */
                void tree2(float *x, uint8_t *classIdx, float *classScore) {
                    
                        if (x[0] < 0.710557222366333) {
                            
                                
                        if (x[1] < 3.8516457080841064) {
                            
                                
                        if (x[1] < 3.1540441513061523) {
                            
                                
                        if (x[1] < 3.046601176261902) {
                            
                                
                        if (x[0] < -0.15589187294244766) {
                            
                                
                        *classIdx = 2;
                        *classScore = 27.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 31.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 31.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 2;
                        *classScore = 27.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[0] < 0.6323449313640594) {
                            
                                
                        if (x[1] < 4.54568076133728) {
                            
                                
                        *classIdx = 0;
                        *classScore = 31.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 4.698897361755371) {
                            
                                
                        *classIdx = 2;
                        *classScore = 27.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 31.0;
                        return;

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 2;
                        *classScore = 27.0;
                        return;

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[1] < 2.8453532457351685) {
                            
                                
                        *classIdx = 1;
                        *classScore = 42.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[0] < 0.9021643102169037) {
                            
                                
                        *classIdx = 2;
                        *classScore = 27.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 31.0;
                        return;

                            
                        }

                            
                        }

                            
                        }

                }
            
        
            
                /**
                 * Random forest's tree #3
                 */
                void tree3(float *x, uint8_t *classIdx, float *classScore) {
                    
                        if (x[1] < 2.8285751342773438) {
                            
                                
                        if (x[0] < 0.4366334304213524) {
                            
                                
                        if (x[1] < 2.3896442651748657) {
                            
                                
                        if (x[0] < -0.15589187294244766) {
                            
                                
                        *classIdx = 2;
                        *classScore = 30.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 32.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 2;
                        *classScore = 30.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 1;
                        *classScore = 38.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[1] < 3.8640373945236206) {
                            
                                
                        if (x[1] < 2.9095653295516968) {
                            
                                
                        *classIdx = 0;
                        *classScore = 32.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 3.4034827947616577) {
                            
                                
                        if (x[0] < 0.8883982300758362) {
                            
                                
                        *classIdx = 2;
                        *classScore = 30.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 32.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[0] < 1.0727892518043518) {
                            
                                
                        *classIdx = 2;
                        *classScore = 30.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 32.0;
                        return;

                            
                        }

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[1] < 3.989566445350647) {
                            
                                
                        *classIdx = 0;
                        *classScore = 32.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[0] < -1.8008280992507935) {
                            
                                
                        *classIdx = 2;
                        *classScore = 30.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 4.305071592330933) {
                            
                                
                        if (x[1] < 4.203420162200928) {
                            
                                
                        *classIdx = 0;
                        *classScore = 32.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 2;
                        *classScore = 30.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 32.0;
                        return;

                            
                        }

                            
                        }

                            
                        }

                            
                        }

                            
                        }

                }
            
        
            
                /**
                 * Random forest's tree #4
                 */
                void tree4(float *x, uint8_t *classIdx, float *classScore) {
                    
                        if (x[1] < 2.8453532457351685) {
                            
                                
                        if (x[0] < 0.47395316511392593) {
                            
                                
                        if (x[0] < -0.11857213824987411) {
                            
                                
                        *classIdx = 2;
                        *classScore = 32.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 32.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 1;
                        *classScore = 36.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[1] < 4.634343385696411) {
                            
                                
                        if (x[0] < -0.9989291727542877) {
                            
                                
                        *classIdx = 2;
                        *classScore = 32.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 2.9446014165878296) {
                            
                                
                        *classIdx = 0;
                        *classScore = 32.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[0] < 0.9391346573829651) {
                            
                                
                        if (x[0] < -0.607555478811264) {
                            
                                
                        *classIdx = 0;
                        *classScore = 32.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[0] < 0.14474186301231384) {
                            
                                
                        *classIdx = 2;
                        *classScore = 32.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 4.35727334022522) {
                            
                                
                        *classIdx = 2;
                        *classScore = 32.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 32.0;
                        return;

                            
                        }

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 32.0;
                        return;

                            
                        }

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 32.0;
                        return;

                            
                        }

                            
                        }

                }
            
        
            
                /**
                 * Random forest's tree #5
                 */
                void tree5(float *x, uint8_t *classIdx, float *classScore) {
                    
                        if (x[0] < -0.8668137192726135) {
                            
                                
                        if (x[0] < -1.5859326720237732) {
                            
                                
                        *classIdx = 2;
                        *classScore = 29.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 4.255159854888916) {
                            
                                
                        *classIdx = 2;
                        *classScore = 29.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 43.0;
                        return;

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[0] < 1.157177746295929) {
                            
                                
                        if (x[1] < 2.294923782348633) {
                            
                                
                        if (x[0] < 0.05735456943511963) {
                            
                                
                        *classIdx = 2;
                        *classScore = 29.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 1;
                        *classScore = 28.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[0] < 0.6323449313640594) {
                            
                                
                        if (x[0] < -0.3076997548341751) {
                            
                                
                        if (x[0] < -0.4882510006427765) {
                            
                                
                        *classIdx = 0;
                        *classScore = 43.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 2;
                        *classScore = 29.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 43.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[1] < 3.4789440631866455) {
                            
                                
                        *classIdx = 1;
                        *classScore = 28.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 4.185506820678711) {
                            
                                
                        *classIdx = 0;
                        *classScore = 43.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 4.430334806442261) {
                            
                                
                        *classIdx = 2;
                        *classScore = 29.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 43.0;
                        return;

                            
                        }

                            
                        }

                            
                        }

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[0] < 2.4956395626068115) {
                            
                                
                        if (x[1] < 2.9383450746536255) {
                            
                                
                        *classIdx = 1;
                        *classScore = 28.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 43.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[0] < 3.240035891532898) {
                            
                                
                        *classIdx = 1;
                        *classScore = 28.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[0] < 3.394772171974182) {
                            
                                
                        *classIdx = 0;
                        *classScore = 43.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 1;
                        *classScore = 28.0;
                        return;

                            
                        }

                            
                        }

                            
                        }

                            
                        }

                            
                        }

                }
            
        
            
                /**
                 * Random forest's tree #6
                 */
                void tree6(float *x, uint8_t *classIdx, float *classScore) {
                    
                        if (x[1] < 2.2261910438537598) {
                            
                                
                        if (x[0] < -0.05844500660896301) {
                            
                                
                        *classIdx = 2;
                        *classScore = 38.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 1;
                        *classScore = 24.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[0] < -0.3076997548341751) {
                            
                                
                        *classIdx = 2;
                        *classScore = 38.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 2.821487307548523) {
                            
                                
                        *classIdx = 1;
                        *classScore = 24.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 4.203420162200928) {
                            
                                
                        if (x[1] < 3.8640373945236206) {
                            
                                
                        if (x[0] < 1.0727892518043518) {
                            
                                
                        if (x[0] < 0.66085284948349) {
                            
                                
                        *classIdx = 0;
                        *classScore = 38.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 2;
                        *classScore = 38.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 38.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 38.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[1] < 4.339936256408691) {
                            
                                
                        *classIdx = 2;
                        *classScore = 38.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 38.0;
                        return;

                            
                        }

                            
                        }

                            
                        }

                            
                        }

                            
                        }

                }
            
        
            
                /**
                 * Random forest's tree #7
                 */
                void tree7(float *x, uint8_t *classIdx, float *classScore) {
                    
                        if (x[1] < 3.3431507349014282) {
                            
                                
                        if (x[1] < 2.9095653295516968) {
                            
                                
                        if (x[0] < 0.4366334304213524) {
                            
                                
                        if (x[0] < -0.23627548292279243) {
                            
                                
                        *classIdx = 2;
                        *classScore = 26.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 42.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 1;
                        *classScore = 32.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 2;
                        *classScore = 26.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[0] < -1.045115351676941) {
                            
                                
                        if (x[1] < 4.794315576553345) {
                            
                                
                        *classIdx = 2;
                        *classScore = 26.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 42.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 42.0;
                        return;

                            
                        }

                            
                        }

                }
            
        
            
                /**
                 * Random forest's tree #8
                 */
                void tree8(float *x, uint8_t *classIdx, float *classScore) {
                    
                        if (x[0] < -0.42700423300266266) {
                            
                                
                        if (x[1] < 4.902410268783569) {
                            
                                
                        if (x[0] < -0.662000834941864) {
                            
                                
                        *classIdx = 2;
                        *classScore = 30.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[0] < -0.6218364834785461) {
                            
                                
                        *classIdx = 0;
                        *classScore = 37.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 2;
                        *classScore = 30.0;
                        return;

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 37.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[1] < 2.862527012825012) {
                            
                                
                        if (x[1] < 2.221549868583679) {
                            
                                
                        *classIdx = 1;
                        *classScore = 33.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 2.662216067314148) {
                            
                                
                        *classIdx = 0;
                        *classScore = 37.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 1;
                        *classScore = 33.0;
                        return;

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[1] < 4.339936256408691) {
                            
                                
                        if (x[0] < 0.6126375794410706) {
                            
                                
                        *classIdx = 0;
                        *classScore = 37.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 4.203420162200928) {
                            
                                
                        if (x[1] < 3.711992025375366) {
                            
                                
                        *classIdx = 0;
                        *classScore = 37.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[0] < 1.0049684643745422) {
                            
                                
                        *classIdx = 2;
                        *classScore = 30.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 37.0;
                        return;

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 2;
                        *classScore = 30.0;
                        return;

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 37.0;
                        return;

                            
                        }

                            
                        }

                            
                        }

                }
            
        
            
                /**
                 * Random forest's tree #9
                 */
                void tree9(float *x, uint8_t *classIdx, float *classScore) {
                    
                        if (x[1] < 2.516901135444641) {
                            
                                
                        if (x[1] < 1.3002896308898926) {
                            
                                
                        if (x[0] < -0.4049113988876343) {
                            
                                
                        *classIdx = 2;
                        *classScore = 34.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 1;
                        *classScore = 21.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[1] < 1.4736040234565735) {
                            
                                
                        *classIdx = 2;
                        *classScore = 34.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[0] < -0.15589187294244766) {
                            
                                
                        *classIdx = 2;
                        *classScore = 34.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[0] < 0.4366334304213524) {
                            
                                
                        *classIdx = 0;
                        *classScore = 45.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 1;
                        *classScore = 21.0;
                        return;

                            
                        }

                            
                        }

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[1] < 3.8640373945236206) {
                            
                                
                        if (x[1] < 3.1540441513061523) {
                            
                                
                        if (x[1] < 2.926908254623413) {
                            
                                
                        *classIdx = 0;
                        *classScore = 45.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[1] < 3.0371975898742676) {
                            
                                
                        *classIdx = 2;
                        *classScore = 34.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 45.0;
                        return;

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[1] < 3.3431507349014282) {
                            
                                
                        *classIdx = 2;
                        *classScore = 34.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[0] < 1.0727892518043518) {
                            
                                
                        *classIdx = 2;
                        *classScore = 34.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 45.0;
                        return;

                            
                        }

                            
                        }

                            
                        }

                            
                        }
                        else {
                            
                                
                        if (x[0] < -1.5859326720237732) {
                            
                                
                        *classIdx = 2;
                        *classScore = 34.0;
                        return;

                            
                        }
                        else {
                            
                                
                        if (x[0] < 0.7546915709972382) {
                            
                                
                        if (x[0] < 0.5514748990535736) {
                            
                                
                        *classIdx = 0;
                        *classScore = 45.0;
                        return;

                            
                        }
                        else {
                            
                                
                        *classIdx = 2;
                        *classScore = 34.0;
                        return;

                            
                        }

                            
                        }
                        else {
                            
                                
                        *classIdx = 0;
                        *classScore = 45.0;
                        return;

                            
                        }

                            
                        }

                            
                        }

                            
                        }

                }
            
        


            
};



static RandomForestClassifier blobClassifier;


#endif
