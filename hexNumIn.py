output = [0,1,2,3,4,5]

def textP(number):
    if (type(number) == int):
        if (number <= 255):
            if (number >= 0):
                output[0] = int(number)
                output[1] = chr(number)
                output[2] = hex(number)
                if (number <= 15):
                    output[3] = output[2].replace("0x", "0x0")
                else:
                    output[3] = output[2].replace("0x", "0x")
                output[4] = output[2].replace("0x", "")
                if (number <= 15):
                    output[5] = output[2].replace("0x", "0")
                else:
                    output[5] = output[2].replace("0x", "")
                return(output)
            else:
                print("Invaild Number: Please use a number from 0-255.")
                return("Invalid Number")
        else:
            print("Invaild Number: Please use a number from 0-255.")
            return("Invalid Number")
    else:
        print("Invaild Number: Specified input is not a integer.")
        return("Invalid Number")