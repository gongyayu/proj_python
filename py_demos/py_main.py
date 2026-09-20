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
        "Select a topic", py_mod.topic_list, key="topic_select", on_change=selection_changed)

    if topic:
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
