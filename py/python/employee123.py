class Employee:

	meetings = []

	def __init__(self, fn = "", ln = ""):
		self.first_name = fn
		self.last_name = ln

	def schedule(self, meeting):
		self.meetings.append(meeting)
		