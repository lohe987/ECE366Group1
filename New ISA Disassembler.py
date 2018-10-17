print("New ISA disassembler")
print("----------")

input_file = open("machine_code.txt", "r")
output_file = open("assembly.txt", "w")

for line in input_file:
    if(line == "\n"):
        continue

    line = line.replace("\n","")    
    print("Machine code:", line)          
    line = line.replace(" ","")

    if(line[1:4] == "000"):
        funct = "lw"
        rx = int(line[4:6],2)
        ry = int(line[6:8],2)
        print("%s $%s, ($%s)" % (funct, rx, ry))
        print()
        output_file.write("%s $%s, ($%s)\n" % (funct, rx, ry))


    elif(line[1:4] == "001"):
        funct = "sw"
        rx = int(line[4:6],2)
        ry = int(line[6:8],2)
        print("%s $%s, ($%s)" % (funct, rx, ry))
        print()
        output_file.write("%s $%s, ($%s)\n" % (funct, rx, ry))   


    elif(line[1:4] == "010"):
        funct = "add"
        rx = int(line[4:6],2)
        ry = int(line[6:8],2)
        print("%s $%s, $%s" % (funct, rx, ry))
        print()
        output_file.write("%s $%s, $%s\n" % (funct, rx, ry))

    elif(line[1:5] == "0110"):
        funct = "sltR0"
        rx = int(line[5],2)
        ry = int(line[6:8],2)
        print("%s $%s, $%s" % (funct, rx, ry))
        print()
        output_file.write("%s $%s, $%s\n" % (funct, rx, ry))

    elif(line[1:5] == "0111"):
        funct = "bezR0"
        imm = int(line[5:8],2)
        print("%s %s" % (funct, imm))
        print()
        output_file.write("%s %s\n" % (funct, imm))

    elif(line[1:4] == "100"):
        funct = "sub"
        rx = int(line[4:6],2)
        ry = int(line[6:8],2)
        print("%s $%s, $%s" % (funct, rx, ry))
        print()
        output_file.write("%s $%s, $%s\n" % (funct, rx, ry))

    elif(line[1:4] == "101"):
        funct = "andi"
        rx = int(line[4:6],2)
        ry = int(line[6:8],2)
        print("%s $%s, $%s" % (funct, rx, ry))
        print()
        output_file.write("%s $%s, $%s\n" % (funct, rx, ry))

    elif(line[1:4] == "110"):
        funct = "li"
        rx = int(line[4],2)
        imm = int(line[5:8],2)
        print("%s $%s, %s" % (funct, rx, imm))
        print()
        output_file.write("%s $%s, %s\n" % (funct, rx, imm))

    elif(line[1:6] == "11100"):
        funct = "subi"
        rx = int(line[6:8],2)
        print("%s $%s" % (funct, rx))
        print()
        output_file.write("%s $%s\n" % (funct, rx))

    elif(line[1:6] == "11101"):
        funct = "xorR0"
        rx = int(line[6:8],2)
        print("%s $%s" % (funct, rx))
        print()
        output_file.write("%s $%s\n" % (funct, rx))

    elif(line[1:6] == "11110"):
        funct = "srl"
        rx = int(line[6:8],2)
        print("%s $%s" % (funct, rx))
        print()
        output_file.write("%s $%s\n" % (funct, rx))

    elif(line[1:6] == "11111"):
        funct = "jump"
        rx = int(line[6:8],2)
        print("%s $%s" % (funct, rx))
        print()
        output_file.write("%s $%s\n" % (funct, rx))
        
input_file.close()
output_file.close()
