# DenV (Internal name Raktaganit)

DenV is a project that is designed to predict the outcome of a patient in Dengue Viral fever. This software uses atom AI, an artificail intelligence model that we have developed to help engineers, scientists and doctors. Atom AI is currently NOT available for public use, nevertheless we have made some atom services available to the public. 
This software is currently in pre-release version and is available only to **devs** working on the project. 
**All doctors** will be able to access the Beta version with the tentitive release date of **June 15 2023**

**Please contact the developer at `sudhaunshdeshpande@gmail.com` to generate a license. Licensing is free however at this stage we can only provide access to doctors and registered beta testers** The software will not work without the license file!

## How it works 
Once you have provided information about the platelet count, Atom AI analyses the platelet count and predicts the viral load, the NS1 antigen count, cytokines, and the world poppulation data and generates a function based on the afformentioned deails. Another function with error and confidence compensation is generaed. These functions are then substitued with the nuber of days of ranging from day 1 to day 11. Using this information the AI recompensates for any errors, recompiles the cnofedence and outputs an array of platelet count. This count is updated until a satifactory confidence is obtained (above 80%). In some cases the confidence might be low but this would be an apparent error or statistically speaking an outlier. However from the alpha tests we have noticed that even with a low confidence, the predictions stand true. This is because the confidence is calculated using the word poppulation data, and it is not necessary that your patient follows the global trend.  

## What happens with your data?
Your data is protected by this software. We respect your right to privacy and any and all information you provide stays locally on your laptop. The moment you close the application all variables are destroyed. If you chose to generate a pdf report your information is saved. This includes your name, age, platelet counts and platelet predictions. This software is open-sourced and DOES NOT collect your information. However in the case of data breach on your local machine we are not responsible for any liabilities. 

## Supported Platforms 

- macOS 
    - Seamless installation 
    - Run Installer_unix.sh


- Linux 
    - Seamless installation 
    - Run Installer_unix.sh


- Windows 
    - Requires manual Python installation 
    - Install and the software by using the following commands 
    - **Be sure to check the option that adds Python to PATH.**
    - Open command promp by pressing the **Windows** key and typing `cmd`
    - `cd Doccuments`
    - `git clone https://github.com/sudhaunsh/denV.git`
    - Run **install_windows.bat** to install dependencies and libraries.  
    - To run the software in a new command prompt window enter the commands:
    - `cd Documents`
    - `python3 gui.py`
    - **License is not preinstalled in this evaluation copy.** 
    - Contact the developer to attain an evaluation license and instruction to install the license. 

## Bug fixes
- Fixed no prompt generated during pdf report generation

## Features 

- Reliable platelet prediction 
- PDF report generation 
- Requires 2 platelet counts 
- Generates healthcare advisory 
- Auto calibration and report confidence generation 
- Supports primary infection 

## Unsupported features 
- Accountability for medical complications (Coming soon)
- Login Some macs and unix systems do not support md5 and so this feature has been disabled until further notice
- Support for secondary infection

## Committed future updates 
- Accountability for medical complications
- Saving sessions 
- Android platform app
- Log in and cloud storage 
- Support for secondary infection

## Issues
- There has been an issue with the pdf report generator. However, this issue has been partially fixed. Our team is working hard to fix all issues 

# Future scope of this project:
We are currently considering on creating a sensor development plan for a biosensor assay including a platelet sensor and a NS1 LAMP sensor assay that can work with this algorithm to make an effortless dengue tratment. 
The idealogy is with a simple prick of the finger, similar to a blood glucose test, the doctor/patient would get an estimate of the platelet count and can determine the plan of action. This means no more trips to the blood lab. 

# More about Atom AI and its capabilities 
As mentioned abbove Atom AI is an artificial intelligence developed to help people is science. Atom ai currently can perform the following taks:
- Platelet prediction in Dengue viral fever
- Basic and complex math 
- Basic electrochemical analysis for biosensors including but not limited to:
    - Chronoamperometry 
    - Cyclic Voltammetry 
    - Linear sweep Voltammetry 
    - Open circuit potentiometry 
    - Chronopotentiometry 

We are commited to make Aotm services and Atom AI available to the public in the near future. 