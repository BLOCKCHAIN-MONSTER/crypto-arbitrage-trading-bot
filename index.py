from web3 import Web3

#CONNECT TO WEB3
w3 = Web3(Web3.HTTPProvider(YOUR INFURA MAINET URL))
if w3:
    print('connected')
    
#ABI OF BOTH UNISWAP AND KYBERSWAP POOL
uni_abi = open("Uniswappoolabi.txt", "r").read()
kyber_abi = open('kyberswappoolabi.txt','r').read()

#POOL ADDRESS FOR BOTH UNISWAP AND KYBERSWAP
pool_address = {
  #Dai is thestable coin which worth for $1   
  'Dai_to_USDT' : ['0xB20bd5D04BE54f870D5C0d3cA85d82b34B836405', '0x8e6dBCaC80Be6E4ef4bB2ceCD83ABc41a1E968e2'],

  'Dai_to_USDC'  : ['0xAE461cA67B15dc8dc81CE7615e0320dA1A9aB8D5','0xa7b64388f0f125354A3C5d5f799EBcDf1F832419']

}


for name , address in pool_address.items():
    print(name +":")
    uni_contract = w3.eth.contract(address=address[0],abi=uni_abi)
    uni_resereve = uni_contract.functions.getReserves().call()
    uni_price = (uni_resereve[1]) *(1000000000000) / uni_resereve[0]
    print(uni_price)

    kyber_contract = w3.eth.contract(address= address[1],abi=kyber_abi)
    kyber_trade_info = kyber_contract.functions.getTradeInfo().call()
    kyber_price = kyber_trade_info[1]*(1000000000000) / kyber_trade_info[0]
    print(kyber_price)

    difference = (uni_price - kyber_price)
    addition  = uni_price + kyber_price
    #addition*0.005 is the gas fee for a dual swap
    if difference <= addition*0.005 and difference >= 0:
        profit = False
    elif difference <= addition*0.005*(-1) and difference <= 0:
        profit = False
    else:
        profit = True
    print(f"profit :{profit}")
    
