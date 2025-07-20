def generate_feedback(sentiment, scores, transcript=None):
    """
    Generates basic textual feedback based on sentiment.

    Args:
        sentiment (str): One of 'Positive', 'Negative', or 'Neutral'.
        scores (dict): VADER scores dictionary with 'pos', 'neu', 'neg', 'compound'.
        transcript (str, optional): Transcript text (not used here, but can be passed for context).

    Returns:
        str: Constructive feedback message.
    """
    if sentiment == "Positive":
        return (
            "✅ Great job! You sounded confident and optimistic. "
            "Maintain this tone while providing relevant examples."
        )
    elif sentiment == "Negative":
        return (
            "⚠️ Try to reduce negative expressions and emphasize achievements. "
            "Work on sounding more upbeat and solutions-focused."
        )
    else:
        return (
            "🟡 Your tone was neutral. Try to show more enthusiasm and clarity in your responses. "
            "Positive energy can leave a stronger impression."
        )
