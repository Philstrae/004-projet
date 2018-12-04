# class Agent():
#   pass

# first_agent = Agent()
# second_agent = Agent()
# print(first_agent, second_agent)

class Agent:
    def say_hello(self, first_name):
        return "Bien le bonjour " + first_name + " !"
    
    def __init__(self, agreeableness):
        self.agreeableness = agreeableness  

#agent = Agent()
#print(agent.say_hello("Céline"))

first_agent = Agent(0)
print(first_agent.agreeableness)