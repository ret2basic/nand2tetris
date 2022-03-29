# Chapter 8: Virtual Machine II Control

## Overview



## Project

In the previous chapter we learned how to use and implement the VM's arithmetic-logical commands and push/pop commands; in this chapter we'll learn how to use and implement the VM's **branching commands** and **function commands**. Specifically, we are going to continue implementing the following modules of our VM translator:

- `code_writer.py`
  - `write_label(label)`: Writes assembly code that effects the `label` command.
  - `write_goto(label)`: Writes assembly code that effects the `goto` command.
  - `write_if(label)`: Writes the assembly code that effects the `if-goto` command.
  - `write_function(function_name, n_vars)`: Writes assembly code that effects the `function` command.
  - `write_call(function_name, n_args)`: Writes assembly code that effects the `call` command.
  - `write_return()`: Writes assembly code that effects the `return` command.
- `VMTranslator.py`
  - This time the input might be a single file or a directory and our VMTranslator should be able to handle both cases.

### code_writer.py

We start from Project 7 and continue implementing the following functions.

- write_label(label)
- write_goto(label)
- write_if(label)
- write_function(function_name, n_vars)
- write_call(function_name, n_args)
- write_return()



### VMTranslator.py

