#!/bin/python3
# -*- coding: utf-8 -*-

# file name: profiletool.py

# standart libraries
from time import sleep
from time import process_time_ns as timer_ns
# to call the respective routines
import subprocess as ps

# local imports
import pyfactorial as pyf
import mathfactorial as mtf

def _vector():
    return range(2, 501, 2)

def _mod_asm(num):
    ps.run(["./asmmodifier.sh", num])
    sleep(0.01)

def user_defined_fac(n):
    return pyf.iterative_factorial(n)

def mathlib_defined_fac(n):
    return mtf.factorial(n)

def vm_defined_fac(n):
    ps.run(["./vm_code/hack_machine/CPUEmulator.sh",
            "./vm_code/test/Factorial.tst",
            "2&>1 >/dev/null"],
            capture_output=True,
            text=True)


def test_user_factorial():
    results = open("./results/vector_nxt_user.txt", "w")
    results.seek(0,2)

    totalTime = 0

    for num in _vector():

        start = timer_ns()
        fac = user_defined_fac(int(num))
        end = timer_ns()
        dt = end - start
        totalTime += dt

        results.write(f"{num} {dt}\n")
        print(f"factorial of {num} took {dt} nanoseconds")
        sleep(0.02)

    print(f"Total time elapsed: {totalTime} nanoseconds")
    results.close()

def test_math_factorial():
    results = open("./results/vector_nxt_mathlib.txt", "w")
    results.seek(0,2)

    totalTime = 0

    for num in _vector():

        start = timer_ns()
        fac = mathlib_defined_fac(int(num))
        end = timer_ns()
        dt = end - start
        totalTime += dt

        results.write(f"{num} {dt}\n")
        print(f"factorial of {num} took {dt} nanoseconds")
        sleep(0.02)

    print(f"Total time elapsed: {totalTime} nanoseconds")
    results.close()

def test_vm_factorial():
    results = open("./results/vector_nxt_vm.txt", "w")
    results.seek(0,2)

    totalTime = 0

    for num in _vector():

        _mod_asm(str(num)) # modify asm file

        start = timer_ns()
        vm_defined_fac(int(num))
        end = timer_ns()
        dt = end - start
        totalTime += dt

        results.write(f"{num} {dt}\n")
        print(f"factorial of {num} took {dt} nanoseconds")
        sleep(0.02)

    print(f"Total time elapsed: {totalTime} nanoseconds")
    results.close()


if __name__ == "__main__":
    test_user_factorial()
    test_math_factorial()
    test_vm_factorial()
