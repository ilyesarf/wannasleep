#!/usr/bin/env python3

from scrapper import Scrapper
import subprocess
import argparse
import sys

def get_error(command=None): 
  from pathlib import Path

  home_dir = str(Path.home())
  error = ""

  if command == None:
    with open(f"{home_dir}/.bash_history", "r") as f:
      command = f.readlines()[-1] #last command runned, error?
      print(command)
  try:
    if " " in command:
      output = subprocess.check_output(command.split(" "))
    else:
      output = subprocess.check_output(command.strip())
  except subprocess.CalledProcessError as e:
    error = e.output
 
  return error

def args():
  parser = argparse.ArgumentParser()
  parser.add_argument("--error", help="set error (default mode)")
  parser.add_argument("--howto",help="look for how to do something")
  parser.add_argument("--history", action="store_true")

  args = parser.parse_args()
  return args

if __name__ == "__main__":
  args = args()
  
  if args.history:
    query = get_error()
    if len(query) <= 0:
      print("No error was found")
      sys.exit(0)

  elif args.howto:
    query = args.howto
  else:
    query = args.error
  
  Scrapper(query).display_answer()
