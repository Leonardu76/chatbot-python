import telebot
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

token = '5235902751:AAHYZyt-Pr8NTLCltb2b7XBPNE1WIOww2CQ'
bot = telebot.TeleBot(token)


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Fazer pedido", callback_data="faz_ped"),
                               InlineKeyboardButton("Fazer reclamação", callback_data="faz_recl"),
                               InlineKeyboardButton("Falar com os atendentes", callback_data="falar_atend"),
                            #    InlineKeyboardButton("Pizza", callback_data="pizza"),
                            #    InlineKeyboardButton("Hamburger", callback_data="hamburger")
                            )
    return markup

def option():
    option = InlineKeyboardMarkup()
    option.row_width = 2
    option.add(InlineKeyboardButton("Pizza", callback_data="pizza"),
                                         InlineKeyboardButton("Hamburger", callback_data="hamburger"),
                                         InlineKeyboardButton("Salada", callback_data="salad"))
    return option

def salad_option():
    salad_option = InlineKeyboardMarkup()
    salad_option.row_width = 2
    salad_option.add(InlineKeyboardButton("Atum R$:19,90", callback_data="atum"),
                                         InlineKeyboardButton("Mix de folhas R$:209,90", callback_data="mix"),
                                         InlineKeyboardButton("Cenoura R$:19,90", callback_data="cen"))
    return salad_option


def pizza_option():
    pizza_option = InlineKeyboardMarkup()
    pizza_option.row_width = 2
    pizza_option.add(InlineKeyboardButton("Calabresa R$:59,90", callback_data="cal"),
                                         InlineKeyboardButton("Á moda R$:209,90", callback_data="moda"),
                                         InlineKeyboardButton("Portuguesa R$:19,90", callback_data="port"))
    return pizza_option

def hamgurguer_option():
    hamgurguer_option = InlineKeyboardMarkup()
    hamgurguer_option.row_width = 2
    hamgurguer_option.add(InlineKeyboardButton("X-tudo R$:9,90", callback_data="tudo"),
                                         InlineKeyboardButton("X-nada R$:4,90", callback_data="nada"),
                                         InlineKeyboardButton("X-tudo ou nada R$:15,30", callback_data="nda"))
    return hamgurguer_option

def payment():
    payment = InlineKeyboardMarkup()
    payment.row_width = 2
    payment.add(InlineKeyboardButton("Crédito", callback_data="ccard"),
                                         InlineKeyboardButton("Débito", callback_data="debcard"),
                                         InlineKeyboardButton("Dinheiro", callback_data="maney"))
    return payment

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):

    bot.reply_to(mensagem, 'Olá, bem vindo a pizzaria Moriá.', reply_markup = gen_markup())

@bot.callback_query_handler(func=lambda message: True)
def callback_query(call):
    if call.data == "faz_ped":

        bot.send_message(call.from_user.id, 'Qual será sua escolha?', reply_markup = option())
        
    elif call.data == "faz_recl":
        
        bot.send_message(call.from_user.id, "Você pode fazer uma reclamação no email da xuxa.")

    if call.data == "falar_atend":
     
        bot.send_message(call.from_user.id, "Um de nossos atendentes irá te atender em breve!")

    elif call.data == "salad":

        bot.send_message(call.from_user.id, 'Qual será sua escolha?', reply_markup = salad_option())

    if call.data == "atum" or call.data == "mix" or call.data == "cen":

        bot.send_message(call.from_user.id, 'Qual a forma de pagamento?', reply_markup = payment()) 

    elif call.data == "pizza":

        bot.send_message(call.from_user.id, 'Qual será sua escolha?', reply_markup = pizza_option())

    if call.data == "cal" or call.data == "moda" or call.data == "port":

        bot.send_message(call.from_user.id, 'Qual a forma de pagamento?', reply_markup = payment())

        
    elif call.data == "hamburger":
        bot.send_message(call.from_user.id, 'Qual será sua escolha', reply_markup = hamgurguer_option())

    if call.data == "tudo" or call.data == "nada" or call.data == "nda":

        bot.send_message(call.from_user.id, 'Qual a forma de pagamento?', reply_markup = payment()) 
        
    elif call.data == "ccard" or call.data == "debcard" or call.data == "maney":

        bot.send_message(call.from_user.id, 'Tudo certo por aqui, seu pedido sairá para entrega em até 3 dias. A pizzaria Moriá agradece a preferência! :)') 

    
