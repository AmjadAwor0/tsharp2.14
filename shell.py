try:
	import basic
except ImportError:
  print("[!] ERROR tsh304: something happened while importing, Update Teasharp to fix.")

try:
	import os
except ImportError:
  print("[!] ERROR tsh304: something happened while importing, Update Teasharp to fix.")
print("""Teasharp Programming Language [Version 2.14]
(c) Amjad Awor. All rights reserved.""")
os.system("title Teasharp 2.14")

while True:
	text = input('>>> ')
	if text.strip() == "": continue
	result, error = basic.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
