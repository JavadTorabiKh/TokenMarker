from flask import Flask
from tronpy import Tron, Contract
from tronpy import Tron
from tronpy.keys import PrivateKey

app = Flask(__name__)
client = Tron(network="nile")


@app.route('/', methods=['GET'])
def process_data():

    processed_data = process()

    return {'result': processed_data}


def process():
    from_addr = "TEUcV3TJTwpy5fjdLwfNXqSc4L1jM31gvi"

    priv_key = PrivateKey(bytes.fromhex(
        "2269ac5ea72cb290aea4de4faa99bc1fa57e1bdcf6e3f4e7120add5edfc26ad2"))

    bytecode = "608060405234801561001057600080fd5b5060c78061001f6000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c806360fe47b11460375780636d4ce63c146062575b600080fd5b606060048036036020811015604b57600080fd5b8101908080359060200190929190505050607e565b005b60686088565b6040518082815260200191505060405180910390f35b8060008190555050565b6000805490509056fea2646970667358221220c8daade51f673e96205b4a991ab6b94af82edea0f4b57be087ab123f03fc40f264736f6c63430006000033"
    abi = [
        {
            "inputs": [],
            "name": "get",
            "outputs": [{"internalType": "uint256", "name": "retVal", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        }
    ]

    cntr = Contract(name="SimpleStore", bytecode=bytecode, abi=abi)

    txn = (
        client.trx.deploy_contract(from_addr, cntr)
        .fee_limit(5_000_000)
        .build()
        .sign(priv_key)
    )

    result = txn.broadcast().wait()
    return {
        "user": {
            "name": "javad",
            "last_name": "torabi",
            "pblicKey": "1"
        },
        "address": str(result['contract_address']),
        "token_type": "ERC20",
        "count": 1000000
    }


if __name__ == '__main__':
    app.run()
