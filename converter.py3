import sys
import logging
import simplejson
from ruamel import yaml

logger = logging.getLogger('converterLogger')

def main():
    fileName = sys.argv[1].split(".")[0]
    with open(sys.argv[1], 'r') as f:
        contents = f.read()

    if ((sys.argv[1])[-4:]) == 'yaml' or ((sys.argv[1])[-3:]) == 'yml':
        convertYamltoJson(contents, fileName)
    elif ((sys.argv[1])[-4:]) == 'json':
        convertJsonToYaml(contents, fileName)
    else:
        logger.error('Invalid input file, please use yaml or json')

def convertYamltoJson(contents, fileName):
    print('-------Converting your yaml file to json.-------')

    with open(fileName + ".json", "w") as text_file:
        print(yaml.safe_load(contents), file=text_file)

    print('Conversion Complete!\n' + fileName + '.json is outputted.')

def convertJsonToYaml(contents, fileName):
    print('-------Converting your json file to yaml.-------')
    with open(fileName + ".yaml", "w") as text_file:
        print(yaml.dump(simplejson.loads(str(contents)), default_flow_style=False), file=text_file)
    print('Conversion Complete!\n' + fileName + '.yaml is outputted.')

main()

# print(contents)
