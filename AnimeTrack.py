from mysql.connector import connect, Error, connection
import argparse

#Before you run this code for the first time, you need to have first set up a MySQL database on your system
#This script will ask for the database/table name, as well as your MySQL credentials, which are needed to connect to the database

class AnimeDB:

    def __init__(self):
        pass
        
    def login(self):
        sql_user=input("Enter your MySQL username: ")
        self.connection = connect(
            host="localhost",
            user=sql_user,
            password=input("Enter your MySQL password: "),
            database=input("Enter the database you're using: ")
        )
        self.tableName = input("Enter the name of the table you're using: ")
        self.cursor = self.connection.cursor()

    #Diplays all the anime in the database
    def printAllAnime(self, *args, **kwargs):
        print("\nAnime on your list: ")
        self.cursor.execute("select * from " + self.tableName + ";")
        result = self.cursor.fetchall()
        for row in result:
            print("\n\t[*] " + row[0] + ", Season " + str(row[1]) + " Episode " + str(row[2]))
        print("")        

    #Check the status of one anime
    def checkAnime(self, *args, **kwargs):
        animeCheck = input("[^] Which anime do you want to check? ")
        self.cursor.execute("select * from " + self.tableName + " where name=\"" + animeCheck + "\";")
        result = self.cursor.fetchone()
        print("\n\n[***] You are on season " + str(result[1]) + " episode " + str(result[2]) + " of " + animeCheck + " [***]\n")

    #Add an anime to the database
    def addAnime(self, *args, **kwargs):
        animeAdd = input("[^] Enter the name of the anime would you like to track: ")
        animeSn = input("[^] What season are you on? ")
        animeEp = input("[^] Which episode are you currently on? ")
        self.cursor.execute("insert into " + self.tableName + "(name, season, episode) values(\"" + animeAdd + "\"," + animeSn + "," + animeEp + ");")
        self.connection.commit()

    #Update the status of an anime
    def updateAnime(self, *args, **kwargs):
        animeUpdate = input("[^] Which anime would you like to update? ")
        newSn = input("Which season are you currently on? ")
        newEpisode = input("Which episode? ")
        self.cursor.execute("update " + self.tableName + " set season=" + newSn + " where name=\"" + animeUpdate + "\";")
        self.cursor.execute("update " + self.tableName + " set episode=" + newEpisode + " where name=\"" + animeUpdate + "\";")
        print("[^] Updated Database")
        self.connection.commit()

    #Remove one anime
    def removeAnime(self, *args, **kwargs):
        animeRemove = input("Which anime would you like to remove? ")
        yesorno = input("[*] If you remove this anime, it will be gone forever.\n\tContinue? (Yes = 1; No = 0)")
        if yesorno == '1':
            self.cursor.execute("delete from " + self.tableName + " where name=\"" + animeRemove + "\";")
            print("[^] Deleted " + animeRemove)
        else:
            print("[^] Cancelled Remove")
        self.connection.commit()

    #Add an anime to the database without saving
    def addAnimeI(self, *args, **kwargs):
        animeAdd = input("[^] Enter the name of the anime would you like to track: ")
        animeSn = input("[^] What season are you on? ")
        animeEp = input("[^] Which episode are you currently on? ")
        self.cursor.execute("insert into " + self.tableName + "(name, season, episode) values(\"" + animeAdd + "\"," + animeSn + "," + animeEp + ");")

    #Update the status of an anime without saving
    def updateAnimeI(self, *args, **kwargs):
        animeUpdate = input("[^] Which anime would you like to update? ")
        newSn = input("Which season are you currently on? ")
        newEpisode = input("Which episode? ")
        self.cursor.execute("update " + self.tableName + " set season=" + newSn + " where name=\"" + animeUpdate + "\";")
        self.cursor.execute("update " + self.tableName + " set episode=" + newEpisode + " where name=\"" + animeUpdate + "\";")
        print("[^] Updated Database")

    #Remove one anime without saving
    def removeAnimeI(self, *args, **kwargs):
        animeRemove = input("Which anime would you like to remove? ")
        yesorno = input("[*] If you remove this anime, it will be gone forever.\n\tContinue? (Yes = 1; No = 0)")
        if yesorno == '1':
            self.cursor.execute("delete from " + self.tableName + " where name=\"" + animeRemove + "\";")
            print("[^] Deleted " + animeRemove)
        else:
            print("[^] Cancelled Remove")

    def exec(self, *args, **kwargs):
        try:
            while True:
                action = int(input("Options:\n\t[1] Check an anime\n\t[2] Add an anime\n\t[3] Update an anime\n\t[4] Print all anime\n\t[5] Remove an anime\n\t[6] Save\n\t [7] Quit & Save\n\t [8] Quit\nWhat would you like to do? "))
                if(action == 1):
                    self.checkAnime()
                elif(action == 2):
                    self.addAnimeI()
                elif(action == 3):
                    self.updateAnimeI()
                elif(action == 4):
                    self.printAllAnime()
                elif(action == 5):
                    self.removeAnimeI()
                elif(action == 6):
                    print("[!***] Changes saved")
                    self.connection.commit()
                elif(action == 7):
                    print("[^] Quitting and saving...")
                    self.connection.commit()
                    exit()
                elif(action == 8):
                    print("Quitting...")
                    exit()
                else:
                    print("Invalid action")
        except Error as e:
            print(e)
        except ValueError:
            print("Invalid Input")

def main():
    try:
        print("***Anime Database Tracker***\n")
        db = AnimeDB()
        commands = {'check': db.checkAnime, 'add': db.addAnime, 'print': db.printAllAnime, 'update': db.updateAnime, 'interactive': db.exec, 'remove': db.removeAnime}
        parser = argparse.ArgumentParser()
        parser.add_argument('command', choices=commands.keys(), help='Enter the command to execute {check | add | print | update | interactive | remove}')
        args = parser.parse_args()
        db.login()
        func = commands[args.command]
        func()
    except KeyboardInterrupt:
        print("\nKeyboard Interrupt detected. Exiting... [*]")
        db.connection.commit()
    except Exception as e:
        x = input("[!***] A critical error occured. Would you like to see the error output? (y/n) ")
        if(x == "y"):
            print(e)
        elif(x == "n"):
            print("Exiting...")
        else:
            exit()

if __name__ == '__main__':
    main()
