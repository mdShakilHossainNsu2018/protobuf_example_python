import complex.complex_pb2 as complex_pb2

complex_message = complex_pb2.ComplexMessage()


# Wrong !!!
# one_dummy_message = complex_pb2.DummyMessage()
# one_dummy_message.id = 1
# one_dummy_message.name = "Dummy name 1"
# complex_message.one_dummy = one_dummy_message

complex_message.one_dummy.id = 1
complex_message.one_dummy.name = "Dummy"

first_multiple_message = complex_message.multiple_dummy.add()

first_multiple_message.id = 1
first_multiple_message.name = "Dump"

complex_message.multiple_dummy.add(id=2, name="2")


third_message = complex_pb2.DummyMessage()
third_message.id = 99

third_message.name = "99"

complex_message.multiple_dummy.extend([third_message])

print(complex_message)
