#!/usr/bin/env python3

from scrapper import Scrapper
import subprocess


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

if __name__ == "__main__":
  error = get_error()

  if len(error) <= 0:
    print("No error was found")
  else:
    Scrapper(error)
