from model.game import BlackjackGame
from model.player import QAgent, ProbAgent, User


# u1 = User()
# dq = DeepQAgent()
# p = ProbAgent()

# b = BlackjackGame(players=[u1, dq, p])
# dq = DeepQAgent()
# p = ProbAgent()

g = BlackjackGame([User()])
try:
    g.run()
except TimeoutError:
    print("User timed out")