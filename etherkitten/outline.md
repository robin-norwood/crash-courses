# Ethereum and Python

## What are we here to learn?

- Cryptocurrencies like Bitcoin and Ethereum are "in the news"
- I'm not here to talk to you about *investing* in cryptocurrencies, or using them to buy and sell drugs, or whatever.
- I'm more interested in the technology behind them, and more specifically some of the things that set Ethereum apart from other cryptocurrencies or blockchains
- So, tonight I'll talk about:
  - What's a blockchain? What's a cryptocurrency?
    - Keeping it as "high level" as possible
  - What is ethereum? How is it like other cryptocurrencies? How is it different?
  - What's the intersection of ethereum and Python?
  - What can we *do* with ethereum?
  - Some walkthroughs and demos of the tools in the ethereum ecosystem, especially those related to Python
  - Questions/discussion

- So what is blockchain?
  - A ledger...
    - ...with cryptography!
    - ...that can be broken into pieces (blocks!)
  - To submit a transaction to the ledger, you essentially sign it with your private key
    - This works like a gpg signature, ssh connection, or authentication with github or many other services with a *keypair*.
    - If you've used keypairs before, you know they consist of a private part, and a public part.
    - The private part you keep secret. If you lose this, you lose access to any balances you might have in the ledger, and the ability to put new transactions into the blockchain
    - The public part you use to validate that you're the one making the transaction (or rather, your private key is)
    - You can say (in public) "this is my public key" - and transactions can be tied to your identity.
      - ...but you don't have to. All anyone can tell is that this transaction was made by the person who has access to this private key (and usually a passphrase)
  - So, in short, a blockchain is a ledger that's broken up into pieces (blocks), where the transactions are signed by keypairs (the same cryptography that keeps the internet secure)
  - So it's really (really) hard to fake a transaction on the blockchain, or repeat one, or remove one once the block has been added to the chain.
  - However all of the transactions themselves are public
    - the public key (or rather, a hash of the public key)
    - the amount of the transaction/and other data
    - although you could encrypt data and put it on the blockchain.
- What's a cryptocurrency?
  - A distributed blockchain...
  - ...Where state is agreed upon by consensus
  - ...(rather than trust in a central authority)
  - ...and transactions involve exchanging a unit of value - called a bitcoin
  - ...and participants in this distributed system (called "miners") are rewarded in...bitcoin!
  - To limit the amount of bitcoin that a given miner can accumulate, three things are done:
  - ...First, an artificial cap is built into the system - 21 million BC
  - ...Second, the reward for mining a block goes down as more BC are mined (12.5BC/block atm)
  - ...Third, in order to validate transactions, miners have to do an arbitrary amount of "work" - essentially guess a random number that satisfies the given transaction.
  - Once a miner "guesses correctly", they sign the block and publish it to the other miners.
  - The rest of the network validates the block, and achieves consensus
    - ...in short, everyone agrees that the block is correct, and adds it to their copy of the blockchain.
  - So, to summarize, we've got three main things going on:
    - 1) Each node (miner) has a copy of the blockchain
    - 2) When a new transaction is submitted, it's added to a block.
    - 3) The nodes work together to validate the block, and are rewarded for their cooperation with bitcoin
  - So that's the basic model for cryptocurrency. At a (really) high level this is how bitcoin and any of the other myriad cryptocurrencies work.

# What makes ethereum different?

- Ethereum does everything I just described.
- It includes a crytocurrency (called "ether")
- You can add transactions to the ethereum blockchain that say "send ether to this other account"
- So you can send "ether", just like you can transfer bitcoin, or whatever other kinds of cryptocurrency you want.
- The key innovation of ethereum is that it adds the notion of a smart contract.
- A smart contract is basically a bit of code!
- One kind of transaction in ethereum creates a contract on the blockchain
  - More on that in a second
