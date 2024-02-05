class Cleanup:
    def __init__(self):
        self.source =["%20", "%22", "%27", "%2C", "%28", "%29", "%3F", "%2F", "%E2%80%99", "%3A", "%21", "%3D", "%25",
                      "%24", "%E2%80%98", "%C3%B4", "%C3%A9", "%23", "%E2%88%92", "%C5%8D", "%C3%85", "%C5%8C",
                      "%E2%80%9C", "%E2%80%9D"]
        self.target = [" ", "\"", "'", ",", "(", ")", "?", "/", "’", ":", "!", "=", "%", "$", "‘", "ô", "é", "#", "-",
                       "ō", "Å", "Ō", "“", "”"]

    def cleanup(self, phrase):
        for i in range(len(self.source)):
            phrase = str.replace(phrase, self.source[i], self.target[i])
        return phrase
