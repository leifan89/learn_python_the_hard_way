from nose.tools import *
from ex48 import parser

def test_svo_sentence():
    sentence = parser.parser("princess eat cabinet")
    sentence_checker(sentence, "princess", "eat", "cabinet")

def test_vo_sentence():
    sentence = parser.parser("go north")
    sentence_checker(sentence, "player", "go", "north")

def test_sv_sentence():
    sentence = parser.parser("princess kill")
    sentence_checker(sentence, "princess", "kill", None)

def test_v_sentence():
    sentence = parser.parser("stop")
    sentence_checker(sentence, "player", "stop", None)

def test_svo_sentence_with_other_words():
    sentence = parser.parser("the princess eat in the 123 cabinet")
    sentence_checker(sentence, "princess", "eat", "cabinet")

def test_vo_sentence_with_unknown_words():
    sentence = parser.parser("it stop me up")
    sentence_checker(sentence, "player", "stop", "up") # "it" is not considered subject *shrug*

def test_s_sentence():
    assert_raises(parser.ParserError, parser.parser, "princess in the")

def test_so_sentence():
    assert_raises(parser.ParserError, parser.parser, "princess in cabinet")

def test_verb_not_immediately_after_subject():
    assert_raises(parser.ParserError, parser.parser, "cabinet at eat")

def sentence_checker(sentence, subject, verb, object):
    assert_equals(sentence.subject, subject)
    assert_equals(sentence.verb, verb)
    assert_equals(sentence.object, object)