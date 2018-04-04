@public
@payable
def reflect():
    send(msg.sender, msg.value)
