"""
15.2 自底向上执行
"""
import e151MatchAnalysis


def test1():
    a = e151MatchAnalysis.game_over(15, 10)
    b = e151MatchAnalysis.game_over(10, 1)
    print("a = {}, b= {}".format(a, b))
    print(e151MatchAnalysis.sim_one_game(0.4, 0.5))


test1()
