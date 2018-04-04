# Kitten Cutie Pageant
#
# An organizer creates the pageant, with a prize value (wei)
#   Next, they add_kitten() up to max_kitten kittens
#   They can also add_judge() any number of judges
# Judges can vote() for either kitten
# The organizer can close() the pageant
#   This sends the prize to the winner
#   ...or divides evenly in the case of a tie
#   ...or returns it to the organizer if there are < max_kitten kittens
# At any time, anyone can get the index of the winning_kitten()
# ...or the winner_name()
# ...or the winner_owner()
# ...but this is only guaranteed to be the final winner if the pageant is_closed()

# Judges, mapped by address
judges: public({
    # Has this judge voted yet?
    voted: bool,
    # Index of the kitten voted for
    vote: num
}[address])

# Kittens, mapped by index (0, 1)
# Currently limited to 2 kittens
kittens: public({
    # Short name, 32 bytes
    name: bytes32,
    # URL of kitten, up to 128 bytes
    url: bytes <= 128,
    # Number of votes for this kitten.
    vote_count: num,
    # Is this kitten registered yet?
    registered: bool,
    # Address of the owner of this kitten.
    owner: address
}[num])

organizer: public(address)
num_kittens: public(num)
max_kittens: public(num)

# Setup global variables
@public
def __init__():
    self.organizer = msg.sender

    self.num_kittens = 0
    self.max_kittens = 2

# Computes the currently winning kitten
@public
@constant
def winning_kitten() -> num:
    winning_vote_count: num = 0
    winning_kitten: num = -1

    for k in range(2):
        if self.kittens[k].vote_count > winning_vote_count:
            winning_vote_count = self.kittens[k].vote_count
            winning_kitten = k

    return winning_kitten

# Return the name of the (currently) winner
@public
@constant
def winner_name() -> bytes32:
    return self.kittens[self.winning_kitten()].name

# Return the owner of the (currently) winner
@public
@constant
def winner_owner() -> address:
    return self.kittens[self.winning_kitten()].owner

# Return URL of the (current) winner
@public
@constant
def winner_url() -> bytes <= 128:
    return self.kittens[self.winning_kitten()].url

@public
def add_kitten(addr: address, name: bytes32, url: bytes <= 128) -> bytes32:
    # Kittens must be added by the organizer
    assert msg.sender == self.organizer
    # Only max_kittens allowed
    assert self.num_kittens < self.max_kittens

    self.kittens[self.num_kittens] = {
        name: name,
        url: url,
        vote_count: 0,
        registered: true,
        owner: addr
    }

    self.num_kittens += 1

    return name

@public
def add_judge(judge: address):
    # Throws if the sender is not the organizer.
    assert msg.sender == self.organizer

    self.judges[judge] = {
        voted: false,
        vote: -1
    }

@public
def vote(kitten: num):
    # Can't vote twice
    # Also, can't vote if not a judge
    assert not self.judges[msg.sender].voted
    # Can only vote on a registered kitten
    assert self.kittens[kitten].registered

    self.judges[msg.sender].vote = kitten
    self.judges[msg.sender].voted = true
    self.kittens[kitten].vote_count += 1
