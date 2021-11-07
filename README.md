# Hemodialysis

E-kidney is a software that is used in blood cleaning process (hemodialysis) to normalize blood of intoxicated people or with kidney diseases.
https://www.youtube.com/watch?v=6kGaB6gFf8s

I used https://github.com/seanny1986/particlePhysics.git for simulation of movement of electrolytes.


## Inspiration

Personalized medicine and on the fly adjustment of therapy represents a current trend of medical practice and research.
Hemodialysis represents the standard  process of treatment and correction of the blood abnormalities in patients with kidney failure for millions awaiting renal transplant . Hemodialysis is also used for emergent  blood detoxification in cases of poisoning. However the current hemodialysis treatment is based on rigid protocols, that leads to either over correction or under correction  of some toxins[electrolytes ] with serious consequences on morbidity and mortality. 
 Our study is aimed to model computationally the process of hemodialysis and  to make it more efficient in terms of timing and physiologic normalization of electrolytes or removal of the toxins.  
 Imagine that a patient undergoes hemodialysis 3-5/hr/session 3 times a week for the rest of his life and every time he will have a hemodialysis his abnormalities may be different depending on diet, medication , fluid intake. If we can shorten the dialysis session only by half an hour ,that multiplied by number of session  a patient may have in his life-time and then multiplied by the number of patients worldwide we can gain maybe thousands years gain in life quality world-wide.   
Our ultimate goal is to create an artificial-intelligence dialysis implementation. 
#ref
###https://www.kidney.org/kidneydisease/global-facts-about-kidney-disease
###https://pharm.ucsf.edu/kidney/need/statistics

## What it does
We simulate hemodialysis with the two compartments:
 the blood compartment and the dialysis fluid compartment.
In the blood compartment are imputed the patient labs -> this is something that we cannot change, but we have control over the exchange dialysis solution and we want to research the optimal composition of this solution for the best timing and the smoothest correction for some electrolytes such as sodium , for which sudden correction can result in brain swelling leading  
