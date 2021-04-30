def hello(name):
    print('{0}さん！こんにちは'.format(name))


def check_name(name):
    if len(name) >= 6:
        return True
    else:
        return None


hello('ナリタタイシン')

print(check_name('クリーク'))
print(check_name('スーパークリーク'))
