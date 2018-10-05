.data 
P: .word 5
R: .word 1

.text
addi $14, $0, 0x2000
lw $15, ($14)


Loop:
lw $17, 4($14)
addi $16, $0, 6
addi $19, $0, 1
addi $9, $0, 0


beq $13, $15, Mod
addi $13, $13, 1

	
multiply:
	beq $9, 31, store
	and $8, $17, $19
	sll $19, $19, 1
	
	beq $8, 0, multiply_inc
	addu $18, $18, $16
	
multiply_inc:
	sll $16, $16, 1
	addiu $9, $9, 1
	j multiply
	

store: 
	sw $18, 4($14) 
	addu $18, $0, $0
	j Loop

Mod:
	addi $8, $0, 17
	lw $9, 4($14)
	Loop2:
	slt $10, $9, $0
	bne $10, $0, Done
	sub $9, $9, $8
	j Loop2
	
	Done:
	addi $9, $9, 17
	sw $9, 4($14)
	exit:
