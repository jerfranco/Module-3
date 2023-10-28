import mysql.connector

# Connect to my database
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='DowH@tsR1ghT',
    database='Vehicledatabase'
)
# dictionary=True display the column name with its perspective value
cursor = connection.cursor(dictionary=True)

# Menu
def display_menu():
    print("Welcome to the Vehicle Database!")
    print("Choose an option below")
    print("1. Find the car brand")
    print("2. Find the car make")
    print("3. Display all of the cars")
    print("4. Add a car")
    print("5. View specifications")
    print("6. Quit")
    
# Makes sure no duplicate make_id
def is_make_id_exists(make_id):
    query = "SELECT * FROM make WHERE make_id = %s"
    cursor.execute(query, (make_id,))
    result = cursor.fetchone()
    return result is not None

# Makes sure no duplicate specifications_id
def specification_id_exists(specifications_id):
    query = "SELECT * FROM specifications WHERE specifications_id = %s"
    cursor.execute(query, (specifications_id,))
    result = cursor.fetchone()
    return result is not None


# Makes sure no duplicate model_id
def model_id_exists(model_id):
    query = "SELECT * FROM model WHERE model_id = %s"
    cursor.execute(query, (model_id,))
    result = cursor.fetchone()
    return result is not None

# When the user chooses an option, it will display one of the 5 options below
def perform_action(option):
    
    # Displays all of the brands in the database
    if option == "1":
        brand = input("What brand do you want to see?")
        query = "SELECT model_id, modelName, country FROM model WHERE modelName = %s"
        cursor.execute(query, (brand,))
        results = cursor.fetchall()
        if results:
            print(f"Details for {brand}")
            for row in results:
                print(row)
    
    # Displays the make of a vehicle
    elif option == "2":
        make = input("What make do you want to see? ")

        query = """SELECT m.model_id, m.modelName, m.country, k.makeName,
            k.makeYear FROM model m JOIN make k ON m.make_make_id = k.make_id
                WHERE makeName = %s;"""
        cursor.execute(query, (make,))
        results = cursor.fetchall()
        if results:
            print(f"Details for {make}")
            for row in results:
                print(row)
        else:
            print(f"No information found for {make}")
    
    # Displays all of the cars the model and make of the vehicle
    elif option == "3":
        query = """SELECT m.model_id, m.modelName, m.country, k.makeName, k.makeYear
            FROM model m JOIN make k
            ON m.make_make_id = k.make_id;"""
        query1 = """SELECT modelName, COUNT(model_id) AS "amount"
            FROM model
            GROUP BY modelName;"""
        cursor.execute(query)
        results = cursor.fetchall()
        print("\nAll cars:")
        for row in results:
            print(row)
        cursor.execute(query1)
        results1 = cursor.fetchall()
        print("\nAmount of cars in each brand: ")
        for row in results1:
            print(row)
            
    # Create a car
    elif option == "4":
        print("Please remember your make_id and the specifications_id")
        make_id = input("What is the make_id? ")
        if is_make_id_exists(make_id):
            print("Invalid")
        else:
            makeName = input("What is the make name? ")
            makeYear = input("What is the make year? ")
            color = input("What is the color of the car? ")
            makesql = """INSERT INTO make (make_id, makeName, makeYear, makeColor) 
            VALUES (%s, %s, %s, %s)"""
            makevalues = (make_id, makeName, makeYear, color)
            cursor.execute(makesql, makevalues)
            connection.commit()
            print(cursor.rowcount, "record inserted.")
        specifications_id = input("What is the specifications_id? ")
        if specification_id_exists(specifications_id):
            print("Invalid")
        else:
            horsepower = input("What is the horsepower? ")
            torque = input("What is the torque? ")
            mpg = input("What is the mpg")
            specificationssql = """INSERT INTO specifications (specifications_id, horsepower, torque, mpg) 
            VALUES (%s, %s, %s, %s)"""
            specificationsvalues = (specifications_id, horsepower, torque, mpg)
            cursor.execute(specificationssql, specificationsvalues)
            connection.commit()
            print(cursor.rowcount, "record inserted. ")
        model_id = input("What is the model_id")
        if model_id_exists(model_id):
            print("Invalid")
        else:
            modelName = input("What is the model name? ")
            country = input("What is the country origin of the brand? ")
            modelsql = """INSERT INTO model (model_id, modelName, country, specifications_specifications_id, make_make_id) 
            VALUES (%s, %s, %s, %s, %s)"""
            modelvalues = (model_id, modelName, country, specifications_id, make_id)
            cursor.execute(modelsql, modelvalues)
            connection.commit()
            print(cursor.rowcount, "record inserted. ")
            
    # Choose a specifications_id to see its specs
    elif option == "5":
        query1 = """SELECT m.modelName, k.makeName, s.specifications_id
            FROM model m
            JOIN make k
            ON m.make_make_id = k.make_id
            JOIN specifications s
            ON m.specifications_specifications_id = s.specifications_id;"""
        cursor.execute(query1)
        results1 = cursor.fetchall()
        for row in results1:
            print(row)
        choice = input("Choose a specifications_id to see the specs: ")
        query2 = """SELECT m.modelName, k.makeName, s.horsepower, s.torque, s.mpg
            FROM specifications s
            JOIN model m
            ON m.specifications_specifications_id = s.specifications_id
            JOIN make k
            ON m.make_make_id = k.make_id
            WHERE specifications_id = %s;"""
        cursor.execute(query2, (choice,))
        results2 = cursor.fetchall()
        for row in results2:
            print(row)
    
    # Ends program
    elif option == "6":
        print("Goodbye")
    else:
        print("Invalid option. Please choose again.")
        

# Runs to program
def main():
    option = ""
    while option != "6":
        display_menu()
        option = input("Enter your choice: ")
        perform_action(option)

if __name__ == "__main__":
    main()
