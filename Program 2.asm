.data
T: .word 0xABCDEF00
best_matching_score: .word 0
best_matching_count: .word 0
Pattern_Array: .word 0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 0xEEEEEEEE, 0x44448888, 0x77777777, 0x33333333, 0xAAAAAAAA, 0xFFFF0000, 0xFFFF, 0xCCCCCCCC, 0x66666666, 0x99999999
final: .word 0
.text
lw $8, T
lw $9, Pattern_Array
addi $15, $0, 20

Main:
beq $11, $15, exit		#Program will loop throgh the Pattern_Array with a size of 20
addi $10, $0, 1			#$10 will be sll in order to compare each bit
addi $11, $0, 32		#counter for each bit in memory
add $12, $0, $0			
add $13, $0, $0

xor $8, $8, $9			#xor both T and one word from pattern array

Loop:
beq $13, $11, next		#break once all 32-bits are compared	
and $9, $8, $10			#compare bits with 1
bne $9, $0, add_1		#if the value !=, then that means that they are different
sll $10, $10, 1			#move bit to next position
addi $13, $13, 1		#counter
j Loop

add_1:
addi $12, $12, 1		#current_score
addi $13, $13, 1		#counter
sll $10, $10, 1
j Loop

next:
sub $12, $11, $12		#32- $12(current score)
lw $10, best_matching_score		
slt $11, $10, $12		#if best_matching_score < current_score
bne $11, $0, next2		#set current_score to be the best_matching_score
beq $10, $12, equal		#else if equal, keep best_matching_score the same but add 1 to best_matching_count

j set

next2:
sw $12, best_matching_score	#store the current score as the new best_matching_score
addi $11, $0, 1
sw $11, best_matching_count	#best_matching_count resets
j set

equal:
lw $11, best_matching_count	#incrment best_matching_count
addi $11, $11, 1
sw $11, best_matching_count
j set

set:
addi $14, $14, 4
lw $8, T
lw $9, Pattern_Array($14)	#load next word from Pattern_Array
lw $11, final
addi, $11, $11, 1
sw $11, final
j Main
exit:
