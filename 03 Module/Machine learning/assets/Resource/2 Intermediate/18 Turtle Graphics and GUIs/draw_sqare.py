import turtle as t

object_1 = t.Turtle()

object_2 = t.Turtle()

object_3 = t.Turtle()

object_4 = t.Turtle()


for _ in range(10):
    object_1.backward(50)
    object_1.right(90)

    object_2.forward(40)
    object_2.right(90)

    object_3.backward(30)
    object_3.left(90)

    object_4.forward(20)
    object_4.left(90)