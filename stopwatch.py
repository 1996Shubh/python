import time

time_start_input=input("Press enter key to start the time!!")
start=time.time()

time_start_output=input("Press enter key to end the time!!")
end=time.time()

total_time=end-start
print(f"Total time is: {round(total_time,6)}sec")