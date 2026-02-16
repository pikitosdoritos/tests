def recurse(str):
    print(str[0])
    if len(str) > 1:
        recurse(str[1:])
        
recurse("Hello")

import random
