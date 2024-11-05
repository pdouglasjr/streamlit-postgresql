import streamlit as st

# intialize connection
conn = st.connection(
    name="postgres",
    type="sql",
    url="postgresql://pdouglasjr:#10EarlinE27#@localhost:5432/pets_db"
)

# Perform query
df = conn.query('SELECT * FROM pets;', ttl="10m")

# Print results
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")