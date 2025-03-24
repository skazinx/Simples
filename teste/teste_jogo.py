from jogo import Jogo

def test_estatisticas():
    jogo = Jogo("FIFA", "Leonardo", "Zidane", 10, 2, 15, 5)
    assert jogo.nome_jogo == "FIFA"
    assert jogo.vitorias == 10
