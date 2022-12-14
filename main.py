import os
import re
my_dir = os.path.expanduser("~")

list_of_stripped_tests = [re.sub(r"['$&+,:;=?@#|<>.^*()%!-]", "", i.split('.')[0]).lower() for i in os.listdir('../../Work/pip-frontend/src/main/views')]
list_of_stripped_mains = [re.sub(r"[$&+,:;=?@#|'<>.^*()%!-]", "", i.split('.')[0]).lower() for i in os.listdir('../../Work/pip-frontend/src/test/unit/views')]

x = {i : i in list_of_stripped_tests for i in list_of_stripped_mains}

for k, v in x.items():
    print(k, v)