bot.polling()

# @bot.message_handler(commands=["Pizza"])
# def opcao_pizza(mensagem):
#     texto = """
#     Qual o sabor de pizza você gostaria de pedir?
#     /Calabresa. R$: 65,99
#     /Napolitano. R$: 54,99
#     /Moria. R$:104,99
#     """
#     bot.send_message(mensagem.chat.id, texto)

# @bot.message_handler(commands=["Hamburguer"])
# def opcao_hamburguer(mensagem):
#     texto = """
#     Qual Hambúrguer você gostaria de pedir?
#     /Xtudo. R$:59,90
#     /Xnada. R$:00,00
#     /Xtudo ou nada. R$:29,95
#     """    
#     bot.send_message(mensagem.chat.id, texto)

# # Opcoes de pizzas e sanduíches

# @bot.message_handler(commands=["Calabresa"])
# def Calabresa(mensagem):
#     texto = """
#     Qual seria a forma de pagamento?
#     /Debito.
#     /Credito.
#     /Dinheiro.
#     """    
#     bot.send_message(mensagem.chat.id, texto)


# @bot.message_handler(commands=["Napolitano"])
# def Napolitano(mensagem):
#     texto = """
#     Qual seria a forma de pagamento?
#     /Debito.
#     /Credito.
#     /Dinheiro.
#     """    
#     bot.send_message(mensagem.chat.id, texto)


# @bot.message_handler(commands=["Moriá"])
# def Moria(mensagem):
#     texto = """
#     Qual seria a forma de pagamento?
#     /Debito.
#     /Credito.
#     /Dinheiro.
#     """    
#     bot.send_message(mensagem.chat.id, texto)


# @bot.message_handler(commands=["Xtudo"])
# def xtudo(mensagem):
#     texto = """
#     Qual seria a forma de pagamento?
#     /Debito.
#     /Credito.
#     /Dinheiro.
#     """    
#     bot.send_message(mensagem.chat.id, texto)


# @bot.message_handler(commands=["Xnada"])
# def xnada(mensagem):
#     texto = """
#     Qual seria a forma de pagamento?
#     /Debito.
#     /Credito.
#     /Dinheiro.
#     """    
#     bot.send_message(mensagem.chat.id, texto)

# @bot.message_handler(commands=["Xtudo ou nada"])
# def Xtudo_ou_nada(mensagem):
#     texto = """
#     Qual seria a forma de pagamento?
#     /Debito.
#     /Credito.
#     /Dinheiro.
#     """    
#     bot.send_message(mensagem.chat.id, texto)
 

# @bot.message_handler(commands=["Dinheiro"])
# def dinheiro (mensagem):

#     bot.send_message(mensagem.chat.id, "Tudo certo, o seu pedido sairá para entrega em até 50 minutos. A pizzaria Moriá agradece a preferência!")

# @bot.message_handler(commands=["Debito"])
# def debito (mensagem):

#     bot.send_message(mensagem.chat.id, "Tudo certo, o seu pedido sairá para entrega em até 50 minutos. A pizzaria Moriá agradece a preferência!")

# @bot.message_handler(commands=["Credito"])
# def credito (mensagem):

#     bot.send_message(mensagem.chat.id, "Tudo certo, o seu pedido sairá para entrega em até 50 minutos. A pizzaria Moriá agradece a preferência!")

# @bot.message_handler(commands=["Salada"])
# def opcao_salada(mensagem):
#     bot.send_message(mensagem.chat.id, "Não temos salada, peça uma pizza!")


# @bot.message_handler(commands=["1"])
# def opcao1(mensagem):
#     texto = """
#     Qual o seu pedido?
#     /Pizza.
#     /Hamburguer.
#     /Salada.
#     """
#     bot.send_message(mensagem.chat.id, texto)

# @bot.message_handler(commands=["2"])
# def opcao2(mensagem):
#     bot.send_message(mensagem.chat.id, "Para fazer uma reclamação envie um email para pizzariamoria@pizza.com")

# @bot.message_handler(commands=["3"])
# def opcao3(mensagem):
#     bot.send_message(mensagem.chat.id, "Um de nossos atendentes irá te atender em breve!")

