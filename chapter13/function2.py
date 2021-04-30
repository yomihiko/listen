def hello(text, name='キタサンブラック', son='ああああ'):
    print(name, text, son)


def hello2(*args, **kwargs):
    print(args, kwargs)


def hello3(text, *, name='あ'):
    print(text, name)


hello('ぽ', son='いいいい')
hello('スーパークリーク')
hello2()
hello2('あ', 'い', 'う')
hello2('え', 'お', a='さ', b='し')
hello3('ぽ', name='お')
hello3('あ', 's')
