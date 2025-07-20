from datasets import load_dataset
import random

# convert dataset to format that can be used by langchain
def convert_dataset(x):
    return {"instruction": x["human_language"], "output": x["expected"]}

netconfeval_ds = load_dataset("NetConfEval/NetConfEval", "Formal Specification Translation")
netconfeval_ds = netconfeval_ds['train'].filter(lambda x: x["batch_size"] <= 10).map(convert_dataset).train_test_split(test_size=0.5, seed=42)
trainset = netconfeval_ds['train']
testset = netconfeval_ds['test']
print("\n\n==========\n\n")
print(trainset[0])


# The 'human_language' and 'instruction' columns have identical values for every sample in the train set.
# The 'human_language' and 'instruction' columns have identical values for every sample in the test set.

# The 'expected' and 'output' columns have identical values for every sample in the train set.
# The 'expected' and 'output' columns have identical values for every sample in the test set.

#print("The 'description' column has the same value for all samples in the train set.")

# Function to print random samples
# def print_random_samples(dataset, dataset_name, num_samples=5):
#     print(f"\nRandom {num_samples} samples from {dataset_name}:")
#     indices = random.sample(range(len(dataset)), num_samples)
#     for idx in indices:
#         sample = dataset[idx]
#         print(f"Index: {idx}, \nInstruction:\n {sample['instruction']}, \nOutput:\n\n {sample['output']}")

# # Print 5 random samples from trainset and testset
# print_random_samples(trainset, "Trainset")
# print_random_samples(testset, "Testset")


# import json

# def print_json_formatted(input_string):
#     try:
#         # Convert the string into a Python dictionary
#         data = eval(input_string)  # Use `eval` to parse the string into a Python dictionary
#         if isinstance(data, dict):  # Ensure it's a dictionary
#             # Print the dictionary as a JSON-formatted string
#             print(json.dumps(data, indent=4))
#         else:
#             print("Input is not a valid dictionary.")
#     except Exception as e:
#         print(f"Error parsing input string: {e}")


# import torch
# print(torch.__version__)
# print(torch.version.cuda)

# print("\nInput:\n")
# single_query = "100.0.13.0/24 is accessible from roma. Traffic originating from vienna can reach the subnet 100.0.24.0/24."
# print(single_query)   


# print("\nOutput:\n")
# estring = """{"reachability": {"roma": ["100.0.13.0/24"], "vienna": ["100.0.24.0/24"]}, "waypoint": {}, "loadbalancing": {}}"""
# print_json_formatted(estring)      