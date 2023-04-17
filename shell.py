import time
t = time.localtime()
ct = time.strftime("%H:%M:%S", t)

print("QuommandLine 0.2")
print("help for help")

while True:
    cmdinput = input("? ")
    if cmdinput == 'help':
        print("exit")
        print("version")
        print("time")

    if cmdinput == 'exit':
        print("Wait please...")
        time.sleep(3)
        break

    if cmdinput == 'version':
        print("ql 0.2")

    if cmdinput == 'time':
        print(ct)

