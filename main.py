import simple.simple_pb2 as simple_pb2

simple_message = simple_pb2.SimpleMessage()
simple_message.id = 1
simple_message.is_simple = True
simple_message.name = "This is a name"
simple_list = simple_message.sample_list

simple_list.append(1)
simple_list.append(2)
simple_list.append(3)

print(simple_message)

with open("simple.bin", "wb") as f:
    bytesAsString = simple_message.SerializeToString()
    f.write(bytesAsString)

with open("simple.bin", "rb") as f:
    print("reading simple message")
    simple_message_read = simple_pb2.SimpleMessage().FromString(f.read())

print(simple_message_read)



