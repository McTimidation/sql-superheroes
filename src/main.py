import psycopg2
from psycopg2 import sql

# Database connection
def connect():
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='postgres',
        host='localhost',
        port='5432'
    )
    conn.autocommit = True
    return conn.cursor()

# Menu Function
def menu():
    print("\nMAIN MENU")
    print("1. List all Superheroes")
    print("2. List all Superpowers")
    print("3. Add a Superhero")
    print("4. Add a Superpower")
    print("5. Add a Relationship")
    print("6. List all Relationships")
    print("7. Quit")
    choice = input("Choose an option: ")
    return int(choice)

# List all Superheroes
def list_superheroes(cur):
    cur.execute("SELECT * FROM heroes;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# List all Superpowers
def list_superpowers(cur):
    cur.execute("SELECT * FROM abilities;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Add a Superhero
def add_superhero(cur):
    name = input("Enter Superhero name: ")
    cur.execute(sql.SQL("INSERT INTO heroes (name) VALUES (%s);"), (name,))

# Add a Superpower
def add_superpower(cur):
    power = input("Enter Superpower: ")
    cur.execute(sql.SQL("INSERT INTO abilities (power) VALUES (%s);"), (power,))

# Add a Relationship
def add_relationship(cur):
    hero_id = input("Enter Superhero id: ")
    power_id = input("Enter Superpower id: ")
    cur.execute(sql.SQL("INSERT INTO relationships (hero_id, power_id) VALUES (%s, %s);"), (hero_id, power_id,))

# List all Relationships
def list_relationships(cur):
    cur.execute("""SELECT heroes.name, superpowers.power 
                   FROM relationships 
                   INNER JOIN heroes ON relationships.hero_id = heroes.id 
                   INNER JOIN superpowers ON relationships.power_id = superpowers.id;""")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Main function
def main():
    cur = connect()
    while True:
        choice = menu()
        if choice == 1:
            list_superheroes(cur)
        elif choice == 2:
            list_superpowers(cur)
        elif choice == 3:
            add_superhero(cur)
        elif choice == 4:
            add_superpower(cur)
        elif choice == 5:
            add_relationship(cur)
        elif choice == 6:
            list_relationships(cur)
        elif choice == 7:
            print("Quitting the application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
