def tandemBicycle(redShirtSpeeds: list, blueShirtSpeeds: list, fastest: bool) -> int:
    return sum([max(r, b) for r, b in zip(sorted(redShirtSpeeds), sorted(blueShirtSpeeds, reverse=fastest))])