- Another kind is to call a function on one of these smart contracts.
- So, what happens when we call one of these functions?
  - Well, like any other function, it gets inputs - included who called it, and an optional amount of ether to send to the contract
  - Each miner in the system runs a small "virtual machine" - not a virtual machine like an EC2 instance running linux. A VM like the Java VM, or the python interpreter
  - As part of validating that transaction (where you called a function on a contract), the VM runs the code.
  - The result can have effects and side effects
  - For example:
    - Contracts can receive and store Ether! So the contract has an account, just like anyone else.
    - Contracts can send Ether! So the contract can send some or all of it's balance to some other account...including another contract!
    - Contracts can store data in their "state"...and keep tract of things
    - Contracts can return a result, which can be read by the caller
  - So wait...if these contracts are code, what's to prevent someone from writing an ether virus, or a DoS, or...
  - Well, something I haven't covered yet is the fact that each transaction in ethereum has a cost - called "gas". This is a tiny amount of ether than you "pay" the miner that validates the transaction.
  - Each operation that a smart contract executes costs a tiny amount of this gas. Once the gas runs out, the transaction fails.
  - It works on a "bidding" system - the idea being that the more "gas" you bid to run your transaction, the faster it will be picked up by the miners and run.
  - But no matter what, your transaction can only run a few operations before it runs out of gas.
- Examples!
  - Ok, so let's see this work.
  - It's always a good idea to start locally, so that's what I'll do.
  - And while I'm at it, I'll finally introduce some of the code that makes this work.
  - A couple of disclaimers:
    - All of this is very much "under development". Things are changing really, really quickly.
    - So I'll be shocked if everything works as intended.
    - And, it's likely that this will change in the coming months/years.
  - So, first let me create a git repo.
```
mkdir ~/code/etherkitten
cd ~/code/etherkitten

atom README.md

pipenv --three
pipenv shell
pipenv install ipython

```
  - There are four main Python projects related to ethereum that I'll talk about today:
  - https://github.com/ethereum/pyethereum
    - This is the "core library"
  - To install it, first I need to install a dependency, that basically handles the peer-to-peer networking bits:
```
pipenv install git+https://github.com/ethereum/pydevp2p.git@develop#egg=devp2p
```
  - Then I can install the library itself:
```
pipenv install git+https://github.com/ethereum/pyethereum@develop#egg=ethereum
```
  - And, we can do a few things with that library:
```
ipython3

from ethereum.tools import tester
import json

bc = tester.Chain()

pre = tester.mk_state_test_prefill(bc)
print(json.dumps(pre, indent=2))

```

  - And we can basically test things out on our own "test" blockchain
  - We're not using "real" ethereum here. This blockchain is just test data.

  - This is all well and good. Let me do a quick digression:
  -  https://github.com/ethereum/pyethapp
  - Pyethapp is a commandline application for interacting with the ethereum blockchain - or "an" ethereum blockchain.
  - There are basically two kinds - the "main" one, and at least a couple of "test" ones
  - We'll just use the test ones today.
  -

```
pipenv install git+https://github.com/ethereum/pyethapp@develop#egg=pyethapp
```

```
pyethapp --profile testnet -d ~/tmp/kitten account new

pyethapp --profile testnet -d ~/tmp/kitten account list

pyethapp --profile testnet -d ~/tmp/kitten run
```
-
```
pipenv install git+https://github.com/ethereum/vyper@master#egg=viper
```

- Ok, so what's *viper*?
- Remember when I said that contracts are written in bytecode?
  - No one writes bytecode - it's machine readable, not human readable
  - We write in a higher level language. Right now, there seem to be two main contenders: solidity and viper
  - Solidity is similar to javascript or C.
  - Viper is similar to python
  - By the way, from everything I can tell, solidity is better supported right now. Viper is newer, and very, very, very much in development
  - But, this is a python group, so I'm gonna go with the one that's more like Python.
  - Ok, so enough of that - let's write a contract:
```
ipython3

from ethereum.tools import tester
import json

bc = tester.Chain()

pre = tester.mk_state_test_prefill(bc)
print(json.dumps(pre, indent=2))

code = """
@public
def add(a: num, b: num) -> num:
    return a + b
"""

con = bc.contract(code, language="viper")
con.add(5, 2)
post = tester.mk_state_test_postfill(bc, pre)
```

- So, you'll notice some differences already
  - viper doesn't do dynamic types
  - We have to specify the type of the arguments and return value
  - As you'll see if we get to it, viper only supports some really, really basic data types, and they work a bit differently from python
  - So, while it's nice that viper is "kind of like" python, there's still a bit of a learning curve, and if you expect to just sit down and start writing python, and using your favorite python modules, you'll be severely disappointed.
  - There is some documentation, but, like I said, all of this is very much "in dev".
- Before we get to more advanced viper code, let's take a bit of a detour.

- Mist
  - Mist is an "ethereum browser"
  - 
