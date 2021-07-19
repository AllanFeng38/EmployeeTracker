import mysql.connector


class Create_Database:
   def __init__(self):
      self.connector=mysql.connector.connect(host="localhost",user="root",password="Kaed3xod!")
      query='create database if not exists p1p1'
      current_connector =self.connector.cursor()
      current_connector.execute(query)
      print("\n successfully connected to database")

#create database instance
employee_database = Create_Database()



while True:
    print("\n1.add new employee")
    print ("\n2.View employee record")
    print("\n3.add and view dependent")
    print("\n4.view dependents")
    print("\n5.update employee")
    print("\n6.remove dependent")
    print("\n7.remove employee")
    option = int(input("\nenter your choice="))
    if option == 1:
        connection = mysql.connector.connect(host="localhost", user="root", password="Kaed3xod!", database="p1p1")
        my_cursor = connection.cursor()
        FNAME = input("\n enter first name of employee = ")
        LNAME = input("\n enter last name of employee = ")
        MINIT = input("\n enter MINIT = ")
        SSN = input("\n enter SSN = ")
        BDATE = input("\n enter BDATE YYYY-MM-DD = ")
        ADDRESS = input("\n enter ADDRESS = ")
        SEX = input("\n enter SEX = ")
        SALARY = input("\n SALARY = ")
        SUPER_SSN = input("\n enter SUPER_SSN = ")
        DNO= input("\n enter DNO = ")
        params = [FNAME, MINIT, LNAME, SSN, BDATE, ADDRESS, SEX, SALARY, SUPER_SSN, DNO]
        values = tuple(params)
        query = "INSERT INTO EMPLOYEE (FNAME, MINIT, LNAME, SSN, BDATE, ADDRESS, SEX, SALARY, SUPER_SSN, DNO) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        my_cursor.execute(query,params)
        connection.commit()
        print("successfully inserted")
    if option == 2:
        employee = input("enter SSN of an employee in order to view:")
        connection = mysql.connector.connect(host="localhost", user="root", password="Kaed3xod!", database="p1p1")
        my_cursor = connection.cursor(buffered=True)
        params = [employee]
        query="select * from employee"
        my_cursor.execute(query)
        result = my_cursor.fetchall()
        for row in result:
            print(row)
        connection.commit()
        query1 = "select d.dname, e.super_ssn, concat(s.fname, s.minit, s.Lname) SUPERVISOR_NAME from employee e, employee s, department d where e.super_ssn = s.ssn and e.Dno = d.dnumber and e.ssn = {}".format(employee)
        my_cursor.execute(query1)
        result1 = my_cursor.fetchall()
        print("\nhere is your supervisor and department")
        for rows in result1:
            print(rows)
        connection.commit()
    if option == 3:
        connection = mysql.connector.connect(host="localhost", user="root", password="Kaed3xod!", database="p1p1")
        my_cursor = connection.cursor()
        employee = input("enter SSN of employee you would like to see dependent of:")
        my_cursor = connection.cursor(buffered=True)
        query =  "select d.dependent_name, d.sex,d.Bdate,d.relationship from dependent d, employee e where d.essn = e.ssn and e.ssn = {}".format(employee)
        my_cursor.execute(query)
        result2 = my_cursor.fetchall()
        for dependents in result2:
            print(dependents)
        connection.commit()
        dependent_name = input("what is your new dependent name:")
        dependent_sex = input("what is the sex of your new dependent:")
        dependent_bdate = input("enter Bdate of dependent in form of YYYY-MM-DD:")
        dependent_relationship= input("enter the relationship of your new dependent:")
        query1 = "insert into dependent(essn,dependent_name,sex,bdate,relationship) values('{}','{}','{}','{}','{}')".format(employee,dependent_name,dependent_sex,dependent_bdate,dependent_relationship)
        my_cursor.execute(query1)
        connection.commit()
        print("successfully added new dependent!")
    if option == 4:
        connection = mysql.connector.connect(host="localhost", user="root", password="Kaed3xod!", database="p1p1")
        my_cursor = connection.cursor()
        employee = input("enter SSN of employee you would like to see dependent of:")
        my_cursor = connection.cursor(buffered=True)
        query = "select d.dependent_name, d.sex,d.Bdate,d.relationship from dependent d, employee e where d.essn = e.ssn and e.ssn = {}".format(
            employee)
        my_cursor.execute(query)
        result3 = my_cursor.fetchall()
        for dependent in result3:
            print(dependent)
        connection.commit()
    if option == 5:
        employee = input("enter SSN of employee to update:")
        connection = mysql.connector.connect(host="localhost", user="root", password="Kaed3xod!", database="p1p1")
        my_cursor = connection.cursor(buffered=True)
        #here i do a write lock on my employee table
        lock = "lock tables employee write"
        my_cursor.execute(lock)
        query = "select * from employee"
        my_cursor.execute(query)
        connection.commit()
        result = my_cursor.fetchall()
        print("here are all the current employees")
        for employees in result:
            print(employees)
        #unlock write lock
        unlock = "unlock tables"
        my_cursor.execute(unlock)
        connection.commit()
        address = input ("\n enter address: ")
        sex = input("\n enter sex = ")
        salary = input("\n enter salary = ")
        super_ssn = input("\n enter super_ssn = ")
        Dno = input("\n enter Dno = ")
        update = "update employee set address ='{}', sex = '{}', salary ='{}', super_ssn = '{}',Dno ='{}' where ssn = {}".format(address, sex, salary, super_ssn, Dno, employee)
        my_cursor.execute(update)
        connection.commit()
        print(" employee user information successfully updated!")
    if option == 6:
        connection = mysql.connector.connect(host="localhost", user="root", password="Kaed3xod!", database="p1p1")
        my_cursor = connection.cursor(buffered=True)
        employee = input("enter SSN of employee:")
        dependent_lock = "lock tables dependent write"
        employee_lock = "lock tables employee write"
        unlock = "unlock tables"
        my_cursor.execute(dependent_lock)
        connection.commit()
        my_cursor.execute(employee_lock)
        connection.commit()
        print("tables are locked")
        print("unlocking tables")
        my_cursor.execute(unlock)
        connection.commit()
        print("here are the employee's current dependents")
        dependent_query = "select d.dependent_name, d.sex,d.Bdate,d.relationship from dependent d, employee e where d.essn = e.ssn and e.ssn = {}".format(employee)
        my_cursor.execute(dependent_query)
        connection.commit()
        result_dependents = my_cursor.fetchall()
        for dependents_resulted in result_dependents:
            print(dependents_resulted)
        remove_dependent = input("which dependent would you like to remove?:")
        remove_query = "delete from dependent where dependent_name = '{}'".format(remove_dependent)
        my_cursor.execute(remove_query)
        connection.commit()
        print("dependent successfully removed")
    if option == 7:
        connection = mysql.connector.connect(host="localhost", user="root", password="Kaed3xod!", database="p1p1")
        my_cursor = connection.cursor(buffered=True)
        employee = input("enter SSN of employee:")
        view_query = "select * from employee where ssn = {}".format(employee)
        employee_lock = "lock tables employee write"
        unlock = "unlock tables"
        my_cursor.execute(employee_lock)
        connection.commit()
        print("tables are locked")
        print("here are the dependent records")
        my_cursor.execute(unlock)
        connection.commit()
        dependent_query = "select d.dependent_name, d.sex,d.Bdate,d.relationship from dependent d, employee e where d.essn = e.ssn and e.ssn = {}".format(
            employee)
        my_cursor.execute(dependent_query)
        connection.commit()
        result_dependents = my_cursor.fetchall()
        for dependents_resulted in result_dependents:
            print(dependents_resulted)
        ask_delete = input("would you like to delete dependents? (Y/N)")
        if ask_delete == "Y":
            delete_dependents = "delete from dependent where essn = '{}'".format(employee)
            my_cursor.execute(delete_dependents)
            connection.commit()
            print("dependents deleted!")
            print("make sure there are no more dependents")
            key_check = "SET FOREIGN_KEY_CHECKS=0"
            my_cursor.execute(key_check)
            connection.commit()
            print("removing employee now")
            delete_employee = "delete from employee where ssn = '{}'".format(employee)
            my_cursor.execute(delete_employee)
            connection.commit()
        else:
            print("okay returning to menu")
            continue