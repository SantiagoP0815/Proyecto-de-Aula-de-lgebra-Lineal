def main():
    print("Bienvenido al programa de cifrado/descifrado.")
    print("Por favor, ingrese la clave (matriz cuadrada de tamaño nxn cuyo determinante es primo relativo con 27):")
    n = int(input())
    while True:
        key = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(int(input()))
            key.append(row)
        if det(key) % 27 == 1:
            break
        else:
            print("La clave no es válida. Por favor, ingrese una clave cuyo determinante sea primo relativo con 27.")
    print("Por favor, ingrese el mensaje:")
    message = input().replace(" ", "").upper()
    while len(message) % n != 0:
        message += "X"
    message_matrix = []
    for i in range(len(message)):
        message_matrix.append(ord(message[i])-65)
    if input("¿Desea cifrar o descifrar el mensaje? (c/d)") == "c":
        encrypted_message = ""
        for i in range(0,len(message),n):
            message_block = []
            for j in range(n):
                message_block.append(message_matrix[i+j])
            encrypted_block = []
            for j in range(n):
                encrypted_element = 0
                for k in range(n):
                    encrypted_element += key[j][k]*message_block[k]
                encrypted_block.append(encrypted_element%27)
            for j in range(n):
                encrypted_message += chr(encrypted_block[j]+65)
        print("Mensaje cifrado:",encrypted_message)
    else:
        decrypted_message = ""
        inverse_key = inverse(key)
        for i in range(0,len(message),n):
            message_block = []
            for j in range(n):
                message_block.append(message_matrix[i+j])
            decrypted_block = []
            for j in range(n):
                decrypted_element = 0
                for k in range(n):
                    decrypted_element += inverse_key[j][k]*message_block[k]
                decrypted_block.append(decrypted_element%27)
            for j in range(n):
                decrypted_message += chr(decrypted_block[j]+65)
        print("Mensaje descifrado:",decrypted_message)

def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    else:
        determinant = 0
        for i in range(len(matrix)):
            submatrix = []
            for j in range(1,len(matrix)):
                row = []
                for k in range(len(matrix)):
                    if k != i:
                        row.append(matrix[j][k])
                submatrix.append(row)
            determinant += (-1)**i*matrix[0][i]*det(submatrix)
        return determinant

def inverse(matrix):
    determinant = det(matrix)
    if determinant == 0:
        return None
    elif len(matrix) == 1:
        return [[1/matrix[0][0]]]
    else:
        cofactor_matrix = []
        for i in range(len(matrix)):
            cofactor_row = []
            for j in range(len(matrix)):
                submatrix = []
                for k in range(len(matrix)):
                    if k != i:
                        row = []
                        for l in range(len(matrix)):
                            if l != j:
                                row.append(matrix[k][l])
                        submatrix.append(row)
                cofactor_row.append((-1)**(i+j)*det(submatrix))
            cofactor_matrix.append(cofactor_row)
        adjugate_matrix = []
        for i in range(len(cofactor_matrix)):
            adjugate_row = []
            for j in range(len(cofactor_matrix)):
                adjugate_row.append(cofactor_matrix[j][i])
            adjugate_matrix.append(adjugate_row)
        inverse_matrix = []
        for i in range(len(adjugate_matrix)):
            inverse_row = []
            for j in range(len(adjugate_matrix)):
                inverse_row.append(adjugate_matrix[i][j]/determinant)
            inverse_matrix.append(inverse_row)
        return inverse_matrix

main()