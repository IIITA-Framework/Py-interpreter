import json
import os
import urllib

data = {} # Initialising an empty Dictionary

print("Chose the language of your preference :")
print("1 NodeJs")
print("2 php")
print("3 Python")
print("Enter the number to proceed"),

# Storing a {'language':'value'} pair in the Dictionary
readInt = int(input())
if(readInt == 1) :
    data['language'] = ['Nodejs']
elif(readInt == 2) :
    data['language'] = ['php']
else :
    data['language'] = ['Python']

# Writing to the packege.json file
with open('package.json','w') as outfile:
    json.dump(data,outfile,sort_keys=False,indent=4)
# Initialise the dependencies key
data['dependencies'] = {}
# Add dependencies the user selects to package.json
print("Do you wish to install dependencies for the selected language (Recomended): Y/n"),
readStr = raw_input()
if(readStr.lower() == 'y') :
    print('Select your dependencies to be installed :')
    # If user selects NodeJs.
    # Install Modules for node.
    if(readInt == 1) :

        #Added support for downloading modules and saving it to node_modules
        dir_path = os.path.dirname(os.path.realpath(__file__))
        fullfoldername = os.path.join(dir_path, './node_modules')
        if not os.path.exists(fullfoldername):
            os.makedirs(fullfoldername)
        urllib.urlretrieve("http://github.com", 'node_modules/filename')

        # Module1
        print("node_mod1 Y/n :"),
        temp = raw_input()
        if(temp.lower() == 'y') :
            data['dependencies']['node_mod1'] = '1.1.1'
        # Module2
        print("node_mod2 Y/n :"),
        temp = raw_input()
        if(temp.lower() == 'y') :
            data['dependencies']['node_mod2'] = '3.1.1'
        # Module3
        print("node_mod3 Y/n :"),
        temp = raw_input()
        if(temp.lower() == 'y') :
            data['dependencies']['node_mod3'] = '3.2.1'
    # If user selects php.
    # Install dependencies for php.
    elif(readInt == 2):

        # Added support for downloading modules and saving it to node_modules
        dir_path = os.path.dirname(os.path.realpath(__file__))
        fullfoldername = os.path.join(dir_path, './node_modules')
        if not os.path.exists(fullfoldername):
            os.makedirs(fullfoldername)
        urllib.urlretrieve("http://github.com", 'node_modules/filename')

        # Module1
        print("php_mod1 Y/n :"),
        temp = raw_input()
        if(temp.lower() == 'y') :
            data['dependencies']['php_mod1'] = '3.1.1'
        # Module2
        print("php_mod2 Y/n :"),
        temp = raw_input()
        if(temp.lower() == 'y') :
            data['dependencies']['php_mod2'] = '3.1.1'
        # Module3
        print("php_mod3 Y/n :"),
        temp = raw_input()
        if(temp.lower() == 'y') :
            data['dependencies']['php_mod3'] = '3.1.1'
    # If user selects python.
    # Install packages for python
    else :

        # Added support for downloading modules and saving it to node_modules
        dir_path = os.path.dirname(os.path.realpath(__file__))
        fullfoldername = os.path.join(dir_path, './node_modules')
        if not os.path.exists(fullfoldername):
            os.makedirs(fullfoldername)
        urllib.urlretrieve("http://github.com", 'node_modules/filename');

        # Module1
        print("py_mod1 Y/n :"),
        temp = raw_input()
        if(temp.lower() == 'y') :
            data['dependencies']['py_mod1'] = '4.2.1'
        # Module2
        print("py_mod2 Y/n :"),
        temp = raw_input()
        if(temp.lower() == 'y') :
            data['dependencies']['py_mod2'] = '1.2.1'
        # Module3
        print("py_mod3 Y/n :"),
        temp = raw_input()
        if(temp.lower() == 'y') :
            data['dependencies']['py_mod3'] = '3.3.1'
    # Write the selected modules to the package.json file
    with open('package.json','w') as outfile:
        json.dump(data, outfile, sort_keys=False, indent=4)

    print("Selected dependencies have been added to the package.json file!")
    print("Thank You!")
else :
    # Quit without adding dependencies to the package.json file
    print("Your package.json file is created! Thank you!")
