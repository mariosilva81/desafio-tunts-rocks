import math


# Function to calculate situation and update the values list
def calculate_and_update(values):
    for row in values[1:]:
        total_classes = 60
        total_absences = int(row[2])
        p1, p2, p3 = map(int, row[3:6])

        # Calculate average
        average = (p1 + p2 + p3) / 3

        # Check if student is failed due to absences
        if total_absences > total_classes * 0.25:
            situation = "Reprovado por Falta"
            naf = 0
        else:
            # Determine situation based on average
            if average < 50:
                situation = "Reprovado por Nota"
                naf = 0
            elif average >= 50 and average < 70:
                situation = "Exame Final"
                # Calculate NAF
                naf = math.ceil(average / 2)
            else:
                situation = "Aprovado"
                naf = 0

        # Update the values list
        row.append(situation)
        row.append(naf)

        print(f"Updated student {row[0]} - Situation: {situation}, NAF: {naf}")

    return values
