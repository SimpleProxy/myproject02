#!/bin/python3

# standart libraries
from time import sleep
from time import process_time_ns as timer_ns
from timeit import default_timer as timer
from datetime import timedelta as delta
# to call the respective routines
import subprocess as ps

# local imports
import udfactorial as uf
from math import factorial as mf

# third party module that reports time mesurements
from timebudget import timebudget

# timebudget configuration
timebudget.set_quiet()
timebudget.report_at_exit()

@timebudget
def user_defined_fac(n):
    return uf.udfactorial(n)

@timebudget
def mathlib_defined_fac(n):
    return mf(n)

@timebudget
def vm_defined_fac(n):
    ps.run(["./vm_code/hack_machine/CPUEmulator.sh",
            "./vm_code/test/Factorial.tst",
            "2&>1 >/dev/null"],
            capture_output=True,
            text=True)

def test_user_factorial():
    results = open("./results/vector_nxt_user.txt", "w")
    results.seek(0,2)
    vector = open("vector_entries.txt", "r")
    vector.seek(0,0)

    totalTime = 0

    for num in vector.read().split():

        start = timer_ns()
        fac = user_defined_fac(int(num))
        end = timer_ns()
        dt = end - start
        totalTime += dt

        results.write(f"{num} {dt}\n")
        print(f"factorial of {num} took {dt} nanoseconds")
        sleep(0.05)

    vector.close()
    print(f"Total time elapsed: {totalTime} nanoseconds")
    results.close()

def test_math_factorial():
    results = open("./results/vector_nxt_mathlib.txt", "w")
    results.seek(0,2)
    vector = open("vector_entries.txt", "r")
    vector.seek(0,0)

    totalTime = 0

    for num in vector.read().split():

        start = timer_ns()
        fac = mathlib_defined_fac(int(num))
        end = timer_ns()
        dt = end - start
        totalTime += dt

        results.write(f"{num} {dt}\n")
        print(f"factorial of {num} took {dt} nanoseconds")
        sleep(0.05)

    vector.close()
    print(f"Total time elapsed: {totalTime} nanoseconds")
    results.close()

def test_vm_factorial():
    results = open("./results/vector_nxt_vm.txt", "w")
    results.seek(0,2)
    vector = open("vector_entries.txt", "r")
    vector.seek(0,0)

    totalTime = 0

    for num in vector.read().split():

        ps.run(["./asmmodifier.sh", str(num)])

        start = timer_ns()
        vm_defined_fac(int(num))
        end = timer_ns()
        dt = end - start
        totalTime += dt

        results.write(f"{num} {dt}\n")
        print(f"factorial of {num} took {dt} nanoseconds")
        sleep(0.05)

    vector.close()
    print(f"Total time elapsed: {totalTime} nanoseconds")
    results.close()


test_user_factorial()
test_math_factorial()
test_vm_factorial()
