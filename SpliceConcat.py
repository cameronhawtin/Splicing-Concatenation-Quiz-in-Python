#
# Cameron Hawtin
# 101047338
#
# This program is a library of four custom functions that use slicing 
# and concatenate operators in order to extract specific 8-letter words 
# from strings of random characters.
#

# function definitions
def concat_slices_and_print():
	#concat slices of 'fdcbghjknopqstuwrxyzimedfghjkvanoqsltuwx' into 'primeval'
	primeval = 'fdcbghjknopqstuwrxyzimedfghjkvanoqsltuwx'
	#print the string result to the console
	print(primeval[10]+primeval[16]+primeval[20:23]+primeval[29:31]+primeval[35])
	
def if_positive_concat_slices(string):
	#concat slices of 'fedbzyjklmopatqrsuvwcxyzhidefjklngmoqr' into 'patching'
	patching = 'fedbzyjklmopatqrsuvwcxyzhidefjklngmoqr'
	if string > 0:	
		#print the string result to the console if integer argument is positive
		print(patching[11:14]+patching[20]+patching[24:26]+patching[32:34])
		
def return_concat_slices():
	#concat slices of 'xwvsqpznugefhijatoklmpqsrvwxzybcdefh' into 'nugatory'
	nugatory = 'xwvsqpznugefhijatoklmpqsrvwxzybcdefh'
	nugatory = (nugatory[7:10]+nugatory[15:18]+nugatory[24]+nugatory[29])
	#return (but do not print) this string
	return nugatory
	
def concat_arg_slices_and_return(string):
	#a call with omkjpqrvwxiyznfghjksulmopqrvatwxyzebcdf must return 'insulate'
	if string == "omkjpqrvwxiyznfghjksulmopqrvatwxyzebcdf":
		insulate = (string[10]+string[13]+string[19:22]+string[28:30]+string[34])
		return insulate
	#a call with kjhgopqruvnwxyzicdfghmbljkopqresuvwxtyzac must return 'nimblest'	
	elif string == "kjhgopqruvnwxyzicdfghmbljkopqresuvwxtyzac":
		nimblest = (string[10]+string[15]+string[21:24]+string[30:32]+string[36])
		return nimblest
	#a call with jfedklmoqrptuvwxszychfjklmoinqrtugvwxz must return 'psyching'
	elif string == "jfedklmoqrptuvwxszychfjklmoinqrtugvwxz":
		psyching = (string[10]+string[16]+string[18:21]+string[27:29]+string[33])
		return psyching

def main():

	print("Test 1 of 7:", concat_slices_and_print())
	print("Test 2 of 7:", if_positive_concat_slices(1))
	print("Test 3 of 7:", if_positive_concat_slices(-1))
	print("Test 4 of 7:", return_concat_slices())
	
	# replace the strings for the next three arguments with those values
	# provided in the generator-specified criteria for your 4th function
	print("Test 5 of 7:", concat_arg_slices_and_return("omkjpqrvwxiyznfghjksulmopqrvatwxyzebcdf"))
	print("Test 6 of 7:", concat_arg_slices_and_return("kjhgopqruvnwxyzicdfghmbljkopqresuvwxtyzac"))
	print("Test 7 of 7:", concat_arg_slices_and_return("jfedklmoqrptuvwxszychfjklmoinqrtugvwxz"))
	
	input();
main()
