import cards


def test_deck():
    """Test that cards.ACTION_DECK actually instantiates"""
    assert len(cards.ACTION_DECK) == 43
