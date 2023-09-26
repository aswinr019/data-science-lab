# Implement perceptron learning algorithm - OR gate

class Perceptron:
    def __init__(self, learning_rate, threshold, weight1, weight2) -> None:
        self.learning_rate = learning_rate
        self.threshold = threshold
        self.weight1 = weight1
        self.weight2 = weight2

    def step_fn(self, sum):
        return (1 if (sum >= self.threshold) else 0)

    def train(self, input) -> None:
        isUpdate= True
        while(isUpdate):
            isUpdate = False
            for i in input:
                sum = (self.weight1 * i[0]) + (self.weight2 * i[1])
                co = self.step_fn(sum)
                print(perceptron.weight1,perceptron.weight2)
                if (co != i[2]):
                    isUpdate= True
                    delta_weight1 = self.learning_rate * (i[2] - co) * i[0]
                    self.weight1 = self.weight1 + delta_weight1
                    delta_weight2 = self.learning_rate * (i[2] - co) * i[1]
                    self.weight2 = self.weight2 + delta_weight2
                    

    def predict(self, test):
        sum = (self.weight1 * test[0]) + (self.weight2 * test[1])
        return (self.step_fn(sum))


lr = float(input("Enter the learning rate : "))
td = int(input("Enter the threshold : "))
w1 = float(input("Enter the weight 1 : "))
w2 = float(input("Enter the weight 2 : "))

data = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]

input1 = int(input("Enter value of x1 : "))
input2 = int(input("Enter value of x2 : "))

training_data = [input1,input2]


perceptron = Perceptron(lr, td, w1, w2)
perceptron.train(data)

print(perceptron.predict(training_data))
