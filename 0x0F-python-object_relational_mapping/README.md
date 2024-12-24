# Python Object Relational Mapping (ORM) Tasks

This repository contains tasks related to Python's Object Relational Mapping (ORM) using SQLAlchemy. Each task demonstrates a specific functionality of SQLAlchemy and how to interact with a MySQL database using Python.

## Table of Contents
1. [Introduction](#introduction)
2. [Tasks](#tasks)
   - [7. All states via SQLAlchemy](#7-all-states-via-sqlalchemy)
   - [8. First state](#8-first-state)
   - [9. Contains `a`](#9-contains-a)
   - [10. Get a state](#10-get-a-state)
   - [11. Add a new state](#11-add-a-new-state)
   - [12. Update a state](#12-update-a-state)
   - [13. Delete states](#13-delete-states)
   - [14. Cities in state](#14-cities-in-state)
   - [15. City relationship](#15-city-relationship)
   - [16. List relationship](#16-list-relationship)

---

## Introduction

In this project, you will work with SQLAlchemy, a Python SQL toolkit and Object Relational Mapper (ORM). This allows you to interact with databases using Python objects instead of writing raw SQL queries.

## Tasks

### 7. All states via SQLAlchemy
Write a script that lists all State objects from the database `hbtn_0e_6_usa`.

**Requirements:**
- Take 3 arguments: `mysql username`, `mysql password`, and `database name`.
- Use the module `SQLAlchemy`.
- Connect to a MySQL server running on `localhost` at port `3306`.

---

### 8. First state
Write a script that prints the first State object from the database `hbtn_0e_6_usa`.

**Requirements:**
- Take 3 arguments: `mysql username`, `mysql password`, and `database name`.
- Use the module `SQLAlchemy`.
- Connect to a MySQL server running on `localhost` at port `3306`.
- Print `Nothing` if the table is empty.

---

### 9. Contains `a`
Write a script that lists all State objects that contain the letter `a` from the database `hbtn_0e_6_usa`.

**Requirements:**
- Take 3 arguments: `mysql username`, `mysql password`, and `database name`.
- Use the module `SQLAlchemy`.
- Connect to a MySQL server running on `localhost` at port `3306`.

---

### 10. Get a state
Write a script that prints the State object with the name passed as an argument from the database `hbtn_0e_6_usa`.

**Requirements:**
- Take 4 arguments: `mysql username`, `mysql password`, `database name`, and `state name to search`.
- Use the module `SQLAlchemy`.
- Connect to a MySQL server running on `localhost` at port `3306`.
- Print `Not found` if the state is not present.

---

### 11. Add a new state
Write a script that adds the State object "Louisiana" to the database `hbtn_0e_6_usa`.

**Requirements:**
- Take 3 arguments: `mysql username`, `mysql password`, and `database name`.
- Use the module `SQLAlchemy`.
- Import `State` and `Base` from `model_state`.
- Connect to a MySQL server running on `localhost` at port `3306`.
- Print the new state's `id` after creation.

**Example Usage:**
```bash
guillaume@ubuntu:~/0x0F$ ./11-model_state_insert.py root root hbtn_0e_6_usa 
6
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
```

---

### 12. Update a state
Write a script that changes the name of a State object from the database `hbtn_0e_6_usa`.

**Requirements:**
- Take 3 arguments: `mysql username`, `mysql password`, and `database name`.
- Use the module `SQLAlchemy`.
- Import `State` and `Base` from `model_state`.
- Connect to a MySQL server running on `localhost` at port `3306`.
- Change the name of the State where `id = 2` to `New Mexico`.

**Example Usage:**
```bash
guillaume@ubuntu:~/0x0F$ ./12-model_state_update_id_2.py root root hbtn_0e_6_usa 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
1: California
2: New Mexico
3: Texas
4: New York
5: Nevada
6: Louisiana
```

---

### 13. Delete states
Write a script that deletes all State objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`.

**Requirements:**
- Take 3 arguments: `mysql username`, `mysql password`, and `database name`.
- Use the module `SQLAlchemy`.
- Import `State` and `Base` from `model_state`.
- Connect to a MySQL server running on `localhost` at port `3306`.

**Example Usage:**
```bash
guillaume@ubuntu:~/0x0F$ ./13-model_state_delete_a.py root root hbtn_0e_6_usa 
guillaume@ubuntu:~/0x0F$ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa 
2: New Mexico
4: New York
```

---

### 14. Cities in state
Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a City.

**City Class:**
- Inherits from `Base`.
- Links to the MySQL table `cities`.
- Includes `id`, `name`, and `state_id` attributes.

Write a script `14-model_city_fetch_by_state.py` that prints all City objects from the database `hbtn_0e_14_usa`.

**Requirements:**
- Take 3 arguments: `mysql username`, `mysql password`, and `database name`.
- Use the module `SQLAlchemy`.
- Results must be sorted in ascending order by `cities.id`.

**Example Usage:**
```bash
guillaume@ubuntu:~/0x0F$ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
California: (1) San Francisco
California: (2) San Jose
California: (3) Los Angeles
...
```

---

### 15. City relationship
Improve the files `model_city.py` and `model_state.py` to support relationships.

**State Class:**
- Includes a relationship with the `City` class.
- Deleting a State also deletes all linked City objects.

Write a script `100-relationship_states_cities.py` that creates the State "California" with the City "San Francisco" in the database `hbtn_0e_100_usa`.

**Requirements:**
- Use the `cities` relationship for all State objects.

**Example Usage:**
```bash
guillaume@ubuntu:~/0x0F$ ./100-relationship_states_cities.py root root hbtn_0e_100_usa
```

---

### 16. List relationship
Write a script that lists all State objects, and corresponding City objects, contained in the database `hbtn_0e_101_usa`.

**Requirements:**
- Take 3 arguments: `mysql username`, `mysql password`, and `database name`.
- Use the `cities` relationship for all State objects.
- Results must be sorted in ascending order by `states.id` and `cities.id`.

**Example Output:**
```bash
<state id>: <state name>
    <city id>: <city name>
```

