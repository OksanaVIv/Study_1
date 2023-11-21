# # # TODO  Напишите функцию count_letters
def count_letters(text):
    letter_count = {}
    text = text.lower()
    for letter_ in text:
        if letter_ not in letter_count.keys() and letter_.isalpha():
            count = text.count(letter_)
            letter_count.update({letter_: count})
    return letter_count
# # TODO Напишите функцию calculate_frequency


def calculate_frequency(letter_count):
    sum_letter = sum(letter_count.values())
    frequency = {}
    for let in letter_count:
        frequency.update({let: f'{letter_count.get(let)/sum_letter: .2f}'})
    return frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

result = calculate_frequency(count_letters(main_str))

for letter in result:
    print(f'{letter}:{result[letter]}')

# # TODO Распечатайте в столбик букву и её частоту в тексте
