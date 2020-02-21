#############################################################################
# Project #5
#
#Create a function that will open a file given by the user
#   Use exception handling to check if the user's file actually exists
#   Print an error message if the file doesn't exist 
#   Re-prompt if the user entered an invalid file. 
#   return the user's file 
#Create a function to read the file and return the overall United States
# MMR coverage.
#Create a function to get the minimum state coverage in the United States 
#   Create a variable that will store the minimum value.
#   Read each file line and create variables to store state and percentage
#   Use conditional statements to ignore NA values. 
#   Use conditional statement to compare the percentage to the minimum value.
#   return the minimum percentage and the corresponding state
#Create a function to get the maximum state coverage in the United States 
#   Create a variable that will store the maximum value.
#   Read each file line and create variables to store state and percentage.
#   Use conditional statements to ignore NA values.
#   Use conditional statement to compare the percentage to the maximum value.
#   return the maximum percentage and the corresponding state
#Create a function to check if a state's coverage is less than 90%.
#   Create a variable that stores 90 and read the file lines.
#   Check if state's percentages are less than 90%
#   Use conditional statements to ignore the NA value in the file.
#   If they are less than 90%, print the state and percentage coverage. 
#Create a function to write the states with coverage less than 90%
#in a new text file
#   Print the those lines in the new text files.
#Create a function to call all the previous functions. 
#   print the header. the overall coverage, and the min and max coverage
#############################################################################

def open_file():
    '''
    This function will not take any arguments. 
    In a while loop, prompt the user to enter a file name. Use exception
    handling to determine if the file can be opened. If it can,
    return the file. If it can't, print error message and re-prompt the
    user. 
    '''
    while True:
        prompt= input("Input a file name: ") #prompt user
        try:
            file= open(prompt) #check for file
            return file 
        except FileNotFoundError: #if file doesn't exist
            print("Error: file not found. Please try again.") #error message
        


def get_us_value(fp):
    '''
    This function will take a file as an argument. The function will read
    the file from the beginning and will do nothing until it reaches the end
    of the file. Return the United States MMR coverage as a float.
    '''
    fp.seek(0) #start reading file at beginning
    fp.readline() #read line
    fp.readline() #read next line
    for line in fp: #while reading the lines, do nothing
        pass
    return float(line[25:].strip()) #return the MMR coverage


        
def get_min_value_and_state(fp):
    '''
    This function takes a file as an argument. It has a variable that will 
    set the minimum value equal to a large number. The function also has 
    a variable that will store an empty string. The function will read
    each line in the file and ignore any line that has NA for the MMR coverage
    Store the state value in a variable and the percentage in a variable. 
    Create a conditional statement to check if the minimum value number is
    greater than the percentage, if it is, the new minimum value is the 
    percentage. return the minimum value and the connected state. 
    '''
    minimum_value= 77456337638  #assigned min value
    min_state= "" # empty string used to store the minimum state
    fp.seek(0) #read first line
    fp.readline() #read line
    fp.readline() #read next line
    for line in fp: #check for NA and continue to next line
        if "NA" in line:
            continue
        state= line[0:25].strip()
        percentage= float(line[25:].strip())
        if minimum_value>percentage: # check if minimum is greater than percent
            minimum_value=percentage #new assignment
            min_state= state #new assignment
    return min_state,minimum_value
        

def get_max_value_and_state(fp):
    '''This function takes a file as an argument. It has a variable that will 
    set the max value equal to a small number. The function also has 
    a variable that will store an empty string. The function will read
    each line in the file and ignore any line that has NA for the MMR coverage
    Store the state value in a variable and the percentage in a variable. 
    Create a conditional statement to check if the max value number is
    less than the percentage, if it is, the new max value is the 
    percentage. return the max value and the connected state.'''
    max_value= 0 #assigned a max value
    max_state= "" #empty string to be used to store state
    fp.seek(0) #read first line
    fp.readline() #read line
    fp.readline() #read next line
    for line in fp: #continues iteration for lines with NA
        if "NA" in line:
            continue
        state= line[0:25].strip()
        percentage= float(line[25:].strip())
        if max_value<percentage: # check if max is less than percentage
            max_value=percentage #new assignment
            max_state= state #new assignment
    return max_state,max_value

        
def display_herd_immunity(fp):
    '''This function takes a file as an argument. Create a variable
    to be equal to 90. Read each line file, ignore files with NA. The
    function checks if percentage is less than 90, if so print the state
    and percentage.'''
    print("\nStates with insufficient Measles herd immunity.")
    print("{:<25s}{:>5s}".format("State","Percent"))
    ninety_percent= 90 #set equal to 90 for comparison
    fp.seek(0) #read first line
    fp.readline() #read line
    fp.readline() #read next line
    for line in fp: #continue past lines with NA
        if "NA" in line:
            continue
        state= line[0:25].strip()
        percentage= float(line[25:].strip())
        if percentage<ninety_percent: #condition if percent is less than 90
            print("{:<25s}{:>5.1f}%".format(state,percentage)) #print results
      

def write_herd_immunity(fp):
    '''This function takes a file as an argument. This has the same exact
    procedures as display_herd_immunity but this function will write 
    the results to a new text file. '''
    herd= open("herd.txt","w") #create new text flle
    #In each print statement, set the current file equal to the outfile
    print("\nStates with insufficient Measles herd immunity.", file=herd)
    print("{:<25s}{:>5s}".format("State","Percent"), file=herd)
    ninety_percent= 90
    fp.seek(0)
    fp.readline()
    fp.readline()
    for line in fp:
        if "NA" in line:
            continue
        state= line[0:25].strip()
        percentage= float(line[25:].strip())
        if percentage<ninety_percent:
            #Writes state and percentage in herd file.
            print("{:<25s}{:>5.1f}%".format(state,percentage), file=herd)
def main():   
    '''This function does not take any arguments. This function will call
    the previous function to display the overal MMR report. '''
    fp = open_file() #calls open_file() to get a file
    header = fp.readline() #reads the header line of the file
    print(header) #print the header
    value=get_us_value(fp) #calls get_us_value() to get overall coverage
    #Calls get_min_value_and_state() to get the minimum values and states
    min_state,min_value = get_min_value_and_state(fp)
    #Calls get_max_value_and_state() to get the max values and states
    max_state,max_value= get_max_value_and_state(fp)
    #print results
    print("Overall US MMR coverage: {}%".format(value))
    print("State with minimal MMR coverage: {} {}%".format(min_state,min_value))
    print("State with maximum MMR coverage: {} {}%".format(max_state,max_value))
    #calls display_herd_immunity() to get states with percent less than 90
    display_herd_immunity(fp) 
    #calls write_herd_immunity() to write the info from display_herd_immunity
    #into herd.txt
    write_herd_immunity(fp)

#Call the function    
if __name__ == "__main__":
    main()    