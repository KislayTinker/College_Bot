import services.faq_service as faq

def test_get_answer_known_question():
    query = "What is your name?"
    answer = faq.get_answer(query)
    assert "chatbot" in answer.lower()

def test_get_answer_unknown_question():
    query = "What is the weather today?"
    answer = faq.get_answer(query)
    assert "sorry" in answer.lower()
