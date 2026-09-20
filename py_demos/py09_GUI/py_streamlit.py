import streamlit as st
from py_mod import line_print, st_print, st_code

### StartofFunc###


def pystreamlit_state():
    import streamlit as st
    sub_service = 'Chain'
    if sub_service == 'Chain':
        toolidx = []
        with st.sidebar:
            col1, col2 = st.columns(2)
            for i, tool in enumerate(tools_mod.AGENT_TOOLS, 1):
                if i % 2:
                    with col2:
                        st.checkbox(tool.name, on_change=tool_changed)
                else:
                    with col1:
                        st.checkbox(tool.name, on_change=tool_changed)

    def tool_changed():
        # Access the changed widget value via session_state
        selected = [
            tool.name for tool in tools_mod.AGENT_TOOLS
            # if tool.name is none, get function return false
            if st.session_state.get(tool.name, False)
        ]
        st.session_state.selected_tools = selected
### EndofCodeSection###
