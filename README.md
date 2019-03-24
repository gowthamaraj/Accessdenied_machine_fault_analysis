# Accessdenied_machine_fault_analysis

## Damage Identification to belts or machinery:
In recent years, much attention has been given to structural health monitoring technology to diagnose the condition of structures using a sensor attached to them, and the number of research projects on the health monitoring of architectural structures is on the rise. Most of the industrial machines and parts are bulky. They may cause the crack to the supporting parts of the rotating parts. in most cases, the crack can be identified with the help of sound and vibration, but it cannot point out where the crack has occurred. It cannot pinpoint where the crack has occurred. Hence to solve this we are going to implement different solutions for different parts of the system.

## BELTS - 
The image of the belt is taken and it is converted into binary using the threshold. Then, the later image is fed into the ML model which can classify whether it is normal or abnormal.
 

## MACHINE PARTS - 
##	methods:
1.Vibration analysis - each vibration will have a signature along with it. Hence, we match the vibration with the signature we already have.
 
2.sound/Noise - the concept of vibration can also be used for monitoring faults using sound.

3.Computer Vision - for most of the visible part with visible cracks, we will be using CV for doing the analysis.

4.Temperature monitoring

5.Open/Short - for the parts which are deep inside, we will stick a sheet of conducting material and will check the continuity of the sheets.
			1. It can be done by using RF transmission method
	                2. It can be done by using a series of the conductor along with a source and Small leads.
			
6.Current and Voltage signature Analysis – Done by using ANN or ML depending on the test case
 

Reference:
https://www.efficientplantmag.com/2012/07/failure-analysis-of-machine-shafts/
https://www.hindawi.com/journals/ijrm/2008/583982/


