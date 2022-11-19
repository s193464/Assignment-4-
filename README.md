<h1> Assignment 4 </h1>
  <h4> 41934 Advanced BIM Fall 22 </h4>
  
  <em>Group 6: Gabriela Miti Tsuge Costa (s220075) and Kirstine Mia Odgaard (s193464)</em>
  
  
## 1. Goal
The goal of this tool is to guide architects in the early design phase, to check if their designed exterior walls comply with the Danish Building Regulation 18 (BR18) regarding the U-value.


## 2. Use case
The U-value of the exterior walls is an important parameter regarding the energy efficiency of a building. This process is part of the BIM USE "Analyze", since it gives information about how much energy there is needed, to heat up the building. 
In order to analyze, it is necessary to gather information about the materials and thickness in the external walls. With this analysis it is possible to validate if the U-value of the building complies with BR18 [^1].
 
 
## 3. Workflow
 
  ![diagram](https://user-images.githubusercontent.com/112421127/198092534-47443485-9ad6-467c-8a1a-c3996f963a3e.svg)
  
### _Process_

When starting the process, different criterias needs to be identified. For doing this, the IFC model is used for the information exchange. Based on this, data of the external wall can be generated. DS418 is used for the reference information, in order to gather data for the thermal conductivity. The U-value can now be calculated, based on this data. BR18 is then used as a reference information, to check if the U-value is acceptable. If not, the criteria of the external wall must be identified again. If yes, then the data of the area of the external wall can be gathered, and the transmission loss can be calculated. The results are then shown to the user of the tool. The process is then terminated

 ## 4. Information Exchange
 
 ![BIM Information Exchange Group 6](https://user-images.githubusercontent.com/112421127/198220722-b772f513-2714-4fe3-82d0-1d1a8c6f563e.JPG)
 
 The 
 
 ### _4.1  Exterior Walls properties:_

The first part of the process is to identify all exterior walls, and their properties: envelope area, materials, thickness, thermal properties. 
The IFC Architectural model is used for the information exchange. The type of material and thickness are usually difinied in the IFC model, however most models do not have the thermal conductivity of the materials specified.


### _4.2  U-value_

In order to calculate the U-value, data from the DS-418 (Dansk Standard)[^3] can be used to stipulate the thermal conductivity of the materials not specified in the model. The DS-418 data was gather in [***Speckle***](https://speckle.xyz/streams/8ecac565ac/commits/06ae4dad4c) to facilitate the information exchange.

  
  





## 5. Appendix

[^1]: Standard for Denmark: 
[^2]: MOLIO: https://anvisninger.molio.dk/gratis-vaerktojer/bygningsdelsspecifikationer/bygningsdelsspecifikationer
[^3]: DS-418
