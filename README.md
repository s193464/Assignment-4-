<h1> Assignment 4 </h1>
  <h4> 41934 Advanced BIM Fall 22 </h4>
  
  <em>Group 6: Kirstine Mia Odgaard (s193464) and Gabriela Miti Tsuge Costa (s220075)</em>
  
  
## 1. Goal
The goal of this tool is to guide architects in the early design phase, to check if their designed exterior walls comply with the Danish Building Regulation 18 (BR18) regarding the U-value.


## 2. Use case
The U-value of the exterior walls is an important parameter regarding the energy efficiency of a building. This process is part of the BIM USE "Analyze", since it gives information about how much energy there is needed, to heat up the building. 
In order to analyze, it is necessary to gather information about the materials and thickness in the external walls. With this analysis it is possible to validate if the U-value of the building complies with BR18 [^1].
Furthermore, when the U-value is calculated, and the total area of the externall walls is found, the transmission loss is also calculated. 
 
 
## 3. Workflow
 
  ![diagram (1)](https://user-images.githubusercontent.com/112421127/203129150-8d47b330-88d4-4c17-a93a-1833b22aa483.svg)

  
### _Process_

When starting the process, different criterias needs to be identified. For doing this, the IFC model is used for the information exchange. Based on this, data of the external wall can be generated. DS418 is used for the reference information, in order to gather data for the thermal conductivity. The values of the different thermal conductivities is uploaded into speckle, and is then streamed from speckle. The U-value can now be calculated, based on this data. BR18 is then used as a reference information, to check if the U-value is acceptable. Like the thermal conductivities, is the BR18 value also streamed from speckle. If the criteria is not met, the criteria of the external wall must be identified again. If yes, then the data of the area of the external wall can be gathered, and the transmission loss can be calculated. The results are then shown to the user of the tool in HTML. The output data also displays if the criteria of BR18 is met. The process is then terminated

 ## 4. Information Exchange
 
 ![BIM Information Exchange Group 6](https://user-images.githubusercontent.com/112421127/198220722-b772f513-2714-4fe3-82d0-1d1a8c6f563e.JPG)
 
 The table above shows the level of Specification of Construction element based on the Model Delivery Specification, developed by DiKon and BIM7AA with collaboration with Molio[^2]. For the Exterior Walls a level LOD 325 DK is required, meaning the wall elements modelled as detailed types of objects with associated properties: materials, dimensions, etc.
 
 ### _4.1.  Exterior Walls properties_

The first part of the process is to identify all exterior walls, and their properties: envelope area, materials, thickness, thermal properties. 
The IFC Architectural model is used for the information exchange. The type of material and thickness are usually difinied in the IFC model, however most models do not have the thermal conductivity of the materials specified.


### _4.2.  U-value_

In order to calculate the U-value, data from the DS418 (Dansk Standard)[^3] can be used to stipulate the thermal conductivity of the materials not specified in the model. The DS418 data was gather in [***Speckle***](https://speckle.xyz/streams/e11e791e2c) to facilitate the information exchange. The exchange of BR18 was also gathered in [***Speckle***](https://speckle.xyz/streams/cce20ff6c3). 

### _4.3. Assumptions_

To calculate the transmission loss, an indoor and outdoor temperature is also needed. It is assumed that the indoor temperature is 20 deg. and the outdoor temperature is -12 deg., as this is a standard for dimensioning temperatures in Denmark. 

## 5. Value

### _5.1. Business Value_

The tool will save the employees time when calculating the U-value and transmission loss. When using IFC, the risk of mistakes will be decreased, compared to finding the data manually by looking at drawings etc.

### _5.2. Social Value_

By ensuring that transmission loss complies with BR18, it is known, that an unnecessary amount of energy is not used to heat up the building. This helps to reduce the emission of CO2, which helps global warming. in addition, it provides an economic advantage for the users of the building, as less energy is used and therefore less money on heating the building.

## 6. Tool
  
In order to support the user to calculate the transmission loss, is the tool used to look up informartion of the external walls and their materials and thickness. When this data is used in combination with the thermal conductivity, it is possible to calculate an U-value. By extracting information about the area of the external wall, by IFC, along with the dimensioning temperatures and U-value, is it possible to calculate the transmission loss. The tool presents the following data, in a visual way: 
- U-value
- Br18 complied (yes/no)
- Transmission loss
- Total area of the externall walls. 

 
 ### _6.1. Tool_
 
To make this possible, following steps are needed:

  1. Check that the IFC file (Duplex A 20110907) contains necessary data regarding the external walls. 
  2. Validate that wanted data is accessible in the external sources. 

Will use following to build the tool:

  3. Python 
  4. IFC openshell
      - IFC Wall (Properties: Thermal Conductivity, Material, Thickness, Area)
  5. Speckle   

Will use following equations:

  6. U-value: 

![u-value](https://user-images.githubusercontent.com/112421127/197871610-8e1b2cac-8d11-4391-af1f-7c9930276962.jpg)

  7. Transmission loss:   

![transmission loss](https://user-images.githubusercontent.com/112421127/197871580-e687ade0-2d40-458c-a4e3-5b4a77e3e419.jpg)



## 7. Prerequisite
For ensuring that program works, following will be needed for python: 
- `pip install ifcopenshell`
- `pip install specklepy`


## 8. Delivery

The tool will calculate the Transmission Losses and U-value of the external walls and perform a conformity check to see if the wall complies with the building regulation BR18. The results are displayed in an HTML format, making it easily accessible. If the wall does not achieve the requirement, the user could start the procedure again with different materials.

![output](https://user-images.githubusercontent.com/112421127/203129951-e19aa02d-2cec-461b-b9d9-e100ba345fc6.jpg)


## 9. Appendix

[^1]: https://bygningsreglementet.dk/Tekniske-bestemmelser/11/Krav/257
[^2]: Model Delivery Specification: https://anvisninger.molio.dk/gratis-vaerktojer/bygningsdelsspecifikationer/bygningsdelsspecifikationer
[^3]: DS418: https://webshop.ds.dk/standard/M337200/ds-418-2011-till-1-2020
