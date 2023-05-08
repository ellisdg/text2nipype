#!/usr/bin/env python
import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api_key", type=str, default="/Users/david.ellis/.openai_api_key.txt",
                        help="Path to ChatGPT API key")
    parser.add_argument("--acquisition_details", type=str, default=None,
                        help="path to txt file describing the details of the image acquisition methods. "
                             "Relevant information includes the voxel size, the number of slices, slice thickness, "
                             "and TR (for fMRI).")
    parser.add_argument("--processing_details", type=str, default=None,
                        help="path to txt file describing the details of the image processing methods. "
                             "Relevant information includes the type of registration, the type of normalization, "
                             "the type of smoothing, and any templates and atlases used.")
    parser.add_argument("--workflow_file", type=str, default="workflow.py",
                        help="path to the file where the workflow will be written.")
    parser.add_argument("--response_file", type=str, default="response.json")
    parser.add_argument("--workflow_template_file", type=str,
                        default=os.path.join(os.path.abspath(os.path.dirname(__file__)), "template_workflow.py"),
                        help="path to the file where the workflow template is stored. This file will describe what "
                             "the output workflow file should look like.")
    return parser.parse_args()


def read_api_key(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return f.read().strip()
    else:
        print("Please provide a ChatGPT API key:")
        return input()


def read_acquisition_details(path=None):
    if path:
        with open(path, "r") as f:
            return f.read().strip()
    else:
        print("Please provide acquisition details. Relevant information includes the voxel size, the number of slices, "
              "slice thickness, and TR (for fMRI):")
        return input()


def read_processing_details(path=None):
    if path:
        with open(path, "r") as f:
            return f.read().strip()
    else:
        print("Please provide processing details. Relevant information includes the type of registration, the type of "
              "normalization, the type of smoothing, and any templates and atlases used:")
        return input()


def ask_chat_gpt(api_key, acquisition_details, processing_details, template_workflow):
    import requests
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": "Bearer {api_key}".format(api_key=api_key)}
    payload = {"model": "gpt-3.5-turbo",
               "messages": [{"role": "user",
                             "content": "Write for me a Nipype workflow that will process my data. "
                                        "My acquisition details are:\n "
                                        "{acquisition_details}.\n"
                                        "My processing details are:\n "
                                        "{processing_details}.\n"
                                        "The workflow should look something like this:\n"
                                        "```{template_workflow}```\n"
                                        "Output only the code for the whole file.".format(
                                 acquisition_details=acquisition_details,
                                 processing_details=processing_details,
                                 template_workflow=template_workflow)}],
               "temperature": 0
               }
    print("Sending request to ChatGPT...")
    response = requests.post(url, headers=headers, json=payload)
    return response.json()


def parse_response(response):
    code = list()
    for chunk in response["choices"][0]["message"]["content"].split("```")[1::2]:
        code.append(chunk)
    return "".join(code).strip()


def write_workflow_file(code, path):
    with open(path, "w") as f:
        f.write(code)


def read_workflow_template(path):
    with open(path, "r") as f:
        return f.read()


def write_json(response, path):
    import json
    with open(path, "w") as f:
        json.dump(response, f)


def main():
    args = parse_args()
    api_key = read_api_key(os.path.abspath(args.api_key))
    acquisition_details = read_acquisition_details(args.acquisition_details)
    processing_details = read_processing_details(args.processing_details)
    template_workflow = read_workflow_template(args.workflow_template_file)
    response = ask_chat_gpt(api_key, acquisition_details, processing_details,
                            template_workflow)
    write_json(response, args.response_file)
    code = parse_response(response)
    write_workflow_file(code, args.workflow_file)


if __name__ == "__main__":
    main()
