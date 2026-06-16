import mysql.connector

# ---------------- DATABASE CONNECTION ----------------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="MONSTER_X_YT1",
        database="student_db"
    )


# ---------------- ADD STUDENT ----------------
def add_student():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        city = input("Enter City: ")

        query = """
        INSERT INTO students (name, age, course, city)
        VALUES (%s, %s, %s, %s)
        """

        values = (name, age, course, city)
        cursor.execute(query, values)
        conn.commit()

        print("Student Added Successfully!")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


# ---------------- VIEW STUDENTS ----------------
def view_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\n----- STUDENT LIST -----")
    for row in records:
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]} | City: {row[4]}")

    conn.close()


# ---------------- SEARCH STUDENT ----------------
def search_student():
    conn = get_connection()
    cursor = conn.cursor()

    name = input("Enter Name to Search: ")

    query = "SELECT * FROM students WHERE name LIKE %s"
    cursor.execute(query, (f"%{name}%",))

    results = cursor.fetchall()

    if results:
        for row in results:
            print(row)
    else:
        print("No student found")

    conn.close()


# ---------------- UPDATE STUDENT ----------------
def update_student():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        student_id = int(input("Enter Student ID to Update: "))
        city = input("Enter New City: ")

        query = "UPDATE students SET city = %s WHERE student_id = %s"
        cursor.execute(query, (city, student_id))
        conn.commit()

        if cursor.rowcount > 0:
            print("Student Updated Successfully!")
        else:
            print("Student ID not found")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


# ---------------- DELETE STUDENT ----------------
def delete_student():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        student_id = int(input("Enter Student ID to Delete: "))

        query = "DELETE FROM students WHERE student_id = %s"
        cursor.execute(query, (student_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print("Student Deleted Successfully!")
        else:
            print("Student ID not found")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


# ---------------- MAIN MENU ----------------
def menu():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting System...")
            break
        else:
            print("Invalid Choice")


# ---------------- RUN PROGRAM ----------------
if __name__ == "__main__":
    menu()