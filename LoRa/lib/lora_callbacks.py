def lora_cb(lora): # initilize logic for callback to get and send packages.
    events = lora.events()

    if events & LoRa.TX_PACKET_EVENT: # send package with trigger
        light_manager.data_send()

# activate callbacks
lora.callback(trigger=(LoRa.TX_PACKET_EVENT), handler=lora_cb)
