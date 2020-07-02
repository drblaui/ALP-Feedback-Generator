# -*- coding: utf-8 -*-
#Umlauts actually wont work

#["Group1, Group2, ..., GroupN"]
#"Group1" = "Name1, Name2, ..., Name3" of the students that work together
names = [YOUR STUDENT NAMES HERE]

def makefile(names, nr, assignments, filename):
	#Create TextFile
	file = open(filename + ".txt", "w")
	file.write("Feedback fuer Blatt " + nr + "\n \n")
  #Create Numbers for every Group
	for name in names:
		file.write(name + "\n")
		maxAmount = 0
		for assignment in assignments:
			maxAmount += assignments[assignment]
			file.write(assignment + ": /" + str(assignments[assignment]) + "\n")
		file.write("Gesamt: /" + str(maxAmount) + "\n")
		file.write("\n")
	file.close()
	print("Generated Feedback")

def askForAssignments():
	nrOfAssignments = int(input("Wie viele Aufgaben gibt es? \n"))
	assList = {}
	for i in range(1, nrOfAssignments + 1):
		assList["A" + str(i)] = int(input("Wie viele Punkte hat Aufgabe " + str(i) + "?\n"))
	return assList


if __name__ == "__main__":
	filename = input("Wie soll die Ausgabedatei heißen? (bitte ohne Dateiendung angeben)\n")
	assignmentNr = input("Das wie vielte Arbeitsblatt ist es? \n")
	assignments = askForAssignments()
	makefile(names, assignmentNr, assignments, filename)
