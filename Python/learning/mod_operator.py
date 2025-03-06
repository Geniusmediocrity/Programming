import operator as op


#?   Неполный список функций из модуля operator выглядит так:

# =======================+===================+=====================+
# Операция	             |   Синтаксис	     |   Функция           |
# -----------------------+-------------------+---------------------+
# Addition	             |  a + b	         |  add(a, b)          |
# Containment Test	     |  obj in seq	     |  contains(seq, obj) |
# Division	             |  a / b	         |  truediv(a, b)      |
# Division	             |  a // b	         |  floordiv(a, b)     |
# Exponentiation	     |  a ** b	         |  pow(a, b)          |
# Modulo	             |  a % b	         |  mod(a, b)          |
# Multiplication	     |  a * b	         |  mul(a, b)          |
# Negation (Arithmetic)	 |  -a	             |  neg(a)             |
# Subtraction	         |  a - b	         |  sub(a, b)          |
# Ordering	             |  a < b	         |  lt(a, b)           |
# Ordering	             |  a <= b	         |  le(a, b)           |
# Equality	             |  a == b	         |  eq(a, b)           |
# Difference	         |  a != b	         |  ne(a, b)           |
# Ordering	             |  a >= b	         |  ge(a, b)           |
# Ordering	             |  a > b	         |  gt(a, b)           |
# =======================+===================+=====================+


print(f"add(+) = {op.add(10, 20)}")
print(f"contains(in) = {op.contains(["a", "b", "c"], "a")}")
print(f"contains(in) = {op.contains(["a", "c", "d"], "b")}")
print(f"truediv(/) = {op.truediv(91, 3)}")
print(f"floordiv(//) = {op.floordiv(91, 3)}")
print(f"power(**) = {op.pow(2, 4)}")
print(f"mod(%) = {op.mod(111, 5)}")
print(f"multiplication(*) = {op.mul(10, 5)}")
print(f"negation(-a) = {op.neg(100)}")
print(f"subtraction(a-b) = {op.sub(1000, 7)}")
print(f"ordering(lt)(<) = {op.lt(10, 10)}")
print(f"ordering(le)(<=) = {op.le(10, 10)}")
print(f"equality(100, 100)(==) = {op.eq(100, 100)}")
print(f"equality(100, 1000)(==) = {op.eq(100, 1000)}")
print(f"difference(!=) = {op.ne("ATHE", "АТНЕ")}")
print(f"ordering(ge)(>=) = {op.ge(100, 100)}")
print(f"ordering(gt)(>) = {op.gt(333, 334)}")