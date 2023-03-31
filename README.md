Vaccination Tracker
![img.png](img.png)
Vaccination Tracker is a web application built using Django
web framework that allows parents to keep track of their children's
vaccination history and any related complications.
The application allows parents to register and add their children to 
their account, track each vaccination administered to their child, and 
log any complications that may arise after vaccination.
Models
The Vaccination Tracker application has four main models:

Parent - stores user account information of the parent.
Child - stores the personal information of each child such as first and last name,
gender, birth date, and a foreign key to the Parent model.
Vaccine - stores the information related to each vaccine, including
the vaccine name, the number of doses required, and the age in days for the first dose.
Vaccination - tracks each instance of a vaccine administered to a child, including
the vaccine, the child receiving the vaccine, the date of administration,
and the vaccination status.
Complication - stores information related to any complications that may arise
after vaccination, including a description of the complication, the date of occurrence,
and a foreign key to the Vaccination model.
