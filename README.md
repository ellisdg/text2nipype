# Text2Nipype
A simple tool to create Nipype workflows from text descriptions of image acquisition and processing method.
Text2Nipype uses ChatGPT to read in text from the user and translate that text
into python code for processing neuroimaging data.

## Introduction
Text2Nipype utilizes ChatGPT which requires an OpenAI API key to run. 
You can get one at [https://platform.openai.com/](https://platform.openai.com/).
Store the API key in a text file and pass the path to the file as an argument to NipypeGPT.
Once you have an API key, you can run NipypeGPT with the following command:
```
run.py --api_key <path_to_api_key>
```
The script will ask you to enter the details of the image acquisition and processing methods.
These details can also be provided in text files. See the Usage section for more details.
The resulting Nipype workflow will be written to a file (default: workflow.py).
For convenience, the workflow file can be run as a script on the commandline.
You can run ```python workflow.py --help``` for more details on how to run your specific workflow.
To write the workflow file to a different location use the `--workflow_file` argument.

## Usage
```
usage: run.py [-h] [--api_key API_KEY] [--acquisition_details ACQUISITION_DETAILS] [--processing_details PROCESSING_DETAILS] [--workflow_file WORKFLOW_FILE] [--workflow_template_file WORKFLOW_TEMPLATE_FILE]

options:
  -h, --help            show this help message and exit
  --api_key API_KEY     Path to ChatGPT API key
  --acquisition_details ACQUISITION_DETAILS
                        path to txt file describing the details of the image acquisition methods. Relevant information includes the voxel size, the number of slices, slice thickness, and TR (for fMRI).
  --processing_details PROCESSING_DETAILS
                        path to txt file describing the details of the image processing methods. Relevant information includes the type of registration, the type of normalization, the type of smoothing, and
                        any templates and atlases used.
  --workflow_file WORKFLOW_FILE
                        path to the file where the workflow will be written.
  --workflow_template_file WORKFLOW_TEMPLATE_FILE
                        path to the file where the workflow template is stored. This file will describe what the output workflow file should look like.
```

## How it works
Text2Nipype takes the text description from the user along with a template nipype workflow.
These are both passed to ChatGPT which modifies the template workflow to do the processing
steps described in the text description.

## Contributing
Feel free to play around with different variations of template workflows or
different ways of asking ChatGPT to create Nipype workflows.
I'm always open to contributions and or suggestions!
