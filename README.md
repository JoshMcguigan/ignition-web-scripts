# ignition-web-scripts

Ignition web scripts are a collection of Python scripts which can be used to extend [Inductive Automation](https://inductiveautomation.com/)'s Ignition software package with a REST API. 

## Installation

  1. Install Ignition and the Web Dev module
  2. Create an Ignition project (for compatibility with [ignition-web-hoc](https://github.com/JoshMcguigan/ignition-web-hoc) React component, name the project 'api')
  3. Open the project with the Ignition designer and create new Python resources for each of the scripts in the '/src' directory of this repository. The Python resources in Ignition should have the same name as the files in the '/src' directory, omitting the '.py' extension. 
  
## Usage

### Tag Read

  * POST to 'localhost:8088/main/system/webdev/api/tagRead'
  * Content-Type: text/plain 
  * Body
  
        {
          "tagPaths":["path/to/tag/tag1", "path/to/tag/tag2"]
        }
        
  * Response
  
        {

          "path/to/tag/tag1": {

            "value": 25,

            "quality": "Good",

            "timestamp": "Tue Oct 10 13:53:42 MST 2017"

          },
          
          "path/to/tag/tag2": {

            "value": 25,

            "quality": "Good",

            "timestamp": "Tue Oct 10 13:53:42 MST 2017"

          }

        }
        
### Tag Browse

  * POST to 'localhost:8088/main/system/webdev/api/tagBrowse'
  * Content-Type: text/plain 
  * Body
  
        {
          "rootPath":"folder 1/folder 2/"
        }
        
  * Response
  
        {

          "containers": [

            "subfolder a",
            
            "subfolder b"

          ],
          
          "tags": [

            "tag a",
            
            "tag b"

          ]

        }

### With ignition-web-hoc

To build a React web application using this API, follow the installation instructions above and then follow the steps in the [ignition-web-hoc](https://github.com/JoshMcguigan/ignition-web-hoc) readme.
