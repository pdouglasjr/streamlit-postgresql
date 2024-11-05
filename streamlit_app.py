import streamlit as st
from sqlalchemy import text

# Intialize connection
conn = st.connection(
    name="postgres",
    type="sql"
)

# Insert some data with conn.session
with conn.session as s:
    # clean database
    s.execute(text("DROP TABLE IF EXISTS pets;"))
    s.execute(text("CREATE TABLE pets (name TEXT, pet TEXT);"))
    s.commit()

    # data
    pet_owners = {
        'Mary': 'dog',
        'John': 'cat',
        'Robert': 'bird',
        'Jerry': 'fish', 
        'Barbara': 'cat',
        'Alex': 'dog'
    }

    # add data to database
    for k in pet_owners:
        s.execute(
            text('INSERT INTO pets (name, pet) VALUES (:name, :pet);'),
            params=dict(name=k, pet=pet_owners[k])
        )
    s.commit()

# Perform query
df = conn.query('SELECT * FROM pets')

# Print results
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")