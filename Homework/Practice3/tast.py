import re
s1 = """<section> variable @"usar" ::=3030 </section>;<section> variable @"qubi"::= 6795 </section>;"""
comp = re.compile("<section> variable @\"[A-Za-z]+\"\s*::=\s*[0-9]+ </section>;")
m = comp.findall(s1)
print(m)