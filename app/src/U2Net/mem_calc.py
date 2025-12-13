import os
from pathlib import Path


import psutil

saved_mem = {}

process = psutil.Process(os.getpid())

def mem(tag):
    rss = process.memory_info().rss / (1024 * 1024)
    saved_mem[tag]=float(f"{rss:.1f}")
    print(f"[{tag}]  RAM: {rss:.1f} MB")



    # tracemalloc.start()
    # mem("before_nograd")    
    
    # current, peak = tracemalloc.get_traced_memory()
    # print(f"Python allocs — current = {current/1e6:.2f} MB, peak = {peak/1e6:.2f} MB")
    # tracemalloc.stop()

