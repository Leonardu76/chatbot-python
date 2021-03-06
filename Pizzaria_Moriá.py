import telebot
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

token = ''
bot = telebot.TeleBot(token)


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("π Fazer pedido", callback_data="faz_ped"),
                               InlineKeyboardButton("π―οΈ Fazer reclamaΓ§Γ£o", callback_data="faz_recl"),
                               InlineKeyboardButton("π Falar com os atendentes", callback_data="falar_atend"),
                               InlineKeyboardButton("Ir ao meu github", url='https://github.com/Leonardu76')
                            )
    return markup

def option():
    option = InlineKeyboardMarkup()
    option.row_width = 2
    option.add(InlineKeyboardButton("π Pizza", callback_data="pizza"),
                                         InlineKeyboardButton("π Hamburger", callback_data="hamburger"),
                                         InlineKeyboardButton("π₯ Salada", callback_data="salad"),
                                         InlineKeyboardButton("π­ Hot-dog", callback_data="hot"))

    return option

def hot_dog():
    hot_dog = InlineKeyboardMarkup()
    hot_dog.row_width = 2
    hot_dog.add(InlineKeyboardButton("π­ Comum R$:5,90", callback_data="comum"),
                                         InlineKeyboardButton("π­ Equilibrado R$9,90", callback_data="equi"),
                                         InlineKeyboardButton("π­ Mata-fome R$:14,90", callback_data="mat"))
    return hot_dog

def salad_option():
    salad_option = InlineKeyboardMarkup()
    salad_option.row_width = 2
    salad_option.add(InlineKeyboardButton("π₯ Atum R$:19,90", callback_data="atum"),
                                         InlineKeyboardButton("π₯ Mix de folhas R$:209,90", callback_data="mix"),
                                         InlineKeyboardButton("π₯ Cenoura R$:19,90", callback_data="cen"))
    return salad_option


def pizza_option():
    pizza_option = InlineKeyboardMarkup()
    pizza_option.row_width = 2
    pizza_option.add(InlineKeyboardButton("π Calabresa R$:19,90", callback_data="cal"),
                                         InlineKeyboardButton("π Γ moda R$:49,90", callback_data="moda"),
                                         InlineKeyboardButton("π Portuguesa R$:39,90", callback_data="port"))
    return pizza_option

def hamgurguer_option():
    hamgurguer_option = InlineKeyboardMarkup()
    hamgurguer_option.row_width = 2
    hamgurguer_option.add(InlineKeyboardButton("π X-tudo R$:14,90", callback_data="tudo"),
                                         InlineKeyboardButton("π X-frango R$:9,90", callback_data="nada"),
                                         InlineKeyboardButton("π X-bacon R$:15,30", callback_data="nda"))
    return hamgurguer_option

def confirmc():
    confirmc = InlineKeyboardMarkup()
    confirmc.row_width = 5
    confirmc.add(InlineKeyboardButton("βοΈ sim", callback_data="simC"),
                          InlineKeyboardButton("β nΓ£o", callback_data="naoC"))
                          
    return confirmc

def confirmN():
    confirmN = InlineKeyboardMarkup()
    confirmN.row_width = 5
    confirmN.add(InlineKeyboardButton("βοΈ sim", callback_data="simN"),
                          InlineKeyboardButton("β nΓ£o", callback_data="naoN"))
    
    return confirmN

def payment():
    payment = InlineKeyboardMarkup()
    payment.row_width = 2
    payment.add(InlineKeyboardButton("π³ CrΓ©dito", callback_data="ccard"),
                                         InlineKeyboardButton("π³ DΓ©bito", callback_data="debcard"),
                                         InlineKeyboardButton("π΅ Dinheiro", callback_data="maney"))
    return payment

    
@bot.message_handler(func=lambda message: True)
def get_info(message):

    text = message.text

    try:
        if len(text) == 8 and int(text):
            try:
                url_base =  f'https://viacep.com.br/ws/{text}/json/'
                r = requests.get(url_base)
                json = r.json()
                cep =  json['cep']
                bairro = json['bairro']
                rua =  json['logradouro']
                bot.reply_to(message, f'Seu endereΓ§o Γ©: \n CEP: {cep} \n Bairro: {bairro} \n Rua: {rua}', reply_markup = confirmc())
            except:
                bot.reply_to(message, f'O cep: {text}, estΓ‘ incorreto \n Por favor digite um cep vΓ‘lido!!')
        
        if len(text) <= 7  and int(text):
            a = message.text
            bot.reply_to(message, f'O nΓΊmero da sua casa Γ© {a}?', reply_markup = confirmN())
    except:
            
            bot.reply_to(message, 'OlΓ‘, bem vindo a pizzaria MoriΓ‘.π', reply_markup = gen_markup())

@bot.callback_query_handler(func=lambda message: True)
def callback_query(call):
    if call.data == "faz_ped":

        bot.send_message(call.from_user.id, 'Qual serΓ‘ sua escolha?', reply_markup = option())
        
    elif call.data == "faz_recl":
        
        bot.send_message(call.from_user.id, "VocΓͺ pode fazer uma reclamaΓ§Γ£o no email pizzamoria@moria.com.")

    if call.data == "falar_atend":
     
        bot.send_message(call.from_user.id, "Um de nossos atendentes irΓ‘ te atender em breve!")

    elif call.data == "salad":

        bot.send_message(call.from_user.id, 'Qual serΓ‘ sua escolha?', reply_markup = salad_option())

    if call.data == "atum" or call.data == "mix" or call.data == "cen" or call.data == "tudo" or call.data == "nada" or call.data == "nda" or call.data == "cal" or call.data == "moda" or call.data == "port" or call.data == "comum" or call.data == "equi" or call.data == "mat":

        bot.send_message(call.from_user.id, 'Qual a forma de pagamento?', reply_markup = payment())

    elif call.data == "hot":
        bot.send_message(call.from_user.id, 'Qual serΓ‘ sua escolha', reply_markup = hot_dog())
    
    elif call.data == "pizza":

        bot.send_message(call.from_user.id, 'Qual serΓ‘ sua escolha?', reply_markup = pizza_option())


    elif call.data == "hamburger":
        bot.send_message(call.from_user.id, 'Qual serΓ‘ sua escolha', reply_markup = hamgurguer_option())

        
    if call.data == "ccard" or call.data == "debcard" or call.data == "maney" or call.data == "naoC":
        bot.send_message(call.from_user.id, 'Por favor digite seu cep!')
    
    if call.data == "simC" or call.data == 'naoN':
        bot.send_message(call.from_user.id, 'Por favor digite o numero da sua casa:')

    if call.data == "simN":
        id = call.from_user.id
        n = call.from_user.first_name
        bot.send_message(call.from_user.id, 'Tudo certo por aqui {}.  \n O nΓΊmero do seu pedido Γ©: {} \n e sairΓ‘ para entrega em atΓ© 1 hora. π\n A pizzaria MoriΓ‘ agradece a preferΓͺncia! '.format(n, id))     


bot.polling()

