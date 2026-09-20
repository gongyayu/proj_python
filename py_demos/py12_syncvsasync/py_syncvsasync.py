import streamlit as st
import time
import asyncio
from py_mod import line_print, st_print

### StartofFunc###


def py_sync():
    """ never used in production """
    import time

    def sync_llm_request(task):
        time.sleep(1)
        return f"task {task} is done."

    def pysync(tasks):
        start = time.time()
        for task in range(tasks):
            res = sync_llm_request(task)
            st.code(res)
        end = time.time()
        st.code(f"All the tasks cost {end - start:.2f} seconds")
    pysync(10)
### EndofCodeSection###


def py_asyncio():
    import asyncio

    async def async_llm_requessts(task):
        """ Also not used in production """
        await asyncio.sleep(1)
        return f"task {task} is done."

    async def pyasync(tasks):
        start = time.time()
        all_tasks = [async_llm_requessts(t) for t in range(tasks)]
        results = await asyncio.gather(*all_tasks)
        for res in results:
            st.code(res)
        end = time.time()
        st.code(f"async tasks cost {end - start:.2f} seconds")
    asyncio.run(pyasync(10))
### EndofCodeSection###


def py_semaphore():
    SEMAPHONE = asyncio.Semaphore(3)

    async def safe_llm_requests(task):
        """ used in production """
        async with SEMAPHONE:
            await asyncio.sleep(1)
            st.code(f"task {task} is done.")
            return task

    async def pysafe(tasks):
        start = time.time()
        all_tasks = [safe_llm_requests(t) for t in range(tasks)]
        results = await asyncio.gather(*all_tasks)
        end = time.time()
        st.code(f"All the tasks cost {end - start:.2f} seconds")
    asyncio.run(pysafe(10))
### EndofCodeSection###
