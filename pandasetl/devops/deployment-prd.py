#Assign the filename
filename = "deployment_desc.txt"
# Open file for writing
fileHandler = open(filename, "w")

# Add some text
fileHandler.write("Dummy\n")
fileHandler.write("Dummy\n")
fileHandler.write("Dummy\n")

# Close the file
fileHandler.close()

