#Node used in stack class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#Definition of stack class using linked list
class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]
    
    #adds new node to the top of the stack
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
        
    #throws an exception when the stack is empty, else removes the element from top of the stack
    def pop(self):
        if self.isEmpty():
            raise Exception("Cannot pop from an Empty Stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

#Function which checks if the given string is a Palindrome
def checkIfPalindromUsingStack(str):
    #Create two empty stacks
    stackOne = Stack()
    stackTwo = Stack()
    
    #Retain unmodified string
    strResult=str
    
    #Get the length of the string, will be used to pop half of the stack only
    stringLen=len(str)
    
    #Convert String to upper case to handle case sensitivity
    str=str.upper()
    
    for char in str:
        #ignore space and characters which aren't alphabets
        if not char.isalpha():
            #Reduce the length by 1 since we ' pushing this into the stack
            stringLen=stringLen-1
            continue
        stackOne.push(char)
        
    #Pop half of the characters and add to the second two
    for i in range(int(stringLen/2)):
       stackTwo.push(stackOne.pop())
       
    #Now the stackTwo has the second half of the string in original order
    #In case of the given string(excluding space and special character) length is off, pop the extra element from the first stack
    if (0!=stringLen%2):
        stackOne.pop()
    #print(stackOne)   
    #print(stackTwo)
    #Pop both the stacks at the same time and return a negative message in case there is a character mismatchp
    for i in range(int(stringLen/2)):
        if(stackOne.pop()!=stackTwo.pop()):
            return "Not a Palindrome"
           
    #Return the unmodified string since it satisfies our condition of being a Palindrome
    return strResult;

#Main Logic Starts here
outputFileWriter = open("outputPS04.txt", "w")
try:
    inputFileReader = open("inputPS04.txt", "r")
    readline=inputFileReader.read().splitlines()
    #Close the reader after reader
    inputFileReader.close()
    if(len(readline) <= 0):
        #handle the case of empty file
        outputFileWriter.write("The input file is empty, please enter any value")
    else:
        # Strips the newline character
        for line in readline:
            outputFileWriter.write(checkIfPalindromUsingStack(line))
            outputFileWriter.write("\n")

        
    #Close writer after completion of the Palindrome check
    outputFileWriter.close()

except FileNotFoundError:
    #throwsexception when the input file cannot be opened
    outputFileWriter.write("The input file was not found. Please enter the right file name & place the input file in the root folder along with the Program")

#print("Done")
