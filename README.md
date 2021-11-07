# Hemodialysis

E-kidney is a software that is used in blood cleaning process (hemodialysis) to normalize blood of intoxicated people or with kidney diseases.
https://www.youtube.com/watch?v=6kGaB6gFf8s

The project was developed together with Martian Cezar Lapadatescu.
We used https://github.com/seanny1986/particlePhysics.git for simulation of movement of electrolytes.

# Inspiration
Patients that have undergone CPR during or after dialysis, some without surviving , but whose hope is not forgotten. Personalized medicine and on the fly adjustment of therapy represents a current trend of medical practice and research. Hemodialysis represents the standard process of treatment and correction of the blood abnormalities in patients with kidney failure for millions awaiting renal transplant . Hemodialysis is also used for emergent blood detoxification in cases of poisoning. However the current hemodialysis treatment is based on rigid protocols, that leads to either over correction or under correction of some toxins[electrolytes ] with serious consequences on morbidity and mortality. Our study is aimed to model computationally the process of hemodialysis and to make it more efficient in terms of timing and physiologic normalization of electrolytes or removal of the toxins.
Imagine that a patient undergoes hemodialysis 3-5/hr/session 3 times a week for the rest of his life and every time he will have a hemodialysis his abnormalities may be different depending on diet, medication , fluid intake. If we can shorten the dialysis session only by half an hour ,that multiplied by number of session a patient may have in his life-time and then multiplied by the number of patients worldwide we can gain maybe thousands years gain in life quality world-wide.
Our ultimate goal is to create an artificial-intelligence assisted dialysis implementation.
Ref
https://www.kidney.org/kidneydisease/global-facts-about-kidney-disease
https://pharm.ucsf.edu/kidney/need/statistics

# What it does
We simulate hemodialysis with the two compartments: the blood compartment and the dialysis fluid compartment. In the blood compartment are imputed the patient labs -> this is something that we cannot change, but we have control over the exchange dialysis solution Electrolytes’ concentrations, and we want to research the optimal composition of this solution for the best timing and the smoothest correction for some electrolytes such as sodium, for which sudden correction can result in brain swelling leading to altered mental state, confusion or death. While even fine changes in Potassium concentration may trigger cardiac arrhythmias or sudden arrest.

# How we built it
We try to mirror the static and dynamic properties of particles suspended in fluid and interacting with the bounder surfaces. We applied the principle of independence distribution and movement across concentration in a mixture of diluted Electrolytes. We considered Constant_of_Velocity that applies to each Electrolytes , but determining its motion speed in conjunction to its physical properties such as density[calculated from volume and mass] and charge_Name and charge_Magnitude. We designed a probabilistic model of Electrolyte passing the separation membrane/barrier between the two compartments, that is updated dynamically as follows : If the Electrolyte P is in compartment 1 with the concentration of the electrolyte Cp1 , and concentration Cp2 in the compartment 2, then the probability of P crossing from compartment 1 into compartment 2 is given by Cp1 / ( Cp1 + Cp2 ) and vice versa if P in compartment 2 the probability of P crossing from compartment 2 into compartment 1 is given by Cp2 / ( Cp1 + Cp2 ) . We computed and displayed on the fly the DELTA vector containing the differences between current concentrations of the Electrolytes in the blood compartment minus the vector containing their respective normal concertation values .

# Challenges we ran into
First was finding the right project, the current one coming the fourth on the list. We accurately depicted the the equilibrium state , in where in the blood compartment there is a %50 of Electrolyte leaving the compartment and %50 of that Electrolyte leaking from dialysate back into blood.
When an Electrolyte is reaching normal values in the blood compartment we set the concentration in the exchange compartment to the normal concentration in the blood, collect the timing of normalization, while the clearance for the remaining electrolytes continue. Displaying a graph whose data changes in real time. There web-resourced having demo by looping through an existing data frame and showing a dynamic change of the graph but not from a changing data frame.
Accomplishments that we're proud of
An original , probably singular to this moment, physic-chemical model of dialysis. Real-time data sampling and display of the gaps between target and the current state. The ability to fast forward or slow motion while traversing the separation process without alteration of the particles’ states and transitions, thus enabling fast and accurate predictions or slow detailed observations. The flexibility to study and adapt to different exchange models, such a membranes properties. Potential integration in research and clinical practice. Possible extensions to other research or industrial separations models commonly used in pharmacology and chemistry, raw mineral purification.

# What we learned
Pseudo code implementation into code. That we are dealing with a complex, real problem. That during dialysis through the membrane can be aimed bidirectionally ; such as medication , or glucose, vitamins being in high concentration in dialyzing fluid are aimed to pass into patient blood , and we implemented this case in our model.
Team work, resilience and communication, that every one is important for success.
What's next for E-kidney
- compare and contrast the data of the hemodialysis simulation to the physical exchange between two compartments of fluids separated by a permeable membranes. - account the exchanges of water between the compartments [ “ the dialysate urine“], the consequent changes in the electrolyte concentrations by including an additional parameter in each compartment represented by the pressure, which will represent the driving force for the water exchange; we may add here also the fluid's tonicity and osmolality.
- correct the Electrolyte’ probability of passing the membranes based on its property. -collect data, train and run machine and deep learning analysis retrospectively or on real time, to obtain to correct in most physiological and time-efficient manner patients’ electrolytical or toxicological disturbances.
-Implement a database data storage - Write code to flag the exchange solutions inputs that can be dangerous or illogical.
-As we can control the exchange solution electrolyte concentrations, an electrolyte or certain electrolytes can be chosen alternatively to be cleared out from blood and such scheduling can implement putative Operating System scheduling algorithms while studying which may be the most efficient chemical or biological separation sequences.
