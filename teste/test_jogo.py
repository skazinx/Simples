import sys
import os

# Adiciona o diretório raiz no path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from jogo import Jogo

def test_jogo_criacao():
    jogo = Jogo('Valorant', 'Leonardo', 'Jett', 10, 5, 50, 20)
    assert jogo.nome_jogo == 'Valorant'
    assert jogo.nome_pessoa == 'Leonardo'
    assert jogo.personagem == 'Jett'