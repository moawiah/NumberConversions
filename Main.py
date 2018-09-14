import sys
import numbers
import decimal
import arabicToRoman
import romanToArabic

def checkIfRomanNumeral(numeral):
     # A function to control the Roman input of the user if it is a valid Roman Number
     numeral = numeral.upper()
     validRomanNumerals = ["M", "D", "C", "L", "X", "V", "I"]
     for letters in numeral:
        if letters not in validRomanNumerals:
            print("The value is not a valid Roman Number")
            return True

#print "This is the name of the script: ", sys.argv[0]
#print "Number of arguments: ", len(sys.argv)
#print "The arguments are: " , str(sys.argv)

num_of_arguments = len(sys.argv)
mode_of_operation = sys.argv[1]

# Check if the number of arguments is correct - otherwise guide the user to the correct usage
if num_of_arguments != 3:
	print("Error: Invalid number of arguments has been entered")
	print("USAGE: python Main.py -mode- -value-")
	exit(-1)
	
# check the mode of the operation. Pop error and exceptional messages when wron flow is detected
if mode_of_operation == "1":
	try:
		value_to_process = int(sys.argv[2])
		if (value_to_process > 0 and value_to_process <= 3999):
			# Call the Arabic To Roman script after making sure that the input is valid
			result = arabicToRoman.write_roman(value_to_process)
			print("Result in Roman is: %s" %result)
		else:
			print("Error: Please enter an integer in the specified range 1 - 3999")
			exit(-4)

	except:
		print("Exception: Enter a number between 1 and 3999 to be converted into Roman")
		exit(-3)	


elif mode_of_operation == "2":
	boolean = checkIfRomanNumeral(sys.argv[2])
	if boolean != True:
		# Call the Roman To Arabic script after making sure that the input is valid
		result = romanToArabic.roman_to_int(sys.argv[2])
		print("Result in Roman is: %s" %result)
		pass
	else:
		print("Error: Please enter a valid Roman value in the specified range I - MMMCMXCIX")
		exit(-5)
	
else:
	print("Error: Invalid mode of operation was entered")
	print("USAGE: mode of operation is either (1) or (2)")
	exit(-2)



