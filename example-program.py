from PyPrankError import pyprankerror

# ------- Generate Error --------
print(pyprankerror.generate_error("syntax"))
print(pyprankerror.generate_error("syntax", True))

# ------- Generate Hacked Message --------
print(pyprankerror.generate_hacked_message())
print(pyprankerror.generate_hacked_message(True))
print(pyprankerror.generate_hacked_message(True, True))

# ------- Generate Stack Trace --------
pyprankerror.generate_stacktrace()
pyprankerror.generate_stacktrace(1)
pyprankerror.generate_stacktrace(1, True)

# ------- Generate Crash Report --------
pyprankerror.generate_crash_report()
pyprankerror.generate_crash_report(True)
pyprankerror.generate_crash_report(True, True)

