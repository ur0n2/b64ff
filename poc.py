import b64ff
f = open("in.txt", "r")
data = f.read()
f2 = open("out.txt", "w")
f2.write(b64ff.encode_base64(data))
f2.close()
f.close()