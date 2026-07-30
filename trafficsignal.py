print("==TRAFFIC SIGNAL STIMULATION===")
signal=input("Enter traffic signal colour:").lower()
if signal=="red":
    print("STOP")
elif signal=="yellow":
    print("WAIT")
elif signal=="green":
    print("GO")
else:
    print("invalid signal colour")
   