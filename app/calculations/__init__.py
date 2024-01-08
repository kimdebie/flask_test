def get_results(text_input: str) -> list:
    if text_input is None or text_input.strip() == "":
        return None
    return [f"{i} search text {text_input}" for i in range(100)]
