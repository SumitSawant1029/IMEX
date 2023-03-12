def Predict_the_Name_of_Student(test_value,dataset):
    scores = []

    for element in dataset:
        score = sum([1 for i, j in zip(test_value, element) if i == j])
        scores.append(score)
    
    max_val = scores[0]  # initialize max_val to the first element of the list
    max_idx = 0       # initialize max_idx to 0
    for i in range(1, len(scores)):
        if scores[i] > max_val:
            max_val = scores[i]
            max_idx = i
    return max_idx


i=input("Enter the wrong spelling:-")
dataset = ['XXXXXX','Afzal', 'Sumit', 'Nigel', 'Abhay', 'Cyril']  
max1 = Predict_the_Name_of_Student(i,dataset)
print(dataset[max1])
