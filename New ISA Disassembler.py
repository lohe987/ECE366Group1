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

    if(line[1:5] == "1000"):
        funct = "sub"
        ry = int(line[7],2)
        rx = int(line[5:7],2)
        print("%s $%s, $%s" % (funct, rx, ry))
        print()
        output_file.write("%s $%s, $%s\n" % (funct, rx, ry))

    elif(line[1:5] == "1001"):
        funct = "add"
        ry = int(line[7],2)
        rx = int(line[5:7],2)
        print("%s $%s, $%s" % (funct, rx, ry))
        print()
        output_file.write("%s $%s, $%s\n" % (funct, rx, ry))
        
    elif(line[1:5] == "1010"):
        funct = "srl"
        imm = int(line[7],2)
        rx = int(line[5:7],2)
        print("%s $%s, %s" % (funct, rx, imm))
        print()
        output_file.write("%s $%s, $%s\n" % (funct, rx, imm))

    elif(line[1:5] == "1011"):
        funct = "sll"
        imm = int(line[7],2)
        rx = int(line[5:7],2)
        print("%s $%s, %s" % (funct, rx, imm))
        print()
        output_file.write("%s $%s, $%s\n" % (funct, rx, imm))

    elif(line[1:5] == "1100"):
        funct = "li"
        imm = int(line[7],2)
        rx = int(line[5:7],2)
        print("%s $%s, %s" % (funct, rx, imm))
        print()
        output_file.write("%s $%s, $%s\n" % (funct, rx, imm))

    elif(line[1:5] == "1101"):
        funct = "andi"
        imm = int(line[7],2)
        rx = int(line[5:7],2)
        print("%s $%s, %s" % (funct, rx, imm))
        print()
        output_file.write("%s $%s, $%s\n" % (funct, rx, imm))
    

    elif(line[1:4] == "111"):
        funct = "xor"
        ry = int(line[6:8],2)
        rx = int(line[4:6],2)
        print("%s $%s, $%s" % (funct, rx, ry))
        print()
        output_file.write("%s $%s, $%s\n" % (funct, rx, ry))

    elif(line[1:4] == "000"):
        funct = "j"
        if(line[4] == "1"):                            #case for negative
            imm = 0b111111 - int(line[4:8],2) + 1
            print("%s -%s" % (funct, imm))
            print()
            output_file.write("%s -%s\n" % (funct, imm))
            
        else:
            imm = int(line[4:8],2)
            print("%s %s" % (funct, imm))
            print()
            output_file.write("%s %s\n" % (funct, imm))
            
    elif(line[1:4] == "001"):
        funct = "bge"
        imm = int(line[7],2)
        rx = int(line[4:6])
        ry = int(line[6])
        print("%s $%s, $%s, %s" % (funct, rx, ry, imm))
        print()
        output_file.write("%s $%s, $%s, %s\n" % (funct, rx, ry, imm))

        
    elif(line[1:4] == "100"):
        funct = "bez"
        imm = int(line[6:8],2)
        rx = int(line[4:6],2)
        print("%s $%s, %s" % (funct, rx, imm))
        print()
        output_file.write("%s $%s, %s\n" % (funct, rx, imm))

    elif(line[1:4] == "101"):
        funct = "lw"
        ry = int(line[6:8],2)
        rx = int(line[4:6],2)
        print("%s $%s, 0($%s)" % (funct, rx, ry))
        print()
        output_file.write("%s $%s, 0($%s)\n" % (funct, rx, ry))
        
    elif(line[1:4] == "110"):
        funct = "sw"
        ry = int(line[6:8],2)
        rx = int(line[4:6],2)
        print("%s $%s, 0($%s)" % (funct, rx, ry))
        print()
        output_file.write("%s $%s, 0($%s)\n" % (funct, rx, ry))

    elif(line[1:3] == "11"):
        funct = "and"
        rz = int(line[6:8],2)
        rx = int(line[3:5],2)
        ry = int(line[5],2)
        print("%s $%s, $%s, $%s" % (funct, rx, ry, rz))
        print()
        output_file.write("%s $%s, $%s, $%s" % (funct, rx, ry, rz))
        
input_file.close()
output_file.close()
