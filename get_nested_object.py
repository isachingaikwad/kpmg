import sys
import json

def get_nested_values(object, key):
    """
    Returns the nested values
    """
    result = object 
    try:
        keys = key.split("/")

        for k in keys:
            result = result[k]
    except Exception as e:
        print("Invalid Key or Object: ")
        raise e
    else:
        return result

if __name__=='__main__': 
    # Pass object and key and get back the nested value
    # object = '{"a":{"b":{"c":"d"}}}'
    # key = "a/b"
    # value = "d"
    object = json.loads(sys.argv[1])
    key = sys.argv[2] # name of filters eg instance-type
    print(get_nested_values(object, key))
    # Execute below command
    # python get_nested_object.py '{"a":{"b":{"c":"d"}}}' a/b/cs