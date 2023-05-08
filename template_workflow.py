import nipype.interfaces.utility as util
import nipype.pipeline.engine as pe


# create the workflow
def create_workflow(input, files, go, here, name="VeryHelpfulWorkflowNameGoesHere"):
    # Be sure to change the input arguments to match the input arguments of your workflow

    workflow = pe.Workflow(name=name)

    # create the input node
    # Be sure to change the fields to match the input arguments of your workflow
    input_node = pe.Node(util.IdentityInterface(fields=["input", "files", "go", "here"]),
                         name="input_node")
    input_node.inputs.input = input
    input_node.inputs.files = files
    input_node.inputs.go = go
    input_node.inputs.here = here

    # workflow details go here

    # create the output node
    # Be sure to change the fields to match the output arguments of your workflow
    output_node = pe.Node(util.IdentityInterface(fields=["output", "files", "go", "here"]),
                          name="output_node")

    # connections go here

    return workflow


def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    # Be sure to change the arguments to match the input arguments of your workflow
    parser.add_argument("--input", help="Input")
    parser.add_argument("--files", help="Files")
    parser.add_argument("--go", help="Go")
    parser.add_argument("--here", help="Here")
    return parser.parse_args()


def main():
    args = parse_args()
    workflow = create_workflow(args.input, args.files, args.go, args.here)
    # Connect the inputs to the input node of the workflow

    # run the workflow
    workflow.run()


if __name__ == "__main__":
    main()
