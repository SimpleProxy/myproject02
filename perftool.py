#!/bin/python3

# TESTING:
from time import sleep
from timeit import default_timer as timer
from time import process_time_ns as timer_ns
from datetime import timedelta as delta

# to call the respective routines
#import os

# custom modules
import udfactorial as uf
import mldfactorial as mf

# third party module to measure time more easily
from timebudget import timebudget

timebudget.set_quiet()
timebudget.report_at_exit()

@timebudget
def user_defined_fac(n):
    return uf.udfactorial(n)

@timebudget
def mathlib_defined_fac(n):
    return mf.factorial(n)

@timebudget
def vm_defined_fac(n):
    pass

def test_user_factorial():
    results = open("user_fac_marks.txt", "w")
    results.seek(0,2)
    vector = open("vector.txt", "r")
    vector.seek(0,0)

    totalTime = 0

    for num in vector.read().split():

        start = timer_ns()
        fac = user_defined_fac(int(num))
        end = timer_ns()
        #dt = delta(seconds=(end - start))
        dt = end - start
        totalTime += dt

        results.write(f"{num}   {dt}\n")

        print(f"factorial of {num}: {fac}")
        print(f"took {dt} nanoseconds")
        sleep(0.2)

    vector.close()
    print(f"Total time elapsed: {totalTime} nanoseconds")
    results.close()

def test_math_factorial():
    results = open("mathlib_fac_marks.txt", "w")
    results.seek(0,2)
    vector = open("vector.txt", "r")
    vector.seek(0,0)

    totalTime = 0

    for num in vector.read().split():

        start = timer_ns()
        fac = mathlib_defined_fac(int(num))
        end = timer_ns()
        dt = end - start
        totalTime += dt

        results.write(f"{num}   {dt}\n")

        print(f"factorial of {num}: {fac}")
        print(f"took {dt} nanoseconds")
        sleep(0.2)

    vector.close()
    print(f"Total time elapsed: {totalTime} nanoseconds")
    results.close()

def test_vm_factorial():
    results = open("vm_fac_marks.txt", "w")
    results.seek(0,2)
    vector = open("vector.txt", "r")
    vector.seek(0,0)

    totalTime = 0

    for num in vector.read().split():

        start = timer_ns()
        fac = vm_defined_fac(int(num))
        end = timer_ns()
        dt = end - start
        totalTime += dt

        results.write(f"{num}   {dt}\n")

        print(f"factorial of {num}: {fac}")
        print(f"took {dt} nanoseconds")
        sleep(0.2)

    vector.close()
    print(f"Total time elapsed: {totalTime} nanoseconds")
    results.close()


test_user_factorial()
test_math_factorial()
