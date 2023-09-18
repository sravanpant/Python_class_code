import locale as lc

l = [
    ["US", "English"],
    ["DE", "German"],
    ["BG", "Bulgarian"],
    ["CZ", "Czech"],
    ["DK", "Danish"],
    ["GR", "Greek"],
    ["ES", "Spanish"],
    ["EE", "Estonian"],
    ["FI", "Finnish"],
    ["FR", "French"],
    ["HR", "Croatian"],
    ["HU", "Hungarian"],
    ["IT", "Italian"],
    ["LT", "Lithuanian"],
    ["LV", "Latvian"],
    ["NL", "Dutch"],
    ["NO", "Norwegian"],
    ["PL", "Polish"],
    ["PT", "Portuguese"],
    ["RO", "Romanian"],
    ["RU", "Russian"],
    ["SK", "Slovak"],
    ["SI", "Slovenian"],
    ["SE", "Swedish"],
]

lc.setlocale(lc.LC_ALL, "en_US.utf")
print(lc.currency(12345678, grouping=True))

# for lang in lc.locale_alias.values():
#     print(lang)
