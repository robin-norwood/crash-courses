## Ethereum

- Pros:
  - Decentralized
  - Distributed


- App ideas
  - Voting system
  - Message/drop box
  - Payroll contract (Kevin Healy's example)
  - Am I hot or not voting
  - Decentralized twitter
  - Actual pyramid scheme
  - Social Security (^ lol)
  - fibonocci/pi/prime number calculator
  - pizza orderer
  - Void/black hole
  - Splitter
  - PirstFost

- censorship-proof
- tamper-proof
- Decentralized app development

- https://www.youtube.com/watch?v=U_LK0t_qaPo
  - What is ethereum video
  - What is it/what is it good for?
  - High level/hand wavy/conceptual
- It's a computer...but...
  - Slow
  - Expensive
  - not immediately decisive (~60s)
- It's a computer...that...
  - Global singleton VM
  - Hard to "crash", block, stop, control, or censor
  - ubiquitous & accessible
  - Public multi-user
  - Natively object oriented
  - deterministic
  - Verifiable & auditable
  - Easy to "fork" (etc/eth)
- Transactions are:
  - Atomic
    - Each transaction either fails (and has no effects) or succeeds (and updates the blockchain)
  - Synchronous/ordered
  - Provenance
    - Cryptographically provable who (which account) initiated a transaction
    - And what data they sent
- Objects/smart contracts are:
  - Public
    - Data & code are always visible
  - Permanent
    - Data never goes away
    - Data can only be updated by the object's code
    - Code never changes
    - Object can never be killed from the outside, only commit suicide
  - Also:
    - like user accounts, in that they can:
      - Have a balance of ether
      - Call other contracts
      - Send/receive ether
    - ...but they cannot
      - Start a transaction (can only be started from outside)



- https://www.youtube.com/watch?v=66SaEDzlmP4
  - Ethereum in 25 min
  - Gas - pay for:
     - computational unit
     - Reads/writes
     - any other resources
     - 4.7 million limit (can be voted up by miners)
  - Nonce
    - unique number/counter in each transaction
  - Ethereum VM
    - Simple VM that runs code
    - Languages:
      - Solidity
      - Serpent/viper
      - lll

- Address
  - Either a user account or smart contract
- Transaction
  - One or more messages
  - Atomic
  - Gas: an amount of ether that the transaction creator "spends" to run the transaction
  - If gas runs out, an exception is raised
- Message
  - data and/or ether
  - Sent to an address
  - Similar to function/API call
  - If sent to a user: this means sending them ether
  - If sent to a contract: runs code in that contract
    - Can result in a return value (data)
    - Can send other messages (all part of same transaction)
    - An exception rolls back entire transaction
    - Max call stack depth: 1024 (per transaction)

- https://www.youtube.com/watch?v=w9WLo33KfCY
  - What is a smart contract?
    - Building blocks of decentralized applications
- User account
  - Hash of public key
    - Private key gives permission to act on behalf of that account
  - Balance
- Smart Contract
  - "An account that is controlled by code, not by a user"
  - Code
    - immutable
    - No one, not even the creator, has the ability to change or delete the contract
  - And data
  - Balance (but can be 0)
  - Address
  - All the privs/abilities of a user/account
  - Similar to objects in an object oriented program
- Dapp
  - Decentralized apps
  - Collection of 1 or more smart contracts

- https://www.youtube.com/watch?v=2jisWLxf38E
  - Four common use cases for smart contracts:
    - Store and maintain data (public)
      - Membership of an organization
    - Maintain a contract/relationship between entities
      - Escrow
    - Provide functions
      - e.g., a library
    - Complex authentication
      - M-of-N multisignature access

- Publish a smart contract
  - Download & install Mist (etherium browser)
  - Run Mist (test net)
  - Rinkeby faucet
    - https://faucet.rinkeby.io
  - http://solidity.readthedocs.io/en/develop/

## Viper

https://github.com/ethereum/vyper

## Python and ethereum

- Solidity
  - Ethereum contract programming language similar to c/go/javascript
  - Most popular smart contract development language
  - Active, sponsored, development
  - Most features
- serpent
  - Ethereum contract programming language similar to Python
  - Semi-deprecated (maybe)
  - Stable!
  - Implemented in c++
  - No tests. :(
  - NO TESTS! :/
  - No. Tests. =(
  - Major security concerns/issues
- viper
  - Ethereum contract programming language similar to Python
  - Newer than serpent
  - unstable-ish
  - Attempts to address serpent's security concerns
  - Has tests!
  - Python 3!
  - Fewer features than serpent/solidity, by design
- pyethereum
  - Core python library of ethereum
- pyethapp
  - Python command line client
- vyper
  - Implementation of viper

## Security concerns

https://blog.acolyer.org/2017/09/01/step-by-step-towards-creating-a-safe-smart-contract-lessons-from-a-cryptocurrency-lab/

### Viper online compiler

https://viper.tools/

### Installing

```
pipenv --three
pipenv install git+https://github.com/ethereum/pydevp2p.git@develop#egg=devp2p
pipenv install git+https://github.com/ethereum/pyethereum@develop#egg=ethereum
pipenv install git+https://github.com/ethereum/pyethapp@develop#egg=pyethapp
```




- https://github.com/ethereum/pyethereum
  - git clone
  - `pipenv --three`
  - `pipenv shell`
  - `python setup.py bdist_wheel`
  - (Might need: `env LDFLAGS="-L$(brew --prefix openssl)/lib" CFLAGS="-I$(brew --prefix openssl)/include" python setup.py bdist_wheel`)
- https://github.com/ethereum/pydevp2p
  - git clone
  - `pipenv --three`
  - `pipenv shell`
  - `python setup.py bdist_wheel`
- https://github.com/ethereum/pyethapp
  - git clone
  - `pipenv --three`
  - `pipenv shell`
  - `pip install setuptools==37`
    - https://stackoverflow.com/questions/47753737/pyethapp-installation-issue-on-osx-10-13-2
  - `python setup.py bdist_wheel`
  - `brew install gmp`

## Vipyr hello-world

```
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

```
code = """
@public
@payable
def reflect():
    send(msg.sender, msg.value)
"""
```

# example using pageant.v.py
- pass args to contract __init__ via args=[<list>]
- Use "sender=tester.k0" when calling contract methods to specify sender of event (using the account *key*)
- the 'public' method for storage data creates getters
- Use positional arguments

```
from ethereum.tools import tester
import json

bc = tester.Chain()
code = """

"""

con = bc.contract(code, sender=tester.k0, language="viper")

con.add_kitten(tester.a1, "Fluffly", "https://steamuserimages-a.akamaihd.net/ugc/861727094491823008/BF4D73E6F5FCA88686AC1FFB496BC6B180E20335/", sender=tester.k0)

con.add_kitten(tester.a2, "Sparkle", "http://www.sparklecatrescue.org/uploads/4/1/3/4/41346911/_5632557_orig.jpg", sender=tester.k0)

con.add_judge(tester.a3, sender=tester.k0)
con.add_judge(tester.a4, sender=tester.k0)
con.add_judge(tester.a5, sender=tester.k0)

con.vote(1, sender=tester.k3)
con.vote(1, sender=tester.k4)
con.vote(0, sender=tester.k5)

con.winner_name()

```

# Next, work with pyethclient and test network

```
pyethapp --profile testnet -d ~/Library/Application\ Support/pyethtest account new

pyethapp --profile testnet -d ~/Library/Application\ Support/pyethtest account list
```

*FIXME: Get the above to work*

# You can also work with Mist, the ethereum browser

- Again, select test network.
- Again, don't forget your password
- Takes a few minutes to load/process the blockchain
- Need to put account id in public social media space

- Create bytecode:
`viper mirror.v.py`
- Create interface:
`viper -f json mirror.v.py`
