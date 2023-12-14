import millionaire_game
 
def test_questions():
    assert len(millionaire_game.load_questions("questions_cs.txt")) > 0