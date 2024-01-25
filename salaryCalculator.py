"""
Program: salaryCalculator.py
Chapter 8 Practice
1/18/2024

**NOTE: the module breezypythonygui.py MUST be in the same directory as this file for the app to run correctly!

GUI-based version of the salary calculator app which calculates an employee's earning.
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports go here

# Class header (class name will change project to project)
class SalaryCalculator(EasyFrame):

	# Definition of our classes constructor method
	def __init__(self):
		# Call to the Easy Frame class constructor
		EasyFrame.__init__(self, title = "Salary Calculator", background = "lightgreen")

		# Variable to store a font design for multiple labels
		labelFont = Font(family = "Georgia", size = 14)

		# Label and entry field
		self.label = self.addLabel(text = "Salary Calculator", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "lightgreen", font = Font(family = "Impact", size = 22))
		self.addLabel(text = "Hourly Wage:", row = 1, column = 0, background = "lightgreen", font = labelFont)
		self.wageField = self.addFloatField(value = 0.0, row = 1, column = 1, width = 10)
		self.addLabel(text = "# of Hours Worked:", row = 2, column = 0, background = "lightgreen", font = labelFont)
		self.hoursField = self.addIntegerField(value = 0, row = 2, column = 1, width = 10)
		self.hoursField["background"] = "khaki1"
		self.wageField["background"] = "khaki1"

		# Add button
		self.button = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		self.button["background"] = "palegoldenrod"
		self.button["width"] = 15

		# Label for Calculation for employee's salary
		self.outputLabel =self.addLabel(text = "", row = 4, column = 0, background = "lightgreen", font = labelFont, sticky = "NSEW", columnspan = 2)
		#self.outputField = self.addFloatField(value = 0.0, row = 4, column = 1, state = "readonly", width = 10, precision = 2)

	# Definition of the compute() function which is the event handler
	def compute(self):
		wage = self.wageField.getNumber()
		hours = self.hoursField.getNumber()
		salary = wage * hours
		self.outputLabel["text"] = "The employee's salary is: $%0.2f" % salary

# Global definition of the main() method
def main():
	# Instantiate an object from the class into mainloop()
	SalaryCalculator().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()