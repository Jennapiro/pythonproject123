# import code to be tested
from employee import Employee 

#create a new instance (object) using my Employee class
Jenna = Employee(fn = "Jenna", ln = "Piromalli")

#create a Super Simple generic Object
#class from mocking object like
#Meetings 
# got from https://programmingideaswithjake.wordpress.com/2016/05/07/object-literals-in-python/
class Object:
	def __init__(self, ** attributes):
		self.__dict__.update(attributes)
mockMeeting = Object(
	time = "10",
	location = "clients office",
	client_company_name = "IBM",)
	
def test_employee_has_a_first_name():
	assert hasattr(Jenna, "first_name")
	assert Jenna.first_name == "Jenna"

def test_employee_has_a_last_name():
	assert hasattr(Jenna, "last_name")
	assert Jenna.last_name == "Piromalli"

def test_employee_has_meetings():
	assert hasattr(Jenna, "meetings")
	assert type(Jenna.meetings) is list 

def test_employee_can_schedule_a_meeting():
	num_meetings = len(Jenna.meetings)
	Jenna.schedule(mockMeeting)
	assert len(Jenna.meetings) == num_meetings + 1
	assert Jenna.meetings[num_meetings].time == "10"
	assert Jenna.meetings[num_meetings].location == "clients office"

def calc_meetings(week1, week2, week3, week4):
	average = (week1 + week2 + week3 + week4) / 4
	return average

def determine_employee_standing( number_of_meetings_per_month ):
	if( number_of_meetings_per_month < 10 ):
		return "in a bad compnay standing"
	elif( number_of_meetings_per_month < 19 ):
		return "in an average company stadning"
	elif( number_of_meetings_per_month < 30 ):
		return "in a competitive company standing"

def ask_for_number_of_meetings():
	week1 = float( input( "please enter number of meetings for week 1: " ))
	week2 = float( input( "please enter number of meetings for week 1: " ))
	week3 = float( input( "please enter number of meetings for week 1: " ))
	week4 = float( input( "please enter number of meetings for week 1: " ))

	return week1, week2, week3, week4
















	