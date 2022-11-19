<h1> Assignment 4 </h1>
  <h4> 41934 Advanced BIM Fall 22 </h4>
  
  <em>Group 6: Gabriela Miti Tsuge Costa (s220075) and Kirstine Mia Odgaard (s193464)</em>
  
  
  <strong> 1. Goal : </strong>
  <p> The goal of this tool is to guide architects in the early design phase, to check if their designed exterior walls comply with the Danish Building Regulation 18 (BR18) regarding the U-value.
</p>

 <strong> 2. Use case : </strong>
 <p> The U-value of the exterior walls is an important parameter regarding the energy efficiency of a building. This process is part of the BIM USE "Analyze", since it gives information about how much energy there is needed, to heat up the building. 
In order to analyze, it is necessary to gather information about the materials and thickness in the external walls. With this analysis it is possible to validate if the U-value of the building complies with BR18. </p>
 
 
 <strong> 3. Workflow </strong>
 
  ![diagram](https://user-images.githubusercontent.com/112421127/198092534-47443485-9ad6-467c-8a1a-c3996f963a3e.svg)
  
 <strong> 4. Process </strong>
 
 4.1  <em>Exterior Walls properties: </em>

<p> The first part of the process is to identify all exterior walls, and their properties: envelope area, materials, thickness, thermal properties. 
The IFC Architectural model is used for the information exchange. The type of material and thickness are usually difinied in the IFC model, however most models do not have the thermal conductivity of the materials specified.
</p>

 4.2  <em>U-value:</em>

 <p>In order to calculate the U-value, data from the DS-418 (Dansk Standard) can be used to stipulate the thermal conductivity of the materials not specified in the model. The DS-418 data was gather in [Speckle](https://speckle.xyz/streams/8ecac565ac/commits/06ae4dad4c) to facilitate the information exchange. </p>

  
  





4.  <strong> Appendix : </strong>

Standard for Denmark: 
