import mysql.connector
import tkinter as tk

connection1 = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Spiderman.55'
)
myCursor=connection1.cursor()
myCursor.execute("CREATE DATABASE IF NOT EXISTS MarvelInformations")

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Spiderman.55',
    database='MarvelInfo'
)
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movies(
                  ID int(3) NOT NULL,
                  Movie varchar(80) NOT NULL,
                  DateInfo varchar(50) NOT NULL,
                  Mcu_Phase varchar(20))''')

#1
with open('marvel.txt', 'r') as file:
    next(file)
    for line in file:
        line = line.strip()
        data = line.split('\t')

        movie_id = int(data[0])
        movieTitle = data[1]
        releaseDate = data[2]
        mcuPhase = data[3]

        #2
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Spiderman.55',
            database='MarvelInfo'
        )
        cursor = connection.cursor()

        # Task 3
        insertQuery = """
            INSERT INTO movies (ID, Movie, DateInfo, Mcu_Phase)
            VALUES (%s, %s, %s, %s)
        """
        values = (movie_id, movieTitle, releaseDate, mcuPhase)
        cursor.execute(insertQuery, values)

        connection.commit()
        cursor.close()
        connection.close()

#4
master = tk.Tk()
master.title(' Marvel Movies Database')

#5
def on_dropdown_select(event):
    selected_id = dropdown_var.get()
    textBox.delete('1.0', tk.END)
    textBox.insert(tk.END, f"Selected ID: {selected_id}")

labelDropdown = tk.Label(master, text='Select ID:')
labelDropdown.pack()

dropdown_var = tk.StringVar(master)
dropdown = tk.OptionMenu(master, dropdown_var, *range(1, 100), command=on_dropdown_select)
dropdown.pack()

# 6
def add_entry():
    entryMaster = tk.Toplevel()
    entryMaster.title('Add Entry')

buttonAdd = tk.Button(master, text='Add', command=add_entry)
buttonAdd.pack()

#  7
def listAllEntries():
    textBox.delete('1.0', tk.END)

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Spiderman.55',
        database='MarvelInfo'
    )
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()

    for row in rows:
        entry = f"ID: {row[0]}\n"
        entry += f"Movie: {row[1]}\n"
        entry += f"Date: {row[2]}\n"
        entry += f"MCU Phase: {row[3]}\n\n"
        textBox.insert(tk.END, entry)

    cursor.close()
    connection.close()

buttonListAll = tk.Button(master, text='LIST ALL', command=listAllEntries)
buttonListAll.pack()

textBox = tk.Text(master)
textBox.pack()

master.mainloop()