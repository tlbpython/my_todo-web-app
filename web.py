import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.subheader(":blue[GROCERY LIST APP]")
st.title(":red[Items to be purchased]")
st.write("*Add items using input box below. Once items purchaed, select the checkbox and the item(s) will be removed.*")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo ...",
              on_change=add_todo, key='new_todo')
