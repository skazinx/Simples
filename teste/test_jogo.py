from jogo import Jogo

def test_vitorias():
    jogo = Jogo("CS", "Leonardo", "Sniper", 5, 3, 10, 2)
    assert jogo.vitorias == 5

