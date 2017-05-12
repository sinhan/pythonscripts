import yaml
with open('employee.yaml', 'r') as f:
    doc = yaml.load(f)
txt = doc["martin"]["name"]
print txt


