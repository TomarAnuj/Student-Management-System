# Student-Management-System

### Library used-
```
1. Tkinter
2. SQlite
```

#### Tkinter code sample

```
root = tk.Tk()

root.title("Management System")

appLabel = tk.Label(root, text="Management System", width = 20)
appLabel.config(font=("Sylfaen",30))
appLabel.pack(padx=(20,20),pady=(30,10))
```

####Sqlite

```
create_table_query = " CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + EMP_ID + \
                    " INTEGER PRIMARY KEY AUTOINCREMENT, " + EMP_NAME + " TEXT, " + \
                    EMP_ADDRESS + " TEXT, " + EMP_phone + " INTEGER );"

connection.execute(create_table_query)
```

####Screeshots
#### 1.Homepage
![alt home](https://github.com/TomarAnuj/Student-Management-System/blob/master/Home.png)

#### 2.Display Records
![alt Display](https://github.com/TomarAnuj/Student-Management-System/blob/master/displayMessage.png)
