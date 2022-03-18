from solcx import compile_standard
from web3 import Web3
import numpy as np
from PIL import Image


def create_contract_object(sol_file, address, private_key, RPC_Server="http://0.0.0.0:8545", chain_id=1337):
    with open("./"+sol_file, "r") as file:
        f = file.read()

    # ACCOUNT DATA FROM GANACHE
    private_key = "0x" + private_key

    # EXTRACTING NAME OF CONTRACT OBJECT FROM .SOL FILE
    s=f.replace(" ","")
    start=s.find("contract")
    end=s.find("{")
    contract_obj = s[start+8:end]

    # COMPILE
    c = compile_standard(
        {
        "language": "Solidity",
        "sources": {sol_file: {"content": f}},
        # 👇🏻 added to ["contracts"]['helloworld.sol']["HelloWorld"]
        "settings": {"outputSelection": {"*": {"*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"] }}},
        
        },
        solc_version = "0.8.12"
    )
    # BUILD CONTRACT
    abi = c["contracts"][sol_file][contract_obj]["abi"]
    b = c["contracts"][sol_file][contract_obj]["evm"]["bytecode"]["object"]
    w3 = Web3(Web3.HTTPProvider(RPC_Server))
    nonce = w3.eth.getTransactionCount(address)
    contract_build = w3.eth.contract(abi=abi, bytecode=b) # -> creates a contract object

    # DEPLOY TO GANACHE
    # create transaction object
    txn = contract_build.constructor().buildTransaction({"chainId": chain_id, "from": address, "nonce": nonce, "gasPrice": w3.eth.gas_price})
    # sign transaction
    signed_txn = w3.eth.account.sign_transaction(transaction_dict=txn, private_key=private_key)
    # # send this signed transaction
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    # confirmation of transaction
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)


    # CREATE CONTRACT OBJECT
    ca = tx_receipt.contractAddress
    contract_deployed = w3.eth.contract(address=ca, abi=abi) # <- creates a contract object
    return ca, contract_deployed

def image_to_string(img):
    """
    Convert image to string
        Parameters:
            img (PIL.Image.Image): an image from PIL     
        Returns:
            img_str (str): the image converted to text
            size (tuple): (width, height) of the image
    """
    # Flatten image
    img_np = np.array(img)
    img_np_flat = img_np.flatten()
    # convert np.array -> list
    img_list = img_np_flat.tolist()
    # convert list -> str
    img_str = str(img_list)[1:-1]

    size = img.size


    return img_str, size

def string_to_image(img_str, size):
    """
    Convert string to PIL image
        Parameters:
            img_str (str): an image in textform, e.g.: '189, 193, ...'  
            size (tuple): (width, height) of the image 
        Returns:
            image (PIL.Image.Image): a Pillow image
            
    """
    w,h = size
    # (re)convert str -> list
    img_list = img_str.split(", ")
    # (re)convert list -> np.array
    img_np_flat2 = np.array(img_list)
    # (re)convert np.array  -> image
    img_np2 = img_np_flat2.reshape((h,w))
    image = Image.fromarray(img_np2.astype(np.uint8))

    return image
