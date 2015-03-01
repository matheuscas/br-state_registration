# -*- coding: utf-8 -*-
"""File to test consistency module call"""

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
import ie.consistency as con


def test_acre_call():
    """Called the state of Acre module, to check to be working"""
    invalid_number = '0172030964577'
    acre_index = 1
    assert con.check(invalid_number, acre_index) == False


def test_alagoas_call():
    """Called the state of Alagoas module, to check to be working"""
    invalid_number = '240071779'
    alagoas_index = 2
    assert con.check(invalid_number, alagoas_index) == False


def test_amazonas_call():
    """Called the state of Amazonas module, to check to be working"""
    valid_number = '100000010'
    amazonas_index = 3
    assert con.check(valid_number, amazonas_index)


def test_amapa_call():
    """Called the state of Amapa module, to check to be working"""
    invalid_number = '172030964'
    amapa_index = 4
    assert con.check(invalid_number, amapa_index) == False


def test_bahia_call():
    """Called the state of Bahia module, to check to be working"""
    valid_number = '162345651'
    bahia_index = 5
    assert con.check(valid_number, bahia_index)


def test_ceara_call():
    """Called the state of Ceara module, to check to be working"""
    invalid_number = '60000013'
    ceara_index = 6
    assert con.check(invalid_number, ceara_index) == False


def test_distrito_federal_call():
    """Called the state of Distrito Federal module, to check to be working"""
    valid_number = '0716109443382'
    distrito_federal_index = 7
    assert con.check(valid_number, distrito_federal_index) == True


def test_espirito_santo_call():
    """Called the state of Espirito Santo module, to check to be working"""
    invalid_number = '999999905'
    espirito_santo_index = 8
    assert con.check(invalid_number, espirito_santo_index) == False


def test_goias_call():
    """Called the state of Goais module, to check to be working"""
    valid_number = '110010000'
    goais_index = 9
    assert con.check(valid_number, goais_index) == True


def test_maranhao_call():
    """Called the state of Maranhao module, to check to be working"""
    invalid_number = '120000382'
    maranhao_index = 10
    assert con.check(invalid_number, maranhao_index) == False


def test_minas_gerais_call():
    """Called the state of Minas Gerais module, to check to be working"""
    valid_number = '5055050000005'
    minas_gerais_index = 11
    assert con.check(valid_number, minas_gerais_index) == True


def test_mato_grosso_do_sul_call():
    """Called the state of Mato Grosso do Sul module, to check to be working"""
    invalid_number = '280000009'
    mato_grosso_do_sul_index = 12
    assert con.check(invalid_number, mato_grosso_do_sul_index) == False


def test_mato_grosso_call():
    """Called the state of Maro Grosso module, to check to be working"""
    valid_number = '00130000019'
    goais_index = 13
    assert con.check(valid_number, goais_index) == True


def test_para_call():
    """Called the state of Para module, to check to be working"""
    invalid_number = '159999999'
    para_index = 14
    assert con.check(invalid_number, para_index) == False


def test_paraiba_call():
    """Called the state of Paraiba module, to check to be working"""
    valid_number = '060000015'
    goais_index = 15
    assert con.check(valid_number, goais_index) == True


def test_pernambuco_call():
    """Called the state of Pernambuco module, to check to be working"""
    invalid_number = '032141833'
    pernambuco_index = 16
    assert con.check(invalid_number, pernambuco_index) == False


def test_piaui_call():
    """Called the state of Piaui module, to check to be working"""
    invalid_number = '012345672'
    piaui_index = 17
    assert con.check(invalid_number, piaui_index) == False


def test_parana_call():
    """Called the state of Parana module, to check to be working"""
    invalid_number = '1234567851'
    parana_index = 18
    assert con.check(invalid_number, parana_index) == False


def test_rio_de_janeiro_call():
    """Called the state of Rio de Janeiro module, to check to be working"""
    invalid_number = '10022009'
    parana_index = 19
    assert con.check(invalid_number, parana_index) == False


def test_rio_grande_do_norte_call():
    """Called the state of Rio Grande de Norte module, to check to be working"""
    invalid_number = '2000400407'
    rio_grande_do_norte_index = 20
    assert con.check(invalid_number, rio_grande_do_norte_index) == False


def test_rodonia_call():
    """Called the state of Rondonia module, to check to be working"""
    invalid_number = '101625214'
    rodonia_index = 21
    assert con.check(invalid_number, rodonia_index) == False


def test_roraima_call():
    """Called the state of Roraima module, to check to be working"""
    invalid_number = '240082660'
    roraima_index = 22
    assert con.check(invalid_number, roraima_index) == False


def test_rio_grande_do_sul_call():
    """Called the state of Rio Grande do Sul module, to check to be working"""
    invalid_number = '2243658796'
    rio_grande_do_sul_index = 23
    assert con.check(invalid_number, rio_grande_do_sul_index) == False


def test_santa_catarina_call():
    """Called the state of Santa Catarina module, to check to be working"""
    invalid_number = '251040855'
    santa_catarina_index = 24
    assert con.check(invalid_number, santa_catarina_index) == False


def test_sergipe_call():
    """Called the state of Sergipe module, to check to be working"""
    invalid_number = '271234560'
    sergipe_index = 25
    assert con.check(invalid_number, sergipe_index) == False


def test_sao_paulo_call():
    """Called the state of Sao Paulo module, to check to be working"""
    invalid_number = 'T011004248003'
    sao_paulo_index = 26
    assert con.check(invalid_number, sao_paulo_index) == False


def test_tocantins_call():
    """Called the state of Tocantins module, to check to be working"""
    invalid_number = '29010227831'
    tocantins_index = 27
    assert con.check(invalid_number, tocantins_index) == False