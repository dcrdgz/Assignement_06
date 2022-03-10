#------------------------------------------#
# Title: CDInventory.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DRodriguez, 2022-Feb-06, Modify file
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    @staticmethod
    def add_CD():
        """Function to add a new item to table
        
        Args:
            dicRow: creates dictionary
            lstTbl: adds new values to dictionary
            show_inventory: displays data
            
        Returns:
            Table showing inventory in lstTbl
        
        """
        intID, strTitle, strArtist = IO.add_CD()
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        lstTbl.append(dicRow)
        return IO.show_inventory(lstTbl)
    
    @staticmethod
    def del_CD():
        """Function to search thru table and delete CD
        
        Args:
            intRowNr: 
            blnCDRemoved:
            stTbl (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
            
        Returns:
            Table showing inventory in lstTbl
        
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        return IO.show_inventory(lstTbl)
    @staticmethod
    def write_file():
        """Function to save data
        
        Args:
            objFile: calls the text file containing CD inventory
            lstValues: row of values in 2D table
            objFile.write: writes inputted data to file
            stTbl (list of dict): 2D data structure (list of dicts) that holds the data during runtime.
            
        Returns:
            Table showing inventory in lstTbl
        
        """
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()
        return IO.show_inventory(lstTbl)

class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': data[0], 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()

    @staticmethod
    def write_file(file_name, table):
        """Writes data to the file

        Args:
            objFile: calls the text file containing CD inventory
            lstValues: row of values in 2D table
            objFile.write: writes inputted data to file
            lstTbl (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            Table of data written to file.
        """
        objFile = open(file_name, 'w')
        for row in lstTbl:
           lstValues = list(row.values())
           lstValues[0] = str(lstValues[0])
           objFile.write(','.join(lstValues) + '\n')
           objFile.close()
        return IO.show_inventory(lstTbl)


# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
    @staticmethod
    def add_CD():
        """Ask user for new ID, CD Title and Artist

          Args:
              strID: name of ID input
              strTitle: name of title input
              strArtist: name of artist input
              intID: Converts strID to integer

          Returns:
              values defined in arguments
              
          """
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        intID = int(strID)
        return intID, strTitle, strArtist

# When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)

# Start main loop
while True:
    # Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    # Process menu selection
    # Process exit first
    if strChoice == 'x':
        break
    # Load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # Add a CD
    elif strChoice == 'a':
        # Ask user for new ID, CD Title and Artist and add item to table
        DataProcessor.add_CD()
        continue  # start loop back at top.
    # Display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # Delete a CD
    elif strChoice == 'd':
        # Get Userinput for which CD to delete
        # Display Inventory to user
        IO.show_inventory(lstTbl)
        # Ask user which ID to remove
        intIDDel = int(input('Which ID woudld you like to delete? ').strip())
        # Search thru table and delete CD
        DataProcessor.del_CD()
        continue  # start loop back at top.
    # Save inventory to file
    elif strChoice == 's':
        # Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # Process choice
        if strYesNo == 'y':
            # Save data
            DataProcessor.write_file()
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    #Catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')