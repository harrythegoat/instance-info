from fastapi import FastAPI
from libs.SystemStates.main import GetSystemStates
from libs.Linux.LsCPU import LsCPU

app = FastAPI()
# Wins Class
sys_state = GetSystemStates()

# Linux Class
lscpu = LsCPU()


@app.get("/")
def read_root():
    return {"Message": "Hello World"}


@app.get("/system/states")
def get_sys_info():
    available_states = sys_state.get_system_states()
    return {
        "available_states": available_states["output"],
        "error": available_states["error"],
        "error_message": available_states["error_message"]
    }


@app.get("/info/cpu")
def get_cpu_info():
    cpu_info = lscpu.get_cpu_info()
    return {
        "cpu_info": cpu_info["output"],
        "error": cpu_info["error"],
        "error_message": cpu_info["error_message"]
    }

