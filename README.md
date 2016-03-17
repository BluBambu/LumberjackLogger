# LumberjackLogger
A Python function logger tool.

## Project Proposal
https://docs.google.com/document/d/1ZUMmpneq-leWA4OewGtOOsApVuTM_s_D6JsCiVZO9U4/edit

## Project Tutorial and Reference
https://docs.google.com/document/d/1JHYtOMG2MgqlvxNnF1_BTcOAJnJ1UU1J8zo4HY6gjAw/edit

## Design Document
https://docs.google.com/document/d/1TaY54rpnuW6ja1uKfws6jBi-r90y8P6zhhhL9zjRAiQ/edit

## Project Slides/Poster
https://github.com/BluBambu/LumberjackLogger/blob/master/slides.ppt

## Source Code and Examples:

All of the project code and example are included in the src directory of the Github repo.<br /><br />
Before running the command, ```spec.py``` should be changed so that it contains the query specifications. ```spec.py``` already contains the query specifications for the easy, intermediate, and advanced examples. Simply uncomment the respective query specifications for the tool to work on the respective example.<br /><br />
The command line to run the tool:
```
python lumberjack.py <sourceFile> <injectQueryCode>
```
```<sourceFile>``` is the file with the source code to convert.<br />
```<injectQueryCode>``` should be ```true``` if the query code should be added to the end of script, can be any other value otherwise to not inject query code.<br /><br />
After running the command, the modified source code will be printed out to the console. Simply pipe this output to a file and run it. Note that the *_out.py files for the demos is simply the output of tool for that respective demo. For example, the contents of ```advanced_demo_out.py``` is the result of running:
```
python lumberjack.py advanced_demo.py true
```
