import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config(
   page_title="Exemplos com Streamlit",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)

#### 3. animate elements
st.title('3. animate elements')

progress_bar = st.progress(0)
status_text = st.empty()
chart = st.line_chart(np.random.randn(10, 2))

for i in range(10):
    # Update progress bar.
    progress_bar.progress(i + 1)

    new_rows = np.random.randn(10, 2)

    # Update status text.
    status_text.text(
        'The latest random number is: %s' % new_rows[-1, 1])

    # Append data to the chart.
    chart.add_rows(new_rows)

    # Pretend we're doing some computation that takes time.
    time.sleep(0.1)

status_text.text('Done!')
#st.balloons()

#### 4. Append data to a table or chart
st.title('4. Append data to a table or chart')

# Get some data.
data = np.random.randn(10, 2)

# Show the data as a chart.
chart = st.line_chart(data)

# Wait 1 second, so the change is clearer.
time.sleep(1)

# Grab some more data.
data2 = np.random.randn(10, 2)

# Append the new data to the existing chart.
chart.add_rows(data2)


#### 5. Batch elements and input widgets with st.form
st.title('5. Batch elements and input widgets with st.form')

# Forms can be declared using the 'with' syntax
with st.form(key='my_form'):
    text_input = st.text_input(label='Enter your name')
    submit_button = st.form_submit_button(label='Submit')

# st.form_submit_button returns True upon form submit
if submit_button:
    st.write(f'hello {text_input}')
    
    
#### 6. create an anchor link
st.title('6. create an anchor link')

st.markdown("[Section 1](#section-1)")
st.markdown("[Section 2](#section-2)")

st.header("Section 1")
st.text("Texto para a sessão 1")

st.header("Section 2")
st.text("Texto para a sessão 2")


#### 7. download a file in Streamlit
st.title('7. download a file in Streamlit')

text_contents = '''
Foo, Bar
123, 456
789, 000
'''

# Different ways to use the API

st.download_button('Download CSV', text_contents, 'text/csv', )


#### 8. download a Pandas DataFrame as a CSV
st.title('8. download a Pandas DataFrame as a CSV')

df = pd.read_csv("input_M15_SINASC_RO_2019.csv")

@st.cache_data
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')


csv = convert_df(df)

st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)


#### 9. get dataframe row-selections from a user
st.title("9. get dataframe row-selections from a user")

df = pd.DataFrame(
    {
        "Animal": ["Lion", "Elephant", "Giraffe", "Monkey", "Zebra"],
        "Habitat": ["Savanna", "Forest", "Savanna", "Forest", "Savanna"],
        "Lifespan (years)": [15, 60, 25, 20, 25],
        "Average weight (kg)": [190, 5000, 800, 10, 350],
    }
)

def dataframe_with_selections(df):
    df_with_selections = df.copy()
    df_with_selections.insert(0, "Select", False)

    # Get dataframe row-selections from user with st.data_editor
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        disabled=df.columns,
    )

    # Filter the dataframe using the temporary column, then drop the column
    selected_rows = edited_df[edited_df.Select]
    return selected_rows.drop('Select', axis=1)


selection = dataframe_with_selections(df)
st.write("Your selection:")
st.write(selection)


#### 10. insert elements out of order
st.title("10. insert elements out of order")

st.text('This will appear first')
# Appends some text to the app.

my_slot1 = st.empty()
# Appends an empty slot to the app. We'll use this later.

my_slot2 = st.empty()
# Appends another empty slot.

st.text('This will appear last')
# Appends some more text to the app.

my_slot1.text('This will appear second')
# Replaces the first empty slot with a text string.

my_slot2.line_chart(np.random.randn(20, 2))
# Replaces the second empty slot with a chart.


#### 11. remove "· Streamlit" from the app title
st.title("11. remove '· Streamlit' from the app title")

st.text('''st.set_page_config(
   page_title="Ex-stream-ly Cool App",
   page_icon="🧊",
   layout="wide",
   initial_sidebar_state="expanded",
)''')


#### 12. retrieve the filename of a file uploaded with st.file_uploader
st.title('12. retrieve the filename of a file uploaded with st.file_uploader')

uploaded_file = st.file_uploader("Upload a file")

if uploaded_file:
   st.write("Filename: ", uploaded_file.name)


#### 13. Widget updating for every second input when using session state
st.title('13. Widget updating for every second input when using session state')

# the callback function for the button will add 1 to the
# slider value up to 10
def plus_one():
    if st.session_state["slider"] < 10:
        st.session_state.slider += 1
    else:
        pass
    return

# when creating the button, assign the name of your callback
# function to the on_click parameter
add_one = st.button("Add one to the slider", on_click=plus_one, key="add_one")

# create the slider
slide_val = st.slider("Pick a number", 0, 10, key="slider")


#### 14. Static file serving
st.title('14. Static file serving')

st.write(
    f'<span style="font-size: 78px; line-height: 1">🐱</span>',
    unsafe_allow_html=True,
)

"""
# Static file serving
"""

st.caption(
    "[Code for this demo](https://github.com/streamlit/static-file-serving-demo/blob/main/streamlit_app.py)"
)

"""
Streamlit 1.18 allows you to serve small, static media files via URL. 

## Instructions

- Create a folder `static` in your app's root directory.
- Place your files in the `static` folder.
- Add the following to your `config.toml` file:

```toml
[server]
enableStaticServing = true
```

You can then access the files on `<your-app-url>/app/static/<filename>`. Read more in our 
[docs](https://docs.streamlit.io/library/advanced-features/static-file-serving).

## Examples

You can use this feature with `st.markdown` to put a link on an image:
"""

with st.echo():
    st.markdown("[![Click me](./app/static/icone.jpg)](https://streamlit.io)")

"""
Or you can use images in HTML or SVG:
"""

with st.echo():
    st.markdown(
        '<img src="icone.jpg" height="333" style="border: 5px solid orange">',
        unsafe_allow_html=True,
    )


#### 15. Secrets

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])

# And the root-level secrets are also accessible as environment variables:

import os

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)


#### 16. Mutate data
st.title('16. Mutate data')

# Criando os dados para o primeiro DataFrame
dados1 = {
    'Nome': ['Alice', 'Bob', 'Carlos', 'Daniela'],
    'Idade': [25, 30, 35, 40]
}

# Criando o primeiro DataFrame
df1 = pd.DataFrame(dados1)

# Criando os dados para o segundo DataFrame
dados2 = {
    'Nome': ['Eduardo', 'Fernanda', 'Gustavo', 'Heloisa'],
    'Idade': [27, 32, 29, 38]
}

# Criando o segundo DataFrame
df2 = pd.DataFrame(dados2)

# Add rows to a dataframe after showing it.
element = st.dataframe(df1)
element.add_rows(df2)

# Add rows to a chart after showing it.
element = st.line_chart(df1)
element.add_rows(df2)


#### 17. Display interactive widgets
st.title('17. Display interactive widgets')

st.button('Hit me')
st.checkbox('Check me out')
st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)

#### 18. Display data
st.title('18. Display data')

st.dataframe(df1)
st.table(df1)

#### 19. Display JSON
st.title('19. Display JSON')

st.json({'foo':'bar','fu':'ba'})

#### 20. Display metrics
st.title('20. Display metrics')
st.metric(label="Temp", value="273 K", delta="1.2 K")