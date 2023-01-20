import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo']
    print(todo)
    todos.append(todo+'\n')
    functions.write_todos(todos)
    st.session_state['new_todo'] = ''


st.title('my to-do app')
st.subheader('this is my to-do app.')
st.write('this app is to increase your productivity.')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo+str(index))
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        print('A', st.session_state[todo+str(index)])
        del st.session_state[todo+str(index)]
        st._rerun()
st.text_input(label='add new to-do... ', key='new_todo', on_change=add_todo,
              placeholder='add new todo: ', label_visibility='hidden')


# del st.session_state['new_todo']

# st.session_state
