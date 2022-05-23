import enums.enum_example_pb2 as enum_example_pb2

enum_message = enum_example_pb2.EnumMessage()

enum_message.id = 1
enum_message.day_of_week = enum_example_pb2.SATURDAY

print(enum_message)

with open("enum.bin", "wb") as f:
    f.write(enum_message.SerializeToString())
    print("writing done")
    

with open("enum.bin", "rb") as f:
    enum_message_read = enum_example_pb2.EnumMessage().FromString(f.read())
    print("reading from file")

print(enum_message_read)

