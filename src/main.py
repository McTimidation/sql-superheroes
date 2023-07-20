from database.connection import execute_query


def select_all_heroes():
    query = """
        SELECT * from heroes;
    """
    returned_items = execute_query(query).fetchall()

    for item in returned_items:
        print(item[1])
    return returned_items

# select_all_heroes()

def create_new_patient(name, about_me, bio):
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
        """
    execute_query(query, (name, about_me, bio))

create_new_patient('Harry', "I'm hairy, what do you want?", "yes")

