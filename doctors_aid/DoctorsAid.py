x = 0

def probability(Disease_Incidence, Diagnosis_Accuracy): #function to calculate probability of patient having disease
    for s in range(len(patient_list)):
        if liste[i][1][0] == patient_list[s][0]: #I compared the names and added conditional statements according to whether the patient and their information are on the patient_list
            incidence = float(Disease_Incidence[0:2]) / float(Disease_Incidence[3:])
            true_positive = float(incidence) * 100000 * float(Diagnosis_Accuracy)
            false_positive = (100000 - float(incidence) * 100000) * (1 - float(Diagnosis_Accuracy))
            global x
            x = true_positive / (false_positive + true_positive) * 100
            x = round(x, 2)
            return f"Patient {liste[i][1][0]} has a probability of {x}% of having {patient_list[j][2]}.\n"
    return "Probability for {} cannot be calculated due to absence.\n".format(liste[i][1][0])

def recommendation(): #function that comments on whether the patient should be treated according to the risk situation
    for s in range(len(patient_list)):
        if liste[i][1][0] == patient_list[s][0]: #I compared the names and added conditional statements according to whether the patient and their information are on the patient_list
            Treatment_Risk = float(patient_list[s][5]) * 100
            if x / 100 > Treatment_Risk:
                A_Patients_Recommendation_for_a_Particular_Treatment1 = "System suggests {} to have the treatment.\n".format(liste[i][1][0])
                return A_Patients_Recommendation_for_a_Particular_Treatment1
            else:
                A_Patients_Recommendation_for_a_Particular_Treatment2 = "System suggests {} NOT to have the treatment.\n".format(liste[i][1][0])
                return A_Patients_Recommendation_for_a_Particular_Treatment2

    return "Recommendation for {} cannot be calculated due to absence.\n".format(liste[i][1][0])

def create(): #function to create patient's informations
    if liste[i][1] in patient_list:
        return "Patient {} cannot be recorded due to duplication.\n".format(liste[i][1][0])
    elif liste[i][0] == "create":
        patient_list.append(liste[i][1])
        return  "Patient {} is recorded.\n".format(liste[i][1][0])

def list(): #function to make a list which includes patient's informations
    z=""
    firstline = f'{"Patient":<8}{"Diagnosis":<16}{"Disease":<16}{"Disease":<12}{"Treatment":<16}{"Treatment"}\n'
    secondline = f'{"Name":<8}{"Accuracy":<16}{"Name":<16}{"Incıdence":<12}{"Name":<16}{"Risk"}\n'
    thirdline = f'{"-------------------------------------------------------------------------"}\n'
    z+=firstline+secondline+thirdline
    for m in range(len(patient_list)):
        firstnumber = str(float(patient_list[m][1])*100) + "%"
        secondnumber = str(float(patient_list[m][5])*100) + "%"

        q=f"{patient_list[m][0]:<8}{firstnumber:<16}{patient_list[m][2]:<16}{patient_list[m][3]:<12}{patient_list[m][4]:<16}{secondnumber}\n"
        z+=q
    return z

def remove(): #function to remove patient's informations
    for x in range(len(patient_list)):
        if liste[i][1][0] == patient_list[x][0]:
            patient_list.remove(patient_list[x])
            return "Patient {} is removed.\n".format(liste[i][1][0])
    return "Patient {} cannot be removed due to absence.\n".format(liste[i][1][0])

def input_file(): #function that allows to read the input
    global liste #Liste is which contains input informations, first line is a list and zeroth index of "liste", second line isa list and first index of "liste"...
    liste = f.readlines()
    for j in range(len(liste)):
        liste[j] = liste[j].split(" ",1)
        if len(liste[j]) == 1:
            liste[j][0] = liste[j][0].replace("\n", "") #I did it so as not to get an error due to the word "list" in input
        else:
            liste[j][1] = liste[j][1].replace("\n","")
            liste[j][1]= liste[j][1].split(", ") ##I separated lists into two lists, the first word and the remaining words

def output_file(): #function that allows to write the output
    global i #I made the "i" global because i used "i" in a lot of places
    for i in range(len(liste)):
        if liste[i][0] == "create":
            file.write(create())
        elif liste[i][0] == "probability":
            global j
            is_equal = False
            for j in range(len(patient_list)):
                if patient_list[j][0] == liste[i][1][0]:
                    file.write(probability(patient_list[j][3], patient_list[j][1]))
                    is_equal = True
            if is_equal == False:
                file.write("Probability for {} cannot be calculated due to absence.\n".format(liste[i][1][0]))
        elif liste[i][0] == "recommendation":
            file.write(recommendation())
        elif liste[i][0] == "list":
            file.write(list())

        elif liste[i][0] == "remove":
            file.write(remove())
        else:
            pass

patient_list = [] #Patient's names and their informations
with open("doctors_aid_outputs.txt", "w", encoding = "utf-8") as file:
    with open("doctors_aid_inputs.txt", "r", encoding = "utf-8") as f:
        input_file()
        output_file()

#İldeniz ÇELEBİ
#b2210356013