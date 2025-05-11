# Accepting command line arguemnts in our program using argparser
import argparse

# Firstly we need to create a parser
parser = argparse.ArgumentParser("Simple Command Line Argument Utility Calculator")

parser.add_argument("num1",type=float,help="number 1")
parser.add_argument("num2",type=float,help="number 2")
parser.add_argument("operation", choices=["add","sub","div","mul"], help="Operation type")

args = parser.parse_args()

if(args.operation=="add"):
    print(f"The result is {args.num1+args.num2}")
elif(args.operation=="sub"):
    print(f"The result is {args.num1-args.num2}")
elif(args.operation=="mul"):
    print(f"The result is {args.num1*args.num2}")
elif(args.operation=="div"):
    print(f"The result is {args.num1/args.num2}")
else:
    print("Not a valid operation type")
