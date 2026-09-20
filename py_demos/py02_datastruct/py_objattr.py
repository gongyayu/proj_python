from py_mod import st_code,st_print,codelines 

### StartofFunc###

# Check if attribute exists
def py_listattr():
    listA = []
    try:
        hasattr(listA, 'append')
        listA.append('hello')
    except Exception as e:
        st_code(f"Error: {str(e)}")    
### EndofCodeSection###