import streamlit as st
import py_mod


def main():
    st.set_page_config(page_title="Python Demos V3", layout="wide")
    st.title("Python Demos", width="content")

    def selection_changed():
        py_mod.options = False

    def func_selection_changed():
        func_selection = True

    topic = st.sidebar.selectbox(
        "Select a topic", py_mod.topic_list(), key="topic_select", on_change=selection_changed)

    if topic:
        if topic == 'py99_files':
            subtopic = st.sidebar.radio("Directory starts frrom", sorted(py_mod.topdirlist),
                                                    index=0, key="key_subtopic", on_change=selection_changed)
            if subtopic:
                days = st.sidebar.text_input('Modified before days, 0 for all',value=0,on_change=selection_changed)

                bkcheck = False
                kword = None
                if subtopic in ['gyu_obsidian','proj_ai','proj_python','uv_python']:
                    backup_checked = st.sidebar.checkbox("check backup", on_change=selection_changed)
                    if backup_checked:
                        bkcheck = True
                elif subtopic == 'AI':
                    kword = st.sidebar.text_input("key word: ", value=None)

                if st.sidebar.button('Confirm'):
                    if not days:
                        days=60
                    py_mod.listfiles(subtopic, days, bkcheck, kword)
        else:
            subtopic = st.sidebar.radio("Select a Subtopic", sorted(py_mod.subtopic_list(topic)),
                                        index=0, key="key_subtopic", on_change=selection_changed)

            if subtopic:
                funclist, func_content = py_mod.get_func_info(
                    topic + '/' + subtopic)
                func_item = st.sidebar.radio(
                    "Select a function", sorted(funclist), index=None, key="func", on_change=func_selection_changed())
                if func_item:
                    py_mod.func_details(topic + '/' + subtopic,
                                        func_item, func_content)
                else:
                    st.markdown(f"Please select a function! ")
            else:
                st.markdown(f"Please select a subtopic! ")
    else:
        st.markdown(f"Please select a topic! ")


if __name__ == "__main__":
    main()
