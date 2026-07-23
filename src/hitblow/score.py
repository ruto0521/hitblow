def evaluate_score(tries):
    if tries <= 3:
        return "🏆 天才！素晴らしい感性です！"
    elif tries <= 6:
        return "👍 ナイスプレイ！標準的なスピードです。"
    else:
        return "粘り勝ち！クリアおめでとう！"