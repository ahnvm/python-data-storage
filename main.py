import os
import json
import database

def main():
    os.system("cls")
    def mainMenu():
        while True:   
            while True:
                try:
                    print("There is the database list: ")
                    i = 1
                    for item in os.listdir("database/"):
                        print(f"{i} ==> {item.replace('.json', '')}")
                        i+=1
                    print("0 ==> Exit")
                    dbSelection = int(input("Select a database with number ==> "))
                    if dbSelection > i-1:
                        os.system("cls")
                        print("Invalid Input")
                    else:
                        break
                except:
                    os.system("cls")
                    print("Invalid Input")
            if dbSelection == 0:
                os.system("cls")
                break
            else:
                os.system("cls")
                print("Selected database is  ==> ",os.listdir("database/")[dbSelection-1].replace(".json",""))
                dataMenu(filepath= "database/"+os.listdir("database/")[dbSelection-1])

    def dataMenu(filepath):
        while True:
            print("1-)Data operations")
            print("2-)Add new data")
            print("0-)Exit")
            try:
                selection = int(input("Select an action ==> "))
                if (selection == 0):
                    os.system("cls")
                    break
                elif(selection == 1):
                    os.system("cls")
                    all_data = database.findpos(filepath)
                    for item in all_data:
                        print(f'{item["id"]}-) {item["name"]}')
                        lastid = item["id"]
                    print("0-) Exit")
                    try:
                        datapos = int(input("Select data ==> "))
                        if datapos == 0:
                            os.system("cls")
                            continue
                        if(datapos > lastid or datapos < 1):
                            os.system("cls")
                            print("Invalid Input")
                        else:
                            os.system("cls")
                            dataOperationsMenu(filepath = filepath, datapos = datapos)
                    except:
                        os.system("cls")
                        print("Invalid Input")
                elif(selection == 2):
                    os.system("cls")
                    dataAddMenu(filepath)
                else:
                    os.system("cls")
                    print("Invalid Input")

            except:
                print("Invalid Input")
            
    def dataOperationsMenu(filepath, datapos):
        data = database.read(filepath,datapos)
        while True:
            print(f"Data Header ==> {data['name']}")
            print("1-) Read Content")
            print("2-) Update Content")
            print("3-) Delete All Data Here")
            print("0-) Exit")
            try:
                selection = int(input("Select an action ==> "))
                if selection == 0:
                    os.system("cls")
                    break
                elif selection == 1:
                    print(data["content"])
                    input("\nPress enter to continue")
                    os.system("cls")
                elif selection == 2:
                    os.system("cls")
                    dataUpdateMenu(filepath= filepath, dataPos= datapos)
                elif selection == 3:
                    os.system("cls")
                    try:
                        choice = input("Are you sure (y/n) ==> ")
                        if(choice.replace(" ", "").lower() == "y"):
                            os.system("cls")
                            delete(filepath= filepath, datapos = datapos)
                            print("Data Deleted Forever")
                        elif(choice.replace(" ", "").lower() == "n"):
                            os.system("cls")
                            print("Nothing Happened")
                        else:
                            os.system("cls")
                            print("Invalid Input")
                    except:
                        os.system("cls")
                        print("Invalid Input")
                else:
                    os.system("cls")
                    print("Invalid Input")
                    
            except:
                os.system("cls")
                print("Invalid Input")

    def dataAddMenu(filepath):
        filepath = filepath.replace("database/", "")
        print("You are working on ", filepath.replace(".json",""), " database.")
        data = {}
        data["id"] = 0
        data["name"] = " "
        data["content"] = " "
        while True:
            print("1-) Header ==> ",data["name"])
            print("2-) Content ==> ", data["content"])
            print("3-) Add Data")
            print("0-) Exit")
            try:
                selection = int(input("Select an action ===> "))
                if selection == 0:
                    os.system("cls")
                    break
                elif( selection == 1):
                    header = input("Please Enter The Title of Data ===> ")
                    if (header.strip() == ""):
                        os.system("cls")
                        print("Invalid Input")
                        continue
                    else:
                        os.system("cls")
                        data["name"] = header
                elif(selection == 2):
                    content = input("Please Enter The Content of Data ===> ")
                    if (content.strip() == ""):
                        os.system("cls")
                        print("Invalid Input")
                        continue
                    else:
                        os.system("cls")
                        data["content"] = content
                elif(selection == 3):
                    os.system("cls")
                    if(data["name"].replace(" ","") == "" or data["content"].replace(" ", "") == ""):
                        os.system("cls")
                        print("Invalid Input")
                        continue
                    else:
                        database.add(filepath= "database/"+filepath, data= data)
                    data["id"] = 0
                    data["name"] = " "
                    data["content"] = " "
                    print("You can exit now. Data created.")
                else:
                    os.system("cls")
                    print("Invalid Input")

            except:
                os.system("cls")
                print("Invalid Input")
    
    def dataUpdateMenu(filepath, dataPos):
        data = database.read(filepath= filepath, datapos= dataPos)
        while True:
            print("1-) Header ==> ",data["name"])
            print("2-) Content ==> ", data["content"])
            print("3-) Update Data")
            print("0-) Exit")
            try:
                selection = int(input("Select an action ===> "))
                if selection == 0:
                    os.system("cls")
                    break
                elif( selection == 1):
                    header = input("Please Enter The Title of Data ===> ")
                    if (header.strip() == ""):
                        os.system("cls")
                        print("Invalid Input")
                        continue
                    else:
                        os.system("cls")
                        data["name"] = header
                elif(selection == 2):
                    content = input("Please Enter The Content of Data ===> ")
                    if (content.strip() == ""):
                        os.system("cls")
                        print("Invalid Input")
                        continue
                    else:
                        os.system("cls")
                        data["content"] = content
                elif(selection == 3):
                    os.system("cls")
                    database.update(filepath= filepath, dataPos= dataPos, data= data)
                    print("Data updated successfully.")
                    data = database.read(filepath= filepath, datapos= dataPos)
                else:
                    os.system("cls")
                    print("Invalid Input")

            except:
                os.system("cls")
                print("Invalid Input")

    def delete(filepath, datapos):
        database.delete(filepath= filepath, dataPos= datapos)
    mainMenu()


if __name__ == "__main__":
    main()
