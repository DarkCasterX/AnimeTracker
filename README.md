# AnimeTrack.py
## A python application to help you keep track of any anime you're watching

This requires previous setup of an empty MySQL database and table, this application will ask for your MySQL credentials.

This is a Python application that uses the MySQL api to connect to a local database which will store the data about the anime you are watching, such as the season and episode. It has various commands:

* Check: check the status of a single anime
* Print: Print all the data for all the anime in the database
* Add: Add an anime to the database
* Remove: Remove an anime from the database
* Update: Update the records for one of the anime in the database
* Interactive: An interactive mode that lets you enter commands in sequence without quitting

After you're done with all you activities in interactive mode, you have an option to either quit, or quit and save. Quitting will not commit any changes to the database, but quitting and saving will commit all changes to the database before exiting. The reason being just in case you mess something up in interactive mode, you have the option to quit and undo all the changes you made.
