# return masked string
def maskify(cc):
    cc = str(cc)
    mask = "#" * len(cc[:-4])
    result = f'{mask}' + f'{cc[-4:]}'
    return result

maskify(4556364607935616)