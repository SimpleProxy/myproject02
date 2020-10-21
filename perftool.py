#!/bin/python3

# standart libraries
from time import sleep
from time import process_time_ns as timer_ns
from timeit import default_timer as timer
from datetime import timedelta as delta
# to call the respective routines
import subprocess #as ps

# local imports
import udfactorial as uf
import mldfactorial as mf

# third party module that reports time mesurements
from timebudget import timebudget

# timebudget configuration
timebudget.set_quiet()
timebudget.report_at_exit()

#class Test:
#    def __init__(self, vector):
#        self.vector = open("vector.txt", "r")
#
#    def run_test(self, recordFile):
#        self.vector.seek(0,0)
#        self.recordFile.seek(0,2)
#        for num in self.vector.read().split():
#
#            start = timer_ns()
#            fac = self.factorial(int(num))
#            end = timer_ns()
#            dt = end - start
#            totalTime += dt
#
#            recordFile.write(f"{num}   {dt}\n")
#
#            print(f"factorial of {num}: {fac}")
#            print(f"took {dt} nanoseconds")
#            sleep(0.2)
#
#        self.vector.close()
#        print(f"Total time elapsed: {totalTime} nanoseconds")
#        self.recordFile.close()
#
#
#
#class PyUserTest(Test):
#    def _init_(self, recordFile):
#        self.recordFile = open("user_fac_marks.txt", "w")
#
#    @timebudget
#    def factorial(self, n):
#        return uf.udfactorial(n)
#
#
#class VMTest(Test):
#    def __init__(self):
#        pass

@timebudget
def user_defined_fac(n):
    return uf.udfactorial(n)

@timebudget
def mathlib_defined_fac(n):
    return mf.factorial(n)

@timebudget
def vm_defined_fac(n):
    subprocess.run(["./vm_code/hack_machine/CPUEmulator.sh",
                    "./vm_code/test/Factorial.tst",
                    "2&>1 >/dev/null"],
                    stdin=None,  # testing
                    stdout=None, # testing
                    stderr=None, # testing
                    capture_output=True,
                    text=True)
    #return subprocess.CompletedProcess(args=args, returncode=returncode)

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

        subprocess.run(["./asmmodifier.sh", str(num)])

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
test_vm_factorial()
