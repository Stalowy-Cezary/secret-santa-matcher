# Secret Santa Matcher
The purpose of this project is to randomly match secret santa participants, everyone gets to be 1 santa and 1 receiver, no duplicatess!

### Dependencies

Windows 10, python 3.9.0
It's assumed list of participants will be on 1st column
### Installing

* download all files and put them in the same directory.
* Add your csv sheet to te same directory.


### Executing program

* Open terminal in the same directory and execute 'main.py'
* type in the name of your participants file

### how does that work?

* App downloads list of participants and turns them into a list
* list is then shuffled to randomize order of elements
* list prints pairs of members one after another, such as member1 + member2 -> member2 + member3 -> member3 + member4...

## issues
* As for now participants list will not launch itself automatically, you have to type in its name
* currently only csv files are supported