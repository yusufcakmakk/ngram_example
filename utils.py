class unicode_tr(str):
    CHARMAP = {
        "to_upper": {
            "ı": "I",
            "i": "İ",
            "ü": "Ü",
            "ş": "Ş",
            "ç": "Ç",
            "ğ": "Ğ",
            "ö": "Ö"
        },
        "to_lower": {
            "I": "ı",
            "İ": "i",
            "Ü": "ü",
            "Ş": "ş",
            "Ç": "ç",
            "Ğ": "ğ",
            "Ö": "ö"
        }
    }

    def lower(self):
        for key, value in self.CHARMAP.get("to_lower").items():
            self = self.replace(key, value)
        return self.lower()

    def upper(self):
        for key, value in self.CHARMAP.get("to_upper").items():
            self = self.replace(key, value)
        return self.upper()