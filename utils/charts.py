import matplotlib.pyplot as plt
import os

def generate_sentiment_chart(scores, output_dir="static/output", filename="chart.png"):
    """
    Generates a pie chart showing sentiment distribution and saves it as a PNG.

    Args:
        scores (dict): Dictionary with 'pos', 'neu', and 'neg' sentiment scores.
        output_dir (str): Directory to save the chart.
        filename (str): Filename of the output chart image.

    Returns:
        str: Path to the saved chart image.
    """
    labels = ['Positive', 'Neutral', 'Negative']
    values = [scores['pos'], scores['neu'], scores['neg']]
    colors = ['#28a745', '#ffc107', '#dc3545']

    plt.figure(figsize=(4, 4))
    plt.pie(values, labels=labels, autopct='%1.1f%%', colors=colors)
    plt.title('Sentiment Distribution')

    os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists
    chart_path = os.path.join(output_dir, filename)
    plt.savefig(chart_path, bbox_inches='tight')
    plt.close()

    return chart_path
