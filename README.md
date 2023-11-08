![Workflow Status](https://github.com/software-students-fall2023/3-python-package-exercise-plant-3-0/actions/workflows/build.yml/badge.svg)

# PyPrankError
PyPrankError is a Python package that lets the user create silly (or serious) error messages, stack traces, crash reports, and hacked messages for a pranks purpose.

## Team members
1. [Nathalia Xu](https://github.com/slurp-slurp)
2. [Bobby Impastato](https://github.com/bobbyimpastato)
3. [Phoebus Yip](https://github.com/phoebusyip)
4. [Alicia Hwang](https://github.com/a-j-hwang)

## How to Install and Use
Run `pip install -i https://test.pypi.org/simple/ pyprankerror`

Now import pyprankerror to use it your own program:

`import pyprankerror`


`generate_hacked_message(is_long, is_silly)`

Description: Prints a message that makes it look like the user is being hacked. Return nothing.
* is_long (bool): False indicates shorter output, True indicates longer output.
* is_silly (bool): True indicates silly less realistic and silly variable and function names.


`generate_stacktrace(length, is_silly)`

Description: Prints a fake stack trace and returns nothing.
* length (int): 0 indicates short (9 lines) output, 1 indicates long (26 lines) output.
* is_silly (bool): True indicates less realistic and silly variable names in the stack trace.


`generate_crash_report(is_long, is_silly)`

Description: Prints a fake crash report
* is_long (bool): False indicates shorter (19 lines) output, True indicates longer output (38 lines).
* is_silly (bool): True indicates a silly and less realistic crash report.


`generate_error(err_type, isSilly)`

Description: Prints a fake error message

* err_type (str): Indicate a “syntax”, “runtime” or “logical” error type.
* is_silly (bool): True indicates silly and less realistic and crash report.